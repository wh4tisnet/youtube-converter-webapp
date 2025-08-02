# 🎵 YouTube to MP3/MP4 Converter

Easily convert YouTube videos into MP3 (audio) or MP4 (video) files with customizable quality settings. This project features a modern web interface powered by a Flask backend using `yt-dlp` for downloading.

## 🚀 Features

- ✅ Convert YouTube videos to MP3 (audio only)  
- ✅ Convert YouTube videos to MP4 (video)  
- ✅ Choose video quality: 1080p, 720p, 480p, 240p  
- ✅ Responsive and user-friendly interface  
- ✅ Direct download from the browser  
- ✅ Flask backend with `yt-dlp` integration  
- ✅ CORS enabled for local development  

## 🖥️ Preview

Here’s a walkthrough of the interface and functionality:

### 🔗 Paste YouTube URL
This is the main interface where users paste the YouTube video URL they want to convert.  
<p align="center">
  <img width="631" height="484" alt="Paste URL" src="https://github.com/user-attachments/assets/1bafbae0-2611-488d-92f3-6e1804fe992c" />
</p>

### ⚙️ Backend Running
Shows the Flask API running locally on port 5000, confirming the backend is active.  
<p align="center">
  <img width="1101" height="271" alt="Backend Running" src="https://github.com/user-attachments/assets/cadc1f43-1db3-4337-a423-1847c2126621" />
</p>

### 🎧 MP3 Conversion
After pasting the URL and selecting MP3, the download process begins.  
<p align="center">
  <img width="594" height="458" alt="MP3 Download" src="https://github.com/user-attachments/assets/bc24b22d-979c-4cf6-a6dc-ed7b5df4267e" />
</p>

### ✅ MP3 Success
Confirmation that the MP3 conversion and download worked successfully.  
<p align="center">
  <img width="1072" height="510" alt="MP3 Success" src="https://github.com/user-attachments/assets/f72669dd-bb84-418b-9f63-47321c661bc0" />
</p>

### 🎥 MP4 Quality Selection
When choosing MP4, users can select the desired video quality.  
<p align="center">
  <img width="539" height="480" alt="MP4 Quality" src="https://github.com/user-attachments/assets/d5668053-d798-4c43-ae1e-4c126b32bef9" />
</p>

### 📥 MP4 Download
Clicking the download button initiates the MP4 conversion.  
<p align="center">
  <img width="627" height="604" alt="MP4 Download" src="https://github.com/user-attachments/assets/8afe78d7-1d77-44e3-804e-0ade117006c5" />
</p>

### ✅ MP4 Success
Confirmation that the MP4 file was downloaded successfully.  
<p align="center">
  <img width="569" height="518" alt="MP4 Success" src="https://github.com/user-attachments/assets/07100a0e-9c7d-4599-ae9b-3680ce2e189b" />
</p>

### 📂 Files Downloaded
Shows that both MP3 and MP4 files were saved correctly.  
<p align="center">
  <img width="690" height="74" alt="Files Downloaded" src="https://github.com/user-attachments/assets/9d293538-2c3e-4819-9b2c-1d02b43e1394" />
</p>

### 🎬 MP4 Playback
Preview of the downloaded MP4 file being played.  
<p align="center">
  <img width="1190" height="929" alt="MP4 Playback" src="https://github.com/user-attachments/assets/6d7c0c8e-b995-4192-b178-aa4db7aed1bb" />
</p>

### 🎵 MP3 Playback
Preview of the downloaded MP3 file being played.  
<p align="center">
  <img width="1200" height="922" alt="MP3 Playback" src="https://github.com/user-attachments/assets/c08cd10d-5dfc-4e6a-9f07-8134fb2d5b85" />
</p>

---

## 📦 Requirements

- Python 3.7 or higher  
- Node.js (optional, for frontend tooling)  
- A modern web browser  

## 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-converter.git
   cd youtube-converter
   ```

2. **Install Python dependencies:**

   ```bash
   pip install flask flask-cors yt-dlp
   ```

3. **Run the Flask server:**

   ```bash
   python app.py
   ```

4. **Open `index.html` in your browser.**

   > Make sure the backend is running at `http://localhost:5000`.

## 📁 Project Structure

```
youtube-converter/
├── downloads/           # Downloaded files
├── flask_api.py               # Flask backend
├── youtube_downloader.html    # Web interface
└── README.md            # This file
```
