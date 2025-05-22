# 🐍 WebSnake

**WebSnake** is a lightweight, browser-based Snake game made with vanilla HTML, CSS, and JavaScript — containerized using Docker for quick and easy deployment anywhere.

---

## 🎮 Live Demo

> Play locally: [http://localhost:8080](http://localhost:8080)

---

## 🚀 Features

- Classic Snake gameplay
- "Easy" and "Hard" mode toggle
- Dynamic speed increase in Hard mode
- Clean retro-style design
- Pure JS, no frameworks
- Fully dockerized (with Flask)

---

## 📦 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/LattenseppCH/WebSnake.git

cd WebSnake
cd WebSnakeFlask

docker build -t websnake .
docker run -d -p 8080:8080 websnake