
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
  cd WebSnakeFlask

  docker build -t websnake .
```
    
## Run Locally

First, run the installation as described above. Afterwards, use the following command to start the container.


```bash
  docker run -d -p 8080:8080 websnake
```


## Tech Stack


**Container:** Flask (Python), HTML, CSS, JS


## Authors

- [@Rahim Pacolli](https://github.com/LattenseppCH)
- [@Julian Eberle](https://github.com/Julian9496)