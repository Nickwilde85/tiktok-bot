# 🎬 Video Downloader Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)

**Telegram бот для скачивания видео из TikTok, YouTube и Pinterest в максимальном качестве**

[⚡️ Возможности](#-возможности) • [📦 Установка Python](#-установка-python-39) • [🚀 Установка бота](#-установка-бота) • [💻 Использование](#-использование)

</div>

---

## ✨ Возможности

- 🎥 **Скачивание видео** в максимальном качестве
- 📸 **Поддержка фото/слайдов** — отправка до 10 изображений (TikTok)
- ⚡ **Параллельные загрузки** — неограниченное количество пользователей
-  **Автоматическая очистка** — временные файлы удаляются
- 🔗 **Множество платформ** — TikTok, YouTube, Pinterest

## 🚀 Установка

### Требования
- Python 3.9+
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))

### 📦 Установка Python 3.9+

<details>
<summary><b>Windows</b></summary>

#### 1. Проверьте, установлен ли Python
Откройте PowerShell или CMD и выполните:
```powershell
python --version
```
Если вы видите версию 3.9 или выше — Python уже установлен. Пропустите шаги ниже.

#### 2. Скачайте установщик Python
1. Перейдите на официальный сайт: https://python.org/downloads
2. Нажмите **"Download Python 3.x.x"** (большая жёлтая кнопка)
3. Или выберите конкретную версию **Python 3.9+** из списка

#### 3. Установите Python
1. Запустите скачанный файл `.exe`
2. **ВАЖНО:** Отметьте галочку ☑️ **"Add Python to PATH"** внизу окна
3. Нажмите **"Install Now"**
4. Дождитесь завершения установки

#### 4. Проверьте установку
```powershell
python --version
pip --version
```

</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

#### 1. Обновите пакеты
```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Установите Python 3.9+
```bash
# Для Ubuntu 26.04+ (Python 3.12+ по умолчанию)
sudo apt install python3 python3-pip python3-venv -y

# Или установите конкретную версию (рекомендуется Python 3.11-3.12):
sudo apt install python3.12 python3.12-pip python3.12-venv -y
```

#### 3. Проверьте установку
```bash
python3 --version
pip3 --version
```

#### 4. Создайте алиасы (опционально)
```bash
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
source ~/.bashrc
```

#### Для старых версий Ubuntu (20.04, 22.04)
Если у вас старая версия и нужен Python 3.9+:
```bash
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-pip python3.12-venv -y
```

</details>

<details>
<summary><b>macOS</b></summary>

#### Вариант 1: Через Homebrew (рекомендуется)
```bash
# Установите Homebrew, если ещё нет
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установите Python
brew install python@3.9
```

#### Вариант 2: С официального сайта
1. Скачайте установщик: https://python.org/downloads/macos
2. Запустите `.pkg` файл
3. Следуйте инструкциям установщика

#### Проверьте установку
```bash
python3 --version
pip3 --version
```

</details>

---

### ❗ Решение проблем

<details>
<summary><b>Команда "python" не найдена (Windows)</b></summary>

1. Переустановите Python с галочкой **"Add Python to PATH"**
2. Или добавьте вручную в переменные среды:
   - `C:\Users\ВАШ_ПОЛЬЗОВАТЕЛЬ\AppData\Local\Programs\Python\Python39`
   - `C:\Users\ВАШ_ПОЛЬЗОВАТЕЛЬ\AppData\Local\Programs\Python\Python39\Scripts`

</details>

<details>
<summary><b>Ошибка "pip is not recognized"</b></summary>

Переустановите pip:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

</details>

<details>
<summary><b>Ошибка "No module named 'venv'" (Linux)</b></summary>

Установите пакет python3-venv:
```bash
sudo apt install python3-venv -y
```

</details>

---

### 🚀 Установка бота

#### Шаги

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/Nickwilde85/tiktok-bot.git
cd tiktok_bot
```

2. **Создайте виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установите зависимости**
```bash
pip install -r requirements.txt
```

4. **Настройте окружение**
```bash
cp .env.example .env
nano .env  # или любой редактор
```
Добавьте ваш `BOT_TOKEN`

## 🔑 Получение токена

1. Напишите [@BotFather](https://t.me/BotFather) в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям для создания бота
4. Скопируйте токен в файл `.env`

## ▶️ Запуск

```bash
python bot.py
```

## 💻 Использование

1. Найдите бота в Telegram
2. Отправьте `/start`
3. Отправьте ссылку на видео (TikTok, YouTube, Pinterest)
4. Получите контент в максимальном качестве!

## 🔗 Поддерживаемые ссылки

**TikTok:**
- `https://vm.tiktok.com/xxxxx` — короткие ссылки
- `https://vt.tiktok.com/xxxxx` — короткие ссылки
- `https://www.tiktok.com/@user/video/xxxxx` — видео
- `https://www.tiktok.com/@user/photo/xxxxx` — фото/слайды

**YouTube:**
- `https://www.youtube.com/watch?v=xxxxx` — видео
- `https://youtu.be/xxxxx` — короткие ссылки

**Pinterest:**
- `https://www.pinterest.com/pin/xxxxx` — пины
- `https://pin.it/xxxxx` — короткие ссылки

##  Технологии

- **Python 3.9+** — основной язык
- **aiogram 3.x** — Telegram Bot API
- **yt-dlp** — скачивание видео

## 📝 Лицензия

MIT License — свободно используйте в своих проектах

## 🤝 Вклад

Pull requests приветствуются!
