# Video Toolkit

This web application provides a set of tools for working with video files, including conversion, downloading, and playback.

## Features

- **Video Conversion:** Upload your video files and convert them to various formats (e.g., MP4, AVI, MOV).
- **Video Downloading:** Download videos directly from URLs.
- **Video Playback:** Play your uploaded videos in the browser.

## Setup and Usage

### Prerequisites

- Python 3.x
- Flask
- ffmpeg
- yt-dlp

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install ffmpeg:**
    Follow the instructions for your operating system:
    - **Linux (Ubuntu/Debian):**
      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```
    - **macOS (using Homebrew):**
      ```bash
      brew install ffmpeg
      ```
    - **Windows:**
      Download the ffmpeg binaries from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add the `bin` directory to your system's PATH.

4.  **Install yt-dlp:**
    ```bash
    pip install yt-dlp
    ```
    Alternatively, follow the installation instructions on the [yt-dlp GitHub page](https://github.com/yt-dlp/yt-dlp#installation).


### Running the Application

1.  **Start the Flask development server:**
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000/`.

## How to Use

-   **Convert Video:**
    1.  Navigate to the "Convert" page.
    2.  Click "Choose File" to select the video you want to convert.
    3.  Select the desired output format from the dropdown menu.
    4.  Click "Convert". The converted file will be downloaded automatically.

-   **Download Video:**
    1.  Navigate to the "Download" page.
    2.  Paste the URL of the video you want to download into the input field.
    3.  Click "Download". The video will be downloaded to your machine.
        *Note: Some videos may not be downloadable due to restrictions (e.g., requiring login).*

-   **Play Video:**
    1.  Navigate to the "Player" page.
    2.  Click "Choose File" to select the video you want to play.
    3.  Click "Upload". The video will load in the player.

## File Management

The application automatically cleans up files older than 6 hours from the `uploads` and `converted` directories to save server space.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
