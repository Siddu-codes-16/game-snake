# 🐍 SNAKE // ARCADE EDITION

A retro neon Snake game built with Python (Flask) + HTML5 Canvas — deployable to Vercel in one click.

## Features
- 🎮 Smooth Snake gameplay with increasing difficulty
- 🌟 Neon arcade aesthetic with glowing effects
- 📱 Mobile-friendly with d-pad controls + swipe support
- ⌨️ Keyboard: Arrow keys / WASD · `P` to pause
- 🏆 High score saved in localStorage
- ⚡ Auto-levels up as your score grows

---

## 🚀 Deploy to Vercel

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Snake game"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/snake-game.git
git push -u origin main
```

### 2. Deploy on Vercel
1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New Project"**
3. Import your GitHub repo
4. Vercel auto-detects the config from `vercel.json`
5. Click **Deploy** — done! 🎉

No environment variables needed.

---

## 🛠 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python api/index.py
```

Open http://localhost:5000 in your browser.

---

## 📁 Project Structure

```
snake-game/
├── api/
│   └── index.py        # Flask app (Vercel entry point)
├── templates/
│   └── index.html      # Game UI + canvas logic
├── vercel.json         # Vercel routing config
├── requirements.txt    # Python dependencies
└── README.md
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ ↓ ← → or W A S D | Move snake |
| P | Pause / Resume |
| Mobile | Swipe or use on-screen d-pad |

## Scoring

- Each food = `Level × 10` points
- Every 50 points → level up (snake speeds up)
- Max speed capped at level ~8
