![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-%E2%9C%94-lightgrey)
![License](https://img.shields.io/badge/License-GPLv3-blue.svg) 
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Anonymous390/NeuroFlap)](https://github.com/Anonymous390/NeuroFlap/releases/latest)
# 🧠 NeuroFlap  
An AI-powered Flappy Bird built **from scratch** in Python with Pygame and a custom neural network, trained using an evolutionary algorithm.  

---

## 🚀 Overview  

NeuroFlap simulates Flappy Bird gameplay where a bird learns to navigate pipes using a simple neural network evolved over generations.  

✨ **Highlights:**  
- Pure Python — no external ML libraries.  
- Neural net evolves through genetic algorithms (no gradient descent, no backprop).  
- Real-time rendering with Pygame.  
- Includes manual play mode (you can play too!).  

---

## 🎮 Features  

✅ Flappy Bird game (Pygame engine)  
✅ Custom neural network (fully connected layers + softmax)  
✅ Genetic algorithm: selection + mutation  
✅ Save/load best performing model  
✅ User mode to play yourself  
✅ Classic style score display (number sprites)  
✅ Game over + restart functionality   

---

## 📝 How it works  

- **`main.py`** → Lets **you play Flappy Bird manually** (spacebar to flap).  
- **`evolve.py`** → Runs the evolutionary training to evolve the AI.  
- **`best_model.py`** → Loads and runs the best saved AI agent automatically.  

---

## 📂 Project structure  

```
NeuroFlap/
├── Saved/
│   └── best_flappy_weights.npz   # Saved AI model weights
├── best_model.py                 # Run the best trained agent
├── custom_nn.py                  # Neural network building blocks
├── evolve.py                     # Evolutionary training loop
├── flappy.py                     # Flappy Bird game environment
├── main.py                       # User play mode (manual play)
├── neural_net.py                  # Neural network wrapper for Flappy
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md                      # Project documentation
```

---

## ⚡ Getting started  

### Requirements  
- Python 3.7+  
- Pygame  
- NumPy  

### Install dependencies  
```bash
pip install -r requirements.txt
```

---

## 🕹️ Running  

### Play manually  
```bash
python main.py
```

### Train AI using genetic algorithm  
```bash
python evolve.py
```

### Watch trained AI play  
```bash
python best_model.py
```

---

## 📌 License  

Licensed under the **GNU General Public License v3.0**.  
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html).   

---
<<<<<<< HEAD
=======

## 🤝 Contributions  

PRs and suggestions welcome — feel free to fork and improve NeuroFlap!
>>>>>>> bd0f5bc (Added assets and a Player mode)
