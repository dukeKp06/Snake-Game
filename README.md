# 🐍 Modern Snake Game

A professionally crafted Snake game built with Python and Pygame, featuring clean architecture, smooth animations, and modern design patterns.

## ✨ Features

- **Smooth Gameplay**: 60 FPS with fluid snake movement
- **Modern UI**: Clean, minimalist design with visual effects
- **Score System**: Real-time scoring with high score tracking
- **Responsive Controls**: WASD and arrow key support
- **Game States**: Menu, gameplay, pause, and game over screens
- **Sound Effects**: Audio feedback for actions (optional)
- **Clean Architecture**: Modular, maintainable code structure

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## 🎮 How to Play

- Use **WASD** or **Arrow Keys** to control the snake
- Eat food (red squares) to grow and increase your score
- Avoid hitting walls or the snake's own body
- Press **SPACE** to pause/unpause
- Press **ESC** to return to menu

## 🏗️ Project Structure

```
game/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md           # Documentation
├── src/
│   ├── game/           # Core game logic
│   │   ├── __init__.py
│   │   ├── engine.py   # Game engine
│   │   ├── snake.py    # Snake entity
│   │   ├── food.py     # Food entity
│   │   └── config.py   # Game configuration
│   ├── ui/             # User interface
│   │   ├── __init__.py
│   │   ├── renderer.py # Graphics rendering
│   │   ├── screens.py  # Game screens
│   │   └── colors.py   # Color definitions
│   └── utils/          # Utilities
│       ├── __init__.py
│       └── helpers.py  # Helper functions
├── assets/             # Game assets
├── tests/              # Unit tests
└── docs/               # Additional documentation
```

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **Pygame**: Graphics and game development library
- **Object-Oriented Design**: Clean, maintainable architecture
- **Type Hints**: Enhanced code readability and IDE support

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 📈 Performance

- **60 FPS**: Smooth gameplay experience
- **Low Memory Usage**: Efficient resource management
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License

## 👨‍💻 Author

**Pranjil Kapoor**
- LinkedIn: https://www.linkedin.com/in/pranjilkapoor/
- GitHub: https://github.com/dukeKp06

---
*Built with ❤️ using Python and Pygame*
