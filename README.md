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

```bash
pip install -r requirements.txt
requirements.txt includes:

rich – for terminal progress bars

mutagen – for MP3 metadata & cover art embedding

System Dependencies
yt-dlp – YouTube downloader backend

ffmpeg – audio extraction and conversion

Install on Ubuntu:

bash
Copy code
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
sudo apt install ffmpeg
Installation & Setup
Clone the repository:

bash
Copy code
git clone https://github.com/iiiggoo/YTmp3.git
cd YTmp3
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Make the script executable:

bash
Copy code
chmod +x ytmp3.py
Optional: Install system-wide to run anywhere:

bash
Copy code
sudo mv ytmp3.py /usr/local/bin/ytmp3
Now you can run the app from any terminal simply by typing:

bash
Copy code
ytmp3
Usage
Run the app:

bash
Copy code
ytmp3
First-time setup: enter the full path to your preferred download folder.

Enter a YouTube URL to download audio.

Select audio quality: Best, 320 kbps, 192 kbps (default), or 128 kbps.

Watch the real-time progress bar as the audio downloads and converts.

MP3 saved in your chosen folder with embedded cover art and metadata.

Notes
Ensure yt-dlp and ffmpeg are installed and in your system PATH.

This app currently supports single videos only.

To update yt-dlp for YouTube compatibility:

bash
Copy code
yt-dlp -U
Contribution
Contributions are welcome. Submit issues or pull requests on GitHub.

License
This project is licensed under the MIT License.
