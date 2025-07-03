import numpy as np
from flappy import FlappyBirdEnv
from neural_net import CustomFlappyNet
import copy
import random

POP_SIZE = 100
N_GENERATIONS = 100
MUTATION_RATE = 0.2
TOP_K = 10  # number of elites

def evaluate_fitness(agent):
    env = FlappyBirdEnv(render=False)
    state = env.reset()
    total_reward = 0
    steps = 0

    done = False
    while not done:
        x = np.array(state).reshape(1, -1)
        output = agent.forward(x)
        action = np.argmax(output)
        state, reward, done = env.step(action)
        total_reward += reward
        steps += 1

        if steps > 1000:  # safety timeout
            break

    return total_reward

def mutate_weights(weights, rate=MUTATION_RATE):
    new_weights = {}
    for key in weights:
        noise = np.random.randn(*weights[key].shape) * rate
        new_weights[key] = weights[key] + noise
    return new_weights

def evolve_population(population, fitnesses):
    # Sort by fitness descending
    sorted_indices = np.argsort(fitnesses)[::-1]
    new_population = []

    # Keep elites
    for i in range(TOP_K):
        elite = copy.deepcopy(population[sorted_indices[i]])
        new_population.append(elite)

    # Fill rest with mutated children of elites
    while len(new_population) < POP_SIZE:
        parent = random.choice(new_population[:TOP_K])
        child = CustomFlappyNet()
        mutated = mutate_weights(parent.get_weights())
        child.set_weights(mutated)
        new_population.append(child)

    return new_population

def main():
    population = [CustomFlappyNet() for _ in range(POP_SIZE)]

    for gen in range(N_GENERATIONS):
        print(f"\nGeneration {gen+1}")

        fitnesses = [evaluate_fitness(agent) for agent in population]
        best_score = max(fitnesses)
        avg_score = np.mean(fitnesses)

        print(f"Best score: {best_score:.2f} | Avg score: {avg_score:.2f}")

        population = evolve_population(population, fitnesses)

    # Save best agent
    best_idx = np.argmax(fitnesses)
    best_agent = population[best_idx]
    # np.savez("Saved/best_flappy_weights.npz", **best_agent.get_weights())

    print("\nTraining finished! Best agent saved to best_flappy_weights.npz")

if __name__ == "__main__":
    main()