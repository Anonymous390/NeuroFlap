from flappy import FlappyBirdEnv
from neural_net import CustomFlappyNet
import numpy as np

env = FlappyBirdEnv(render=True)
net = CustomFlappyNet()

# Load saved weights
data = np.load("Saved/best_flappy_weights.npz")
weights = {key: data[key] for key in data.files}
net.set_weights(weights)

state = env.reset()
done = False

while not done:
    x = np.array(state).reshape(1, -1)
    output = net.forward(x)
    action = np.argmax(output)
    state, reward, done = env.step(action)
    env.render()
