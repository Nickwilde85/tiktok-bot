import asyncio
import logging
import os
import tempfile
import re

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import (
    Message, FSInputFile, URLInputFile, InputMediaPhoto
)
from dotenv import load_dotenv
import yt_dlp
import aiohttp

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set in .env file")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()




def download_tiktok_video(url: str, output_path: str) -> str:
    """Download TikTok video in highest quality using yt-dlp."""
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.tiktok.com/',
        }
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


def normalize_tiktok_url(url: str) -> str:
    """Convert photo URLs to video format for yt-dlp compatibility."""
    # Replace /photo/ with /video/ for yt-dlp
    url = re.sub(r'/photo/', '/video/', url)
    return url


async def extract_tiktok_photos(url: str) -> list:
    """Extract photo URLs from TikTok photo post by parsing HTML."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.tiktok.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    
    # Try to extract from JSON data in the page
    # TikTok stores data in __NEXT_DATA__ or similar script tags
    photo_urls = []
    
    # Pattern 1: Look for image URLs in the HTML (broader patterns)
    patterns = [
        r'https://[^"\'\\s]*tiktokcdn\.com[^"\'\\s]*',
        r'https://[^"\'\\s]*byteimg\.com[^"\'\\s]*',
        r'https://[^"\'\\s]*tiktok\.com[^"\'\\s]*img[^"\'\\s]*',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, html)
        for match in matches:
            # Clean up the URL (remove trailing characters)
            clean_url = match.split('?')[0].split('&')[0]
            if clean_url not in photo_urls:
                photo_urls.append(clean_url)
    
    # Pattern 2: Try to find JSON data with image URLs
    json_patterns = [
        r'"imagePost":\s*\{[^}]*"images":\s*\[([^\]]+)\]',
        r'"images":\s*\[([^\]]+)\]',
        r'"url":\s*"([^"]*tiktokcdn[^"]*)"',
        r'"url":\s*"([^"]*byteimg[^"]*)"',
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, html)
        for match in matches:
            if isinstance(match, str):
                if match not in photo_urls:
                    photo_urls.append(match)
            else:
                for m in match:
                    if isinstance(m, str) and m not in photo_urls:
                        photo_urls.append(m)
    
    # Filter only image URLs
    image_urls = []
    for url in photo_urls:
        if any(ext in url for ext in ['.jpg', '.jpeg', '.png', '.webp']):
            if url not in image_urls:
                image_urls.append(url)
    
    logger.info(f"Extracted {len(image_urls)} image URLs from HTML")
    return image_urls[:10]  # Limit to 10 photos


def download_tiktok_content(url: str, temp_dir: str) -> dict:
    """Download TikTok content (video or photos) and return info."""
    # Check if it's a photo post
    if '/photo/' in url:
        # Return marker that this needs async photo extraction
        return {'type': 'photos_async', 'url': url}
    
    # It's a video - download it with yt-dlp (no photo check needed here)
    output_path = os.path.join(temp_dir, "video.%(ext)s")
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True,
        'no_warnings': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.tiktok.com/',
        }
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)
        return {
            'type': 'video',
            'path': video_path,
            'title': info.get('title', 'TikTok Video'),
            'webpage_url': info.get('webpage_url', url)
        }


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я бот для скачивания видео из TikTok.\n\n"
        "📱 Просто отправь мне ссылку на TikTok видео или фото, и я скачаю его в максимальном качестве.\n\n"
        "⚡️ Поддерживаются параллельные загрузки!"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📋 <b>Как использовать:</b>\n"
        "1. Отправь ссылку на TikTok видео или фото\n"
        "2. Дождись загрузки\n"
        "3. Получи контент в максимальном качестве!\n\n"
        "🔗 <b>Поддерживаемые форматы ссылок:</b>\n"
        "• https://vm.tiktok.com/xxxxx\n"
        "• https://www.tiktok.com/@user/video/xxxxx\n"
        "• https://www.tiktok.com/@user/photo/xxxxx",
        parse_mode="HTML"
    )


async def process_download(message: Message, url: str):
    """Download and send content (video or photos) to the chat."""
    logger.info(f"Processing URL: {url}")
    status_message = await message.answer("⏳ Скачиваю контент в максимальном качестве...")
    
    try:
        # Normalize URL for yt-dlp (convert /photo/ to /video/)
        url = normalize_tiktok_url(url)
        logger.info(f"Normalized URL: {url}")
        
        # Download with yt-dlp
        await status_message.edit_text("📤 Отправляю видео...")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            loop = asyncio.get_event_loop()
            content = await loop.run_in_executor(
                None, download_tiktok_content, url, temp_dir
            )
            
            video_file = FSInputFile(content['path'])
            await message.answer_video(
                video=video_file,
                caption=f"✅ Готово! Видео скачано в максимальном качестве.\n\n🔗 {content['webpage_url']}",
                supports_streaming=True
            )
            
            await status_message.delete()
            
    except Exception as e:
        logger.error(f"Error downloading content: {e}")
        await status_message.edit_text(
            "❌ Ошибка при скачивании контента.\n"
            "Проверьте ссылку и попробуйте снова."
        )


@dp.message(F.text.regexp(r'https?://(?:www\.)?(?:tiktok\.com|vm\.tiktok\.com|vt\.tiktok\.com)/.+'))
async def download_video(message: Message):
    url = message.text.strip()
    await process_download(message, url)


@dp.message()
async def unknown_message(message: Message):
    await message.answer(
        "🤔 Я не понимаю это сообщение.\n"
        "Отправь мне ссылку на TikTok видео или используй /help"
    )


async def main():
    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
