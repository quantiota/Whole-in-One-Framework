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

# Compute the final aggregated decisions
final_decision_without_influence = np.mean(decisions_without_influence)
final_decision_with_influence = np.mean(decisions_with_influence)

# Plot comparison of decision distributions
plt.figure(figsize=(10, 6))
plt.hist(decisions_without_influence, bins=20, alpha=0.8, label="Without Divine Influence", color="#ffcc70")
plt.hist(decisions_with_influence, bins=20, alpha=0.8, label="With Divine Influence", color="#fea37c")
plt.xlabel("Decision Probability (0 = Sell, 1 = Buy)")
plt.ylabel("Number of Traders")
plt.title("Impact of 'Divine Influence' on Trader Decisions")
plt.legend()
plt.grid(True)
plt.savefig('decision_distributions.png')  # Save the first plot
plt.show()

# Plot the final aggregated decisions
plt.figure(figsize=(8, 5))
bars = plt.bar(["Without Divine Influence", "With Divine Influence"],
               [final_decision_without_influence, final_decision_with_influence],
               color=["#ffcc70", "#fea37c"])
plt.ylim(0, 1)
plt.ylabel("Average Decision Probability")
plt.title("Final Aggregated Decision Probability")

# Annotate the bars with the exact probability values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{yval:.2f}", ha='center', va='bottom')

plt.grid(True, axis='y')
plt.savefig('final_aggregated_decision.png')  # Save the second plot
plt.show()