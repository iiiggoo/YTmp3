# YTmp3 – YouTube MP3 Downloader (Terminal)

A terminal-based Python application to download YouTube videos as MP3 audio files, with:

- Colored progress bars (`rich`)
- Embedded cover art and metadata (`mutagen`)
- Configurable download folder
- Audio quality selection (Best / 320 kbps / 192 kbps / 128 kbps)
- System-wide installation for easy usage
---

## Features

- **First-run setup:** choose your download folder, saved for future runs
- **Audio quality selection:** choose preferred bitrate
- **Real-time progress bars:** colored download and conversion progress
- **Metadata & cover art:** embeds video thumbnail as MP3 cover
- **System-wide usage:** run anywhere by typing `ytmp3`
---

## Requirements

### Python Packages

Install via pip:

pip install -r requirements.txt

requirements.txt includes:

rich    # for terminal progress bars
mutagen # for MP3 metadata & cover art embedding

### System Dependencies

yt-dlp – YouTube downloader backend
ffmpeg – audio extraction and conversion

Install on Ubuntu:

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
sudo apt install ffmpeg
---

## Installation & Setup

1. Clone the repository:

git clone https://github.com/iiiggoo/YTmp3.git
cd YTmp3

2. Install Python dependencies:

pip install -r requirements.txt

3. Make the script executable:

chmod +x ytmp3.py

4. Optional: Install system-wide to run anywhere:

sudo mv ytmp3.py /usr/local/bin/ytmp3

Now you can run the app from any terminal simply by typing:

ytmp3
---

## Usage

1. Run the app:

ytmp3

2. First-time setup: enter the full path to your preferred download folder.  
3. Enter a YouTube URL to download audio.  
4. Select audio quality: Best, 320 kbps, 192 kbps (default), or 128 kbps.  
5. Watch the real-time progress bar as the audio downloads and converts.  
6. MP3 saved in your chosen folder with embedded cover art and metadata.
---

## Notes

- Ensure yt-dlp and ffmpeg are installed and in your system PATH.  
- This app currently supports single videos only.  
- To update yt-dlp for YouTube compatibility:

yt-dlp -U
---

## Contribution

Contributions are welcome. Submit issues or pull requests on GitHub.
---

## Contribution

Contributions are welcome. Submit issues or pull requests on GitHub.
---

## License

This project is licensed under the MIT License.
