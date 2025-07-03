from flappy import FlappyBirdEnv
from neural_net import CustomFlappyNet
import numpy as np

env = FlappyBirdEnv(render=True)
net = CustomFlappyNet()

state = env.reset()
done = False

while not done:
    input_state = np.array(state).reshape(1, -1)
    output = net.forward(input_state)
    action = np.argmax(output)

    state, reward, done = env.step(action)
    env.render()