#!/usr/bin/env python3

import subprocess
import sys
import shutil
import os
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, DownloadColumn

# ----------------- Initialization -----------------
console = Console()
CONFIG_FILE = Path.home() / ".mp3_downloader_config"

# ----------------- Helper Functions -----------------
def clear_screen():
    print("\033c", end="")

def check_dependencies():
    """Ensure yt-dlp, ffmpeg, and mutagen are installed."""
    for tool in ("yt-dlp", "ffmpeg"):
        if not shutil.which(tool):
            console.print(f"[bold red][ERROR][/bold red] {tool} is not installed. Install it first.")
            sys.exit(1)

    try:
        import mutagen
    except ImportError:
        console.print("[bold yellow][INFO][/bold yellow] Installing mutagen for cover art embedding...")
        subprocess.run([sys.executable, "-m", "pip", "install", "mutagen"], check=True)

def get_download_folder():
    """Ask user for download folder on first run, store in config."""
    if CONFIG_FILE.exists():
        folder = Path(CONFIG_FILE.read_text().strip())
        if folder.exists():
            return folder

    console.print("[bold cyan]Welcome![/bold cyan] Let's set up your download folder.")
    folder = Path(input("Enter the full path to the download folder: ").strip()).expanduser()
    folder.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(str(folder))
    return folder

def choose_quality():
    console.print("\nSelect audio quality:")
    console.print("1) Best available")
    console.print("2) 320 kbps")
    console.print("3) 192 kbps (default)")
    console.print("4) 128 kbps")

    choice = input("\nChoice [1-4]: ").strip()
    return {
        "1": "0",
        "2": "320K",
        "3": "192K",
        "4": "128K"
    }.get(choice, "192K")

def download_audio(url, quality, folder):
    """Download YouTube video as MP3 with cover art embedding and rich progress bar."""
    output_template = str(folder / "%(title)s.%(ext)s")
    command = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", quality,
        "--embed-thumbnail",
        "--add-metadata",
        "--progress-template", " {downloaded_bytes}/{total_bytes} ",
        "-o", output_template,
        url
    ]

    console.print("\n[bold green]Starting download...[/bold green]\n")
    # Using rich Progress to show progress dynamically
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        DownloadColumn(),
        TimeElapsedColumn(),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("Downloading...", total=None)
        try:
            subprocess.run(command, check=True)
            progress.update(task, description="[bold green]Download Complete![/bold green]")
            progress.stop()
            console.print(f"[bold green]✔ MP3 saved in {folder}[/bold green]")
        except subprocess.CalledProcessError:
            progress.stop()
            console.print("[bold red]✖ Download failed. Check URL, network, or yt-dlp version.[/bold red]")

# ----------------- Main Program -----------------
def main():
    clear_screen()
    check_dependencies()
    console.print("="*60)
    console.print("[bold yellow]        YouTube MP3 Downloader (Terminal)        [/bold yellow]")
    console.print("="*60)

    folder = get_download_folder()
    url = input("\nEnter YouTube URL: ").strip()
    if not url:
        console.print("[bold red]No URL provided. Exiting.[/bold red]")
        return

    quality = choose_quality()
    download_audio(url, quality, folder)

if __name__ == "__main__":
    main()
