
![Logo](https://github.com/LattenseppCH/WebSnake/blob/main/game/static/icons/websnake_full.png)


# 🐍 WebSnake

**WebSnake** is a lightweight, browser-based Snake game built with vanilla HTML, CSS, and JavaScript.  
It’s fully containerized using Docker Compose, featuring separate services for authentication, gameplay, and reverse proxy – allowing quick and secure deployment anywhere.



## ✨ Features

- Classic Snake gameplay built with pure JavaScript and HTML5 Canvas
- Difficulty toggle: "Easy" and "Hard" mode
- Dynamic speed increase in Hard mode
- Clean, retro-inspired UI
- Flask-based Auth and Game servers
- Fully dockerized using Docker Compose
- NGINX reverse proxy handles routing and access control
- Lightweight and portable (no external database required)

## 💻 Installation

Install WebSnake using this repository

```bash
  git clone https://github.com/LattenseppCH/WebSnake.git

  cd WebSnake

  docker compose up --build
```
    

## 🤖 Tech Stack

| Component         | Technology                                     |
|------------------|------------------------------------------------|
| Containerization | Docker, Docker Compose                         |
| Reverse Proxy     | NGINX (handles routing & auth cookie checks)   |
| Authentication    | Flask (Python), SQLite (token-based login)     |
| Game Server       | Flask (Python), HTML5, CSS3, JavaScript (Canvas) |
| Database          | SQLite (file-based, embedded in container)     |


## 📖 Authors

- [@Rahim Pacolli](https://github.com/LattenseppCH)
- [@Julian Eberle](https://github.com/Julian9496)


## 🔎 Sources

- [Emoji](https://emojipedia.org/)
- [Logo](https://chatgpt.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [README](https://readme.so)
- [NGINX Config](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)