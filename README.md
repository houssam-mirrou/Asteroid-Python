# Asteroids Game

A classic arcade-style Asteroids game built with Python and Pygame. Destroy asteroids, avoid collisions, and survive as long as possible!

## Overview

This is a Python implementation of the iconic Asteroids arcade game. Control your spaceship to destroy incoming asteroids while avoiding collisions. Each asteroid you destroy may split into smaller fragments, increasing the challenge.

## Game Features

- **Classic Gameplay**: Navigate a spaceship through an asteroid field and destroy them with shots
- **Progressive Difficulty**: Asteroids split into smaller pieces when destroyed, creating more obstacles
- **Event Logging**: Game events are logged to `game_events.jsonl` for analysis and debugging
- **State Tracking**: Game state is continuously logged to `game_state.jsonl`
- **Collision Detection**: Full collision detection for player-asteroid and shot-asteroid interactions

## How to Play

### Controls
- **A** - Rotate left
- **D** - Rotate right
- **W / S** - Move forward
- **SPACE** - Shoot

### Objective
- Destroy all asteroids by shooting them
- Avoid colliding with asteroids (game ends on collision)
- Asteroids split into smaller pieces when destroyed
- Survive as long as possible

## Installation

### Requirements
- Python 3.13 or higher
- Pygame 2.6.1

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/houssam-mirrou/Asteroid-Python.git
   cd Asteroid-Python
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```
   Or directly:
   ```bash
   pip install pygame==2.6.1
   ```

## Running the Game

Start the game from the project directory:

```bash
python main.py
```

The game window will open and start spawning asteroids. Close the window or encounter a collision to end the game.

## Project Structure

```
.
├── main.py                  # Main game loop and entry point
├── player.py               # Player spaceship class
├── asteroid.py             # Asteroid class with splitting logic
├── asteroidfield.py        # Asteroid spawning system
├── shot.py                 # Projectile class
├── circleshape.py          # Base class for circular entities
├── constants.py            # Game configuration values
├── logger.py               # Event and state logging system
├── game_events.jsonl       # Logged game events (generated)
├── game_state.jsonl        # Logged game states (generated)
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Configuration

Game settings can be adjusted in [constants.py](constants.py):

- `SCREEN_WIDTH` / `SCREEN_HEIGHT` - Window dimensions (1280x720)
- `PLAYER_RADIUS` - Player spaceship size (20)
- `PLAYER_TURN_SPEED` - Rotation speed (300 degrees/sec)
- `PLAYER_SPEED` - Movement speed (200 pixels/sec)
- `PLAYER_SHOOT_SPEED` - Projectile velocity (500 pixels/sec)
- `PLAYER_SHOOT_COOLDOWN_SECONDS` - Time between shots (0.3s)
- `ASTEROID_MIN_RADIUS` - Minimum asteroid size (20)
- `ASTEROID_MAX_RADIUS` - Maximum asteroid size
- `ASTEROID_SPAWN_RATE_SECONDS` - Spawn frequency (0.8s)

## Logging

The game logs two types of data:

- **game_events.jsonl** - Individual game events (asteroid_split, player_hit, asteroid_shot)
- **game_state.jsonl** - Complete game state snapshots each frame

These files are useful for analysis, debugging, and replay functionality.

## Technical Details

### Architecture

The game uses:
- **Pygame** for graphics and input handling
- **Sprite Groups** for managing game objects
- **Collision Detection** via distance-based collision methods
- **Event Logging** for game analytics

### Class Hierarchy

- `CircleShape` - Base class for all circular entities
  - `Player` - Player-controlled spaceship
  - `Asteroid` - Destructible asteroids that split on impact
  - `Shot` - Projectiles fired by the player

## Future Enhancements

Possible improvements and features:
- Score tracking and display
- Lives system instead of instant game-over
- Sound effects and music
- Difficulty levels
- High score leaderboard
- Power-ups
- Menu system
- Pause functionality

## License

This project is open source and available on GitHub.

## Credits

Classic Asteroids arcade game concept reimplemented in Python with Pygame.

---

**Play responsibly and have fun!** 🎮
