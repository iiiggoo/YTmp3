# 🎵 YTmp3 - YouTube MP3 Downloader

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A beautiful and feature-rich command-line YouTube to MP3 downloader built with Python. This tool provides an enhanced terminal UI, allowing you to preview video details before downloading and track progress with a clean, informative progress bar. It also automatically adds cover art and metadata to your downloaded tracks for a seamless music library experience.

---

## ✨ Features

-   **Enhanced Terminal UI**: Leveraging the `rich` library for a modern, colorful, and clean command-line experience.
-   **Video Preview**: See video details (title, duration, size) before you commit to the download.
-   **Smart Progress Bar**: Track your downloads in real-time with an accurate and aesthetic progress indicator.
-   **Persistent Configuration**: Remembers your preferences to streamline future downloads.
-   **Flexible Audio Quality**: Choose your preferred bitrate: Best (Variable), 320kbps, 192kbps (Default), or 128kbps.
-   **Automatic Cover Art & Metadata**: Automatically embeds thumbnails as album art and fills in ID3 tags (title, artist).
-   **System-Wide Installation**: Easy to set up as a global command for access from any directory.

---

## 🛠️ Installation & Setup

Follow these steps to get **YTmp3** running on your system.

### Step 1: Prerequisites
Ensure you have **Python 3.6+** installed. You also need `yt-dlp` and `ffmpeg` installed on your system.

**Install yt-dlp:**
```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && sudo chmod a+rx /usr/local/bin/yt-dlp
```

**Install ffmpeg:**
- **Ubuntu/Debian:**
  ```bash
  sudo apt install ffmpeg -y
  ```
- **Fedora, CentOS, RHEL:**
  ```bash
  sudo dnf install ffmpeg
  ```
- **Arch Linux:**
  ```bash
  sudo pacman -S ffmpeg
  ```
- **macOS (via Homebrew):**
  ```bash
  brew install ffmpeg
  ```

### Step 2: Clone the Repository
```bash
git clone https://github.com/iiiggoo/YTmp3.git && cd YTmp3
```

### Step 3: Virtual Environment & Dependencies
It is recommended to use a virtual environment to keep your global Python installation clean.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip3 install -r requirements.txt
```

### Step 4: System-wide Installation for linux users (Optional)
If you want to run `ytmp3` from anywhere in your terminal:

## 1:
First, navigate to your project directory and run this command : 
```bash
nano ytmp3
```
Now change the `PATH` to be compatible with your files placing:

```Python
#!/bin/bash
# This wrapper script activates the virtual environment and runs the Python script

# Set the path to your project's virtual environment(change the PATH based on your placing)
VENV_PATH="/home/your_username/Projects/YTmp3/venv/bin/activate"

# Set the path to your actual Python script(change the PATH based on your placing)
SCRIPT_PATH="/home/your_username/Projects/YTmp3/ytmp3.py"

# Check if the virtual environment exists(don't modify it)
if [ ! -f "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH"
    exit 1
fi

# Check if the Python script exists(don't modify it)
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $SCRIPT_PATH"
    exit 1
fi

# Activate the virtual environment and run the script(don't modify it)
source "$VENV_PATH"
python3 "$SCRIPT_PATH" "$@"
```
## 2:

Move the `ytmp3` file to the bin folder in your system:

```bash
# make the file executable
chmod +x ytmp3
# move it to the bin folder
sudo mv ytmp3 /usr/local/bin/ytmp3
```

---

## 🚀 Usage

Once installed, you can launch the downloader by simply typing:

```bash
ytmp3
```
*Alternatively, if you didn't perform the system-wide install:*
```bash
python ytmp3.py
```

> [!IMPORTANT]
> **Note:** Currently, YTmp3 is designed for **single video URLs only**. Support for playlists is not available at this time , make sure its one video **URL** not a palylist **URL**.

---

## ⚠️ Notes & Troubleshooting

-   **Update yt-dlp**: YouTube frequently updates its platform, which can break downloaders. If you encounter issues, update your system's `yt-dlp` first:
    ```bash
    yt-dlp -U
    ```
-   **FFmpeg Path**: Ensure `ffmpeg` is in your system's PATH. You can check this by running `ffmpeg -version` in your terminal. If the command isn't found, re-run the installation steps in Step 1.
-   **Metadata**: Metadata extraction depends on the information provided by the YouTube uploader.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
*Built with ❤️ using Python and the [Rich](https://github.com/Textualize/rich) library.*