# 🎬 Video Downloader Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)

**Telegram бот для скачивания видео из TikTok, YouTube и Pinterest в максимальном качестве**

[⚡️ Возможности](#-возможности) • [📦 Установка](#-установка) • [🔧 Настройка прокси](#-настройка-прокси-для-tiktok) • [🛠️ Решение проблем](#-решение-проблем)

</div>

---

## ✨ Возможности

- 🎥 **Скачивание видео** в максимальном качестве (до 4K, если доступно)
- ⚡ **Параллельные загрузки** — неограниченное количество пользователей одновременно
- 🗑️ **Автоматическая очистка** — временные файлы удаляются автоматически
- 🔗 **Множество платформ** — TikTok, YouTube, Pinterest
- 🔄 **Продвинутые ретраи** — автоматические повторные попытки при ошибках
- 🚀 **Автозапуск** — systemd сервис для Linux серверов

---

## 📋 Системные требования

| Компонент | Минимум | Рекомендуется |
|-----------|---------|---------------|
| Python | 3.9+ | 3.11-3.12 |
| RAM | 512 MB | 1 GB+ |
| Disk | 2 GB свободно | 5 GB+ |
| Network | Стабильное соединение | Proxy (для TikTok) |

---

## 📦 Установка

### 1️⃣ Установка Python

<details>
<summary><b>🪟 Windows</b></summary>

```powershell
# 1. Скачайте Python с https://python.org/downloads
# 2. Запустите установщик
# 3. ⚠️ ОБЯЗАТЕЛЬНО отметьте "Add Python to PATH"
# 4. Нажмите "Install Now"

# Проверка установки:
python --version  # Должно показать 3.9+
pip --version
```
</details>

<details>
<summary><b>🐧 Linux (Ubuntu/Debian)</b></summary>

```bash
# Обновите систему
sudo apt update && sudo apt upgrade -y

# Установите Python и необходимые пакеты
sudo apt install -y python3 python3-pip python3-venv git curl

# Проверьте версию
python3 --version  # Должно быть 3.9+
```

**Для старых версий Ubuntu (20.04, 22.04):**
```bash
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-pip
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
# Через Homebrew (рекомендуется)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.11

# Проверка
python3 --version
```
</details>

---

### 2️⃣ Установка бота

#### Клонирование репозитория
```bash
git clone https://github.com/Nickwilde85/tiktok-bot.git
cd tiktok-bot
```

#### Создание виртуального окружения
```bash
# Создайте окружение
python3 -m venv venv

# Активируйте (Linux/macOS)
source venv/bin/activate

# Активируйте (Windows)
venv\Scripts\activate

# Вы увидите (venv) в начале строки - окружение активировано
```

#### Установка зависимостей
```bash
# Обновите pip
pip install --upgrade pip

# Установите зависимости
pip install -r requirements.txt

# ⚠️ ВАЖНО: Установите curl_cffi (необходим для TikTok)
pip install curl_cffi
```

---

### 3️⃣ Настройка окружения

#### Получение Bot Token
1. Откройте Telegram и найдите [@BotFather](https://t.me/BotFather)
2. Отправьте команду `/newbot`
3. Следуйте инструкциям:
   - Введите имя бота (например: "My Video Bot")
   - Введите username (например: "myvideobot" - должен заканчиваться на "bot")
4. Скопируйте токен вида: `123456789:ABCdefGHIjklMNOpqrSTUvwxyz`

#### Создание .env файла
```bash
# Скопируйте шаблон
cp .env.example .env

# Отредактируйте
nano .env  # или используйте любой редактор
```

#### Минимальная конфигурация
```env
BOT_TOKEN=your_telegram_bot_token_here
```

---

## 🔧 Настройка прокси (для TikTok)

### ⚠️ ВАЖНО
TikTok активно блокирует запросы с серверов. Без прокси скачивание часто не работает!

### Где купить прокси

| Тип | Рекомендуемые провайдеры | Цена | Для TikTok |
|-----|-------------------------|------|------------|
| Резидентные | proxy-seller.io, proxy6.net | $3-10/мес | ✅ Отлично |
| Мобильные | airproxy.io, litport.net | $10-30/мес | ✅ Лучший вариант |
| Дата-центр | oxylabs.io, brightdata.com | $5-15/мес | ⚠️ Иногда блокируют |

**Рекомендации:**
- Геолокация: США, Великобритания, Германия
- Тип: HTTP/HTTPS прокси
- Формат: `http://user:pass@host:port`

### Настройка в .env

```env
BOT_TOKEN=your_telegram_bot_token_here
HTTP_PROXY=http://username:password@192.121.87.135:10673
HTTPS_PROXY=http://username:password@192.121.87.135:10673
```

### Проверка прокси
```bash
# Тест через curl
curl -x http://username:password@192.121.87.135:10673 https://www.tiktok.com

# Если возвращает HTML - прокси работает
```

---

## 🚀 Запуск бота

### Ручной запуск (для тестирования)
```bash
cd /path/to/tiktok-bot
source venv/bin/activate
python bot.py

# Для остановки нажмите Ctrl+C
```

### Автозапуск через systemd (Linux сервера)

#### 1. Настройка сервиса
```bash
# Скопируйте сервис-файл
sudo cp tiktok-bot.service /etc/systemd/system/

# Отредактируйте пути под вашу систему
sudo nano /etc/systemd/system/tiktok-bot.service
```

#### 2. Пример tiktok-bot.service
```ini
[Unit]
Description=TikTok Downloader Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/home/your_username/tiktok-bot
ExecStart=/home/your_username/tiktok-bot/venv/bin/python /home/your_username/tiktok-bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### 3. Запуск и автозагрузка
```bash
# Перезагрузить systemd
sudo systemctl daemon-reload

# Включить автозапуск
sudo systemctl enable tiktok-bot

# Запустить сервис
sudo systemctl start tiktok-bot

# Проверить статус
sudo systemctl status tiktok-bot

# Посмотреть логи
sudo journalctl -u tiktok-bot -f
```

---

## 💻 Использование

### Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Приветственное сообщение и инструкция |
| `/help` | Помощь и поддерживаемые платформы |
| Отправка URL | Скачивание видео/фото |

### Поддерживаемые ссылки

**TikTok:**
- `https://vm.tiktok.com/xxxxx` — короткие ссылки
- `https://vt.tiktok.com/xxxxx` — короткие ссылки
- `https://www.tiktok.com/@user/video/xxxxx` — видео

**YouTube:**
- `https://www.youtube.com/watch?v=xxxxx` — обычные ссылки
- `https://youtu.be/xxxxx` — короткие ссылки
- `https://www.youtube.com/shorts/xxxxx` — Shorts

**Pinterest:**
- `https://www.pinterest.com/pin/xxxxx` — пины
- `https://pin.it/xxxxx` — короткие ссылки

---

## 🛠️ Решение проблем

### ❌ Ошибка: "Conflict: terminated by other getUpdates request"

**Причина:** Запущено несколько экземпляров бота с одним токеном.

**Решение:**
```bash
# Найдите все процессы бота
ps aux | grep bot.py

# Убейте лишние процессы
kill <PID>

# Или перезапустите сервис
sudo systemctl restart tiktok-bot
```

---

### ❌ Ошибка: "Download timed out" / "Got error: timed out"

**Причины:**
1. TikTok блокирует IP
2. Медленное соединение
3. Нет прокси

**Решение:**
1. Установите curl_cffi:
   ```bash
   pip install curl_cffi
   ```
2. Настройте прокси в `.env` (см. раздел выше)
3. Увеличьте таймаут в коде:
   ```python
   ydl_opts = {
       'socket_timeout': 60,
       'retries': 3,
       # ... остальные опции
   }
   ```

---

### ❌ Ошибка: "No module named 'aiogram'"

**Решение:**
```bash
# Убедитесь, что окружение активировано
source venv/bin/activate

# Переустановите зависимости
pip install -r requirements.txt
```

---

### ❌ Ошибка: "[TikTok] The extractor is attempting impersonation"

**Решение:**
```bash
# Установите curl_cffi (критически важно!)
pip install curl_cffi

# Перезапустите бота
sudo systemctl restart tiktok-bot
```

---

### ❌ Бот не отвечает на сообщения

**Проверьте:**
```bash
# 1. Статус сервиса
sudo systemctl status tiktok-bot

# 2. Логи ошибок
sudo journalctl -u tiktok-bot -n 50 --no-pager

# 3. Проверьте токен
cat .env | grep BOT_TOKEN

# 4. Проверьте, не запущен ли бот в другом месте
ps aux | grep bot.py
```

---

### ❌ Ошибка: "Video is too big"

**Причина:** Telegram ограничивает размер файлов (50 MB для ботов).

**Решение:**
- Используйте ссылки на более короткие видео
- Или измените формат в `bot.py`:
  ```python
  'format': 'best[filesize<50M]',  # Только файлы < 50MB
  ```

---

## 📝 Обновление бота

```bash
cd /path/to/tiktok-bot

# Сохраните .env
cp .env /tmp/.env.backup

# Обновите код
git pull origin main

# Восстановите .env
cp /tmp/.env.backup .env

# Обновите зависимости
source venv/bin/activate
pip install -r requirements.txt

# Перезапустите
sudo systemctl restart tiktok-bot
```

---

## 🔍 Диагностика

### Проверка yt-dlp
```bash
# Тест скачивания
yt-dlp --no-download --print title "https://www.tiktok.com/@username/video/123456"

# Тест с прокси
yt-dlp --proxy "http://user:pass@host:port" --no-download --print title "URL"
```

### Проверка прокси
```bash
# HTTP прокси
curl -x http://user:pass@host:port https://www.tiktok.com -I

# Должен вернуть: HTTP/2 200
```

### Полные логи
```bash
# Все логи бота
sudo journalctl -u tiktok-bot --no-pager

# Последние 100 строк с отслеживанием
sudo journalctl -u tiktok-bot -f -n 100
```

---

## 🆘 FAQ

**Q: Почему TikTok не скачивается?**  
A: TikTok блокирует серверные IP. Нужен резидентный/мобильный прокси.

**Q: Можно ли использовать бесплатные прокси?**  
A: Можно попробовать, но обычно они быстро банятся TikTok.

**Q: Работает ли бот на Windows?**  
A: Да, но systemd автозапуск доступен только на Linux.

**Q: Как ограничить доступ к боту?**  
A: Добавьте проверку user_id в `process_download()`.

**Q: Где хранятся скачанные видео?**  
A: Во временной директории `/tmp` - автоматически удаляются.

---

## 🛡️ Безопасность

- **НЕ коммитьте `.env` файл** — там ваш токен!
- **Используйте прокси** — защитит ваш сервер от банов
- **Ограничьте доступ** к серверу через firewall

---

## 🤝 Вклад в проект

Pull requests приветствуются!

1. Форкните репозиторий
2. Создайте ветку: `git checkout -b feature/my-feature`
3. Коммитьте: `git commit -am 'Add feature'`
4. Пуш: `git push origin feature/my-feature`
5. Создайте Pull Request

---

## 📜 Лицензия

MIT License — свободно используйте в своих проектах.

---

<div align="center">

**⭐ Если проект полезен — поставьте звёздочку на GitHub!**

</div>
