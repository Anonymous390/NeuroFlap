![GitHub release (latest by date)](https://img.shields.io/github/v/release/Anonymous390/NNFS-MNIST-with-Convolution)
![License](https://img.shields.io/badge/License-GPLv3-blue.svg)  
# 🧠 NeuroFlap  
An AI-powered Flappy Bird built **from scratch** in Python with Pygame and a custom neural network, trained using an evolutionary algorithm.  

---

## 🚀 Overview  

**NeuroFlap** simulates a Flappy Bird game where the bird is controlled by a simple neural network. The network evolves over generations using a genetic algorithm to maximize its survival time.  

- Written in **pure Python**, no machine learning libraries used.  
- Evolutionary training — no gradient descent, no backpropagation.  
- Real-time rendering with Pygame.  

---

## 🎮 Features  

✅ Flappy Bird environment (Pygame)  
✅ Custom neural net (fully connected layers + softmax)  
✅ Evolutionary strategy: selection + mutation  
✅ Save and load best model  
✅ Replay saved agents  

---

## 📝 How it works  

1️⃣ **evolve.py** — Runs the genetic algorithm to evolve neural networks.  
2️⃣ **main.py** — Runs a trained agent in the game environment.  
3️⃣ **best_model.py** — Loads and plays the best saved model.  

---

## 📂 Project structure  

```
NeuroFlap/
├── Saved/
│   └── best_flappy_weights.npz   # Saved neural network weights
├── best_model.py                 # Run the best saved agent
├── custom_nn.py                  # Neural net building blocks
├── evolve.py                     # Evolutionary training loop
├── flappy.py                     # Game environment
├── main.py                        # Run a single agent (live)
├── neural_net.py                  # Neural network class for Flappy
├── requirements.txt               # Dependencies
├── .gitignore
└── README.md                      # Project description
```

---

## ⚡ Getting started  

### Requirements  
- Python 3.x  
- Pygame  

### Install dependencies  
```bash
pip install -r requirements.txt
```

### Run training  
```bash
python evolve.py
```

### Run best model  
```bash
python best_model.py
```

---

## 📌 License  

This project is licensed under the **GNU General Public License v3.0**.  
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) for details.  

---
