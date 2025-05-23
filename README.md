
![Logo](https://github.com/LattenseppCH/WebSnake/blob/main/WebSnakeFlask/static/websnake_full.png)



**WebSnake** is a lightweight, browser-based Snake game made with vanilla HTML, CSS, and JavaScript — containerized using Docker for quick and easy deployment anywhere.


## Features

- Classic Snake gameplay
- "Easy" and "Hard" mode toggle
- Dynamic speed increase in Hard mode
- Clean retro-style design
- Pure JS, no frameworks
- Fully dockerized (with Flask)

## Installation

Install WebSnake using this repository

```bash
  git clone https://github.com/LattenseppCH/WebSnake.git

  cd WebSnake

  docker compose up --build
```
    

## Tech Stack

| Component         | Technology                                     |
|------------------|------------------------------------------------|
| Containerization | Docker, Docker Compose                         |
| Reverse Proxy     | NGINX (handles routing & auth cookie checks)   |
| Authentication    | Flask (Python), SQLite (token-based login)     |
| Game Server       | Flask (Python), HTML5, CSS3, JavaScript (Canvas) |
| Database          | SQLite (file-based, embedded in container)     |


## Authors

- [@Rahim Pacolli](https://github.com/LattenseppCH)
- [@Julian Eberle](https://github.com/Julian9496)