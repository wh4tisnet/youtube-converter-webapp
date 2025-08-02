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

Here are some screenshots of the interface:

<img width="631" height="484" alt="image" src="https://github.com/user-attachments/assets/1bafbae0-2611-488d-92f3-6e1804fe992c" />
<img width="1101" height="271" alt="image" src="https://github.com/user-attachments/assets/cadc1f43-1db3-4337-a423-1847c2126621" />

<img width="594" height="458" alt="image" src="https://github.com/user-attachments/assets/bc24b22d-979c-4cf6-a6dc-ed7b5df4267e" />
<img width="1072" height="510" alt="image" src="https://github.com/user-attachments/assets/f72669dd-bb84-418b-9f63-47321c661bc0" />
<img width="539" height="480" alt="image" src="https://github.com/user-attachments/assets/d5668053-d798-4c43-ae1e-4c126b32bef9" />
<img width="627" height="604" alt="image" src="https://github.com/user-attachments/assets/8afe78d7-1d77-44e3-804e-0ade117006c5" />
<img width="569" height="518" alt="image" src="https://github.com/user-attachments/assets/07100a0e-9c7d-4599-ae9b-3680ce2e189b" />
<img width="1004" height="357" alt="image" src="https://github.com/user-attachments/assets/7d5fa4c7-8f9a-410d-822a-f0fce6d61cce" />
<img width="573" height="538" alt="image" src="https://github.com/user-attachments/assets/d270cc3f-aa2d-4a22-a79a-82cf8a54d841" />

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
├── app.py               # Flask backend
├── index.html           # Web interface
└── README.md            # This file
```
