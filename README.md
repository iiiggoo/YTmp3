# 🎵 YTmp3 - YouTube MP3 Downloader

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A beautiful and feature-rich command-line YouTube to MP3 downloader built with Python. This tool provides an enhanced terminal UI, allowing you to preview video details before downloading and track progress with a clean, informative progress bar. It also automatically adds cover art and metadata to your downloaded tracks.

## ✨ Features

-   **Enhanced Terminal UI:** A clean, modern, and colorful interface built with the `rich` library.
-   **Video Preview:** Before downloading, see the video's **title, duration, and estimated file size** to confirm it's the right one.
-   **Smart Progress Bar:** A real-time progress bar shows the download status, including downloaded data, total size, and percentage. It also indicates when the file is being processed (e.g., converted to MP3).
-   **Persistent Configuration:** The application remembers your download folder, so you only need to set it up once.
-   **Flexible Audio Quality Selection:** Choose from Best, 320kbps, 192kbps (default), or 128kbps to balance quality and file size.
-   **Automatic Cover Art & Metadata Embedding:** Downloads the video thumbnail and embeds it as album art, along with song title and artist metadata.
-   **System-Wide Installation:** Install it once and run the `ytmp3` command from anywhere in your terminal.

---

## 🛠️ Installation & Setup

Follow these steps to get YTmp3 running on your system. These instructions are tailored for Linux/macOS users.

### Step 1: Prerequisites

Before you can run YTmp3, you need to have `Python`, `yt-dlp`, and `ffmpeg` installed on your system.

**A. Python and pip:**
This project is built on Python. You can check if you have it installed by running `python3 --version`. If not, install it from the official Python website.

**B. yt-dlp (The Downloader):**
`yt-dlp` is the engine that fetches the video from YouTube.

# Use these commands in your terminal
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

**C. ffmpeg (The Audio Converter):**
`ffmpeg` is a powerful tool used to convert the video stream into an MP3 audio file.

# For Ubuntu/Debian-based systems
sudo apt update && sudo apt install ffmpeg

# For macOS (using Homebrew)
brew install ffmpeg

### Step 2: Clone the Repository

This command downloads the YTmp3 project files from GitHub to your computer.

# Use this command in your terminal
git clone https://github.com/iiiggoo/YTmp3.git

Now, navigate into the project directory:

# Use this command in your terminal
cd YTmp3

### Step 3: Set Up a Virtual Environment & Install Dependencies

It's highly recommended to use a virtual environment to manage project dependencies. This keeps your project's libraries separate from your system's Python.

# Use these commands in your terminal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Step 4: (Optional) System-Wide Installation

This is a highly recommended step. It allows you to run the app from any directory just by typing `ytmp3`, instead of having to find the script every time.

# Use these commands in your terminal
chmod +x ytmp3.py
sudo mv ytmp3.py /usr/local/bin/ytmp3

---

## 🚀 Usage

Once installed, using YTmp3 is straightforward.

1.  **Run the application.**
    If you performed the optional system-wide installation, you can run it from anywhere with:
    
    # Use this command in your terminal
    ytmp3
    
    If you didn't, you must run it from the project directory with the virtual environment activated:
    
    # Use these commands in your terminal
    cd YTmp3
    source venv/bin/activate
    python ytmp3.py

2.  **First-Time Setup.**
    The very first time you run the app, it will ask you to enter the full path to your preferred download folder (e.g., `/home/user/Music/YoutubeDownloads`). This setting will be saved for future runs.

3.  **Download a Song.**
    - The app will prompt you to `Enter YouTube URL:`. Paste the link to the YouTube video you want to download.
    - **Important:** Please ensure the URL you provide is for a **single video**, not a playlist. This tool is designed to download one video at a time.
    - The application will display the video details (title, duration, size). Confirm if you want to proceed.
    - You will then be asked to select the audio quality. Type your choice and press Enter.

4.  **Enjoy!**
    A colored progress bar will show the download and conversion status. Once finished, you'll find the MP3 file in your configured download folder, complete with cover art and metadata.

---

## ⚠️ Notes & Troubleshooting

-   **Ensure Dependencies are in PATH:** Make sure `yt-dlp` and `ffmpeg` are installed correctly and are in your system's PATH. The installation commands above should handle this for you.
-   **Updating yt-dlp:** YouTube frequently changes its backend. If you encounter download errors, `yt-dlp` might need an update. You can update it by running:
    
    # Use this command in your terminal
    yt-dlp -U
-   **Single Videos Only:** This app is designed to download individual videos. It will not work correctly with playlist URLs.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.