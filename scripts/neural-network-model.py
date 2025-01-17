import numpy as np
import matplotlib.pyplot as plt

# Define sigmoid activation function to simulate decision-making (buy/sell)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Simulate market input factors (e.g., news, trends, emotions)
np.random.seed(42)  # For reproducibility
num_traders = 100
market_inputs = np.random.normal(0, 1, (num_traders, 5))  # 5 input factors for each trader

# Initialize random weights and biases for traders
weights = np.random.normal(0, 1, (num_traders, 5))
biases = np.random.normal(0, 0.5, num_traders)

# Simulate decision-making without divine influence
decisions_without_influence = sigmoid(np.sum(market_inputs * weights, axis=1) + biases)

# Introduce "Divine Influence" by adjusting weights (small positive or negative shift)
divine_influence = np.random.choice([-0.5, 0.5], size=(num_traders, 5))
adjusted_weights = weights + divine_influence

# Simulate decision-making with divine influence
decisions_with_influence = sigmoid(np.sum(market_inputs * adjusted_weights, axis=1) + biases)

# Plot comparison of decision distributions
plt.figure(figsize=(10, 6))
plt.hist(decisions_without_influence, bins=20, alpha=0.8, label="Without Divine Influence", color="#ffcc70")
plt.hist(decisions_with_influence, bins=20, alpha=0.8, label="With Divine Influence", color="#fea37c")
plt.xlabel("Decision Probability (0 = Sell, 1 = Buy)")
plt.ylabel("Number of Traders")
plt.title("Impact of 'Divine Influence' on Trader Decisions")
plt.legend()
plt.grid(True)


# Save the neural network plot to a file
plt.savefig('trader_decisions_with_divine_influence.png')

plt.show()
