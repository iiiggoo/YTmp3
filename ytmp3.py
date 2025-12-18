import subprocess
import sys
import shutil
import os
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn
from rich.panel import Panel
import yt_dlp

# Initialization
console = Console()
CONFIG_FILE = Path.home() / ".mp3_downloader_config"

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_dependencies():
    """Ensure all required command-line tools and Python libraries are installed."""
    console.print("[cyan]Checking for dependencies...[/cyan]")
    # Check for command-line tools
    for tool in ("yt-dlp", "ffmpeg"):
        if not shutil.which(tool):
            console.print(f"[bold red]Error:[/bold red] '{tool}' is not installed or not in your system's PATH.")
            console.print(f"Please install it using your system's package manager (e.g., 'sudo apt install {tool}').")
            sys.exit(1)
    
    # Check for Python libraries
    required_libs = {"yt_dlp": "yt-dlp", "rich": "rich", "mutagen": "mutagen"}
    for lib_name, pip_name in required_libs.items():
        try:
            __import__(lib_name)
        except ImportError:
            console.print(f"[bold red]Error:[/bold red] The Python library '{lib_name}' is not installed.")
            console.print(f"Please install it by running: [bold]pip install {pip_name}[/bold]")
            sys.exit(1)
    console.print("[green]✔ All dependencies found.[/green]")

def format_bytes(bytes):
    """Formats a number of bytes into a human-readable string (KB, MB, GB)."""
    if bytes is None:
        return "N/A"
    power = 1024
    n = 0
    power_labels = {0: '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while bytes >= power and n < len(power_labels):
        bytes /= power
        n += 1
    return f"{bytes:.2f} {power_labels[n]}"

def get_download_folder():
    """Ask user for download folder on first run, store in config."""
    if CONFIG_FILE.exists():
        try:
            folder = Path(CONFIG_FILE.read_text().strip())
            if folder.is_dir():
                return folder
        except (IOError, OSError):
            console.print(f"[yellow]Warning: Could not read config file at {CONFIG_FILE}.[/yellow]")

    console.print(Panel.fit("[bold cyan]Welcome![/bold cyan]\nLet's set up your download folder.", border_style="cyan"))
    while True:
        folder_str = console.input("\nEnter the full path to the download folder: ").strip()
        folder = Path(folder_str).expanduser()
        if not folder_str:
            console.print("[red]No path entered. Please try again.[/red]")
            continue
        
        try:
            folder.mkdir(parents=True, exist_ok=True)
            CONFIG_FILE.write_text(str(folder))
            console.print(f"[green]✔ Download folder set to: {folder}[/green]")
            return folder
        except OSError as e:
            console.print(f"[red]Error creating directory '{folder}': {e}[/red]")

def get_video_info_and_confirm(url):
    """Fetches video info (title, duration, size) and asks for confirmation."""
    console.print(f"\n[cyan]Fetching video info...[/cyan]")
    ydl_opts = {'quiet': True, 'no_warnings': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'N/A')
            duration = info_dict.get('duration', 0)
            filesize = info_dict.get('filesize_approx') # Use approximate size for better reliability

            # Format duration
            if duration:
                minutes, seconds = divmod(duration, 60)
                duration_str = f"{minutes}:{seconds:02d}"
            else:
                duration_str = "N/A"
            
            # Format file size
            size_str = format_bytes(filesize)

            # --- Display UI ---
            text_content = f"[bold yellow]Title:[/bold yellow] {title}\n"
            text_content += f"[bold yellow]Duration:[/bold yellow] {duration_str}\n"
            text_content += f"[bold yellow]Size:[/bold yellow] {size_str}\n"
            text_content += f"[bold yellow]URL:[/bold yellow] {url}"
            
            console.print(Panel.fit(text_content, title="Video Details", border_style="blue"))

            choice = console.input("\nIs this the correct video? [Y/n]: ").strip().lower()
            return choice in ['', 'y', 'yes']

    except yt_dlp.utils.DownloadError:
        console.print(Panel.fit("[bold red]Error:[/bold red] Could not fetch video info. The URL may be invalid or the video is private.", border_style="red"))
        return False

def choose_quality():
    """Prompts the user to select an audio quality."""
    console.print("\n[bold]Select audio quality:[/bold]")
    options = {
        "1": ("Best available", "0"),
        "2": ("320 kbps", "320K"),
        "3": ("192 kbps (default)", "192K"),
        "4": ("128 kbps", "128K")
    }
    for key, (desc, _) in options.items():
        console.print(f"  [cyan]{key}[/cyan]) {desc}")

    while True:
        choice = console.input("\nChoice [1-4]: ").strip()
        if choice in options:
            return options[choice][1]
        console.print("[red]Invalid choice. Please enter a number between 1 and 4.[/red]")

def download_audio(url, quality, folder):
    """Downloads YouTube video as MP3 with a clear, two-stage progress indicator."""
    output_template = str(folder / "%(title)s.%(ext)s")
    progress_bar = None
    task_id = None

    def my_hook(d):
        nonlocal progress_bar, task_id
        if d['status'] == 'downloading':
            if progress_bar.tasks[task_id].total is None and d.get('total_bytes') is not None:
                progress_bar.update(task_id, total=d.get('total_bytes'))
            if d.get('downloaded_bytes') is not None:
                progress_bar.update(task_id, completed=d.get('downloaded_bytes'))
        elif d['status'] == 'finished':
            total_bytes = d.get('total_bytes', 0)
            progress_bar.update(task_id, completed=total_bytes, description="[bold yellow]Download finished. Processing file...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': quality}, {'key': 'EmbedThumbnail'}, {'key': 'FFmpegMetadata'}],
        'quiet': True, 'no_warnings': True, 'progress_hooks': [my_hook],
    }

    console.print(f"\n[cyan]Starting download for:[/cyan] {url}")
    try:
        with Progress(TextColumn("[bold blue]{task.description}", justify="right"), BarColumn(bar_width=40), DownloadColumn(binary_units=True), console=console, transient=False) as progress:
            task_id = progress.add_task("Downloading...", total=None)
            progress_bar = progress
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            progress.update(task_id, description="[bold green]✔ Complete![/bold green]")
        
        console.print(Panel.fit("[bold green]Success![/bold green]\nFile has been saved to your download folder.", border_style="green"))
        return True
    except yt_dlp.utils.DownloadError as e:
        console.print(Panel.fit(f"[bold red]✖ Download Failed[/bold red]\n\n[red]{e}[/red]", title="Error Details", border_style="red"))
        return False
    except Exception as e:
        console.print(Panel.fit(f"[bold red]An unexpected error occurred:[/bold red]\n{e}", border_style="red"))
        return False

# --- Main Program ---

def main():
    clear_screen()
    check_dependencies()
    folder = get_download_folder()

    while True:
        clear_screen()
        console.print(Panel.fit("[bold yellow]YouTube to MP3 Downloader[/bold yellow]", border_style="yellow"))
        
        url = console.input("\nEnter [bold cyan]YouTube URL[/bold cyan] (or 'q' to quit): ").strip()
        if url.lower() in ['q', 'quit', 'exit']:
            break

        if not url:
            console.print("[bold red]No URL provided. Please try again.[/red]")
            input("Press Enter to continue...")
            continue

        if not get_video_info_and_confirm(url):
            input("Press Enter to try another URL...")
            continue

        quality = choose_quality()
        success = download_audio(url, quality, folder)
        
        while True:
            choice = console.input("\nDo you want to download another file? [Y/n]: ").strip().lower()
            if choice in ['', 'y', 'yes']:
                break
            elif choice in ['n', 'no']:
                console.print("[yellow]Exiting...[/yellow]")
                return
            else:
                console.print("[red]Invalid input. Please enter 'y' or 'n'.[/red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user. Exiting.[/yellow]")
        sys.exit(0)