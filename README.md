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

- rich – for terminal progress bars
- mutagen – for MP3 metadata & cover art embedding

### System Dependencies

- yt-dlp – YouTube downloader backend
- ffmpeg – audio extraction and conversion

Install on Ubuntu:

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
sudo apt install ffmpeg
