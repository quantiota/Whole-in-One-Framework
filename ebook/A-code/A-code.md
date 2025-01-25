# APPENDIX A: Python Programming Code 

## Neural Network Model

```python
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

```


## Trend Probability

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple

class TrendProbabilityCalculator:
    def __init__(self, short_window: int = 5, long_window: int = 20, sensitivity: float = 5.0):
        self.short_window = short_window
        self.long_window = long_window
        self.sensitivity = sensitivity

    def compute_moving_averages(self, prices: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Compute short and long-term moving averages."""
        df = pd.DataFrame({'Price': prices})
        ma_short = df['Price'].rolling(window=self.short_window).mean()
        ma_long = df['Price'].rolling(window=self.long_window).mean()
        return ma_short.values, ma_long.values

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Apply sigmoid transformation with sensitivity scaling."""
        return 1 / (1 + np.exp(-self.sensitivity * x))

    def calculate_trend_probability(self, prices: np.ndarray) -> pd.DataFrame:
        """Calculate trend probability and assign Buy/Sell signals."""
        ma_short, ma_long = self.compute_moving_averages(prices)
        df = pd.DataFrame({
            'Price': prices,
            'MA_Short': ma_short,
            'MA_Long': ma_long
        })

        # Compute the difference between short and long moving averages
        df['Delta_MA'] = df['MA_Short'] - df['MA_Long']
        df['Normalized_Delta'] = df['Delta_MA'] / df['Price']

        # Apply sigmoid to compute trend probability
        df['Trend_Probability'] = self.sigmoid(df['Normalized_Delta'])

        # Use a single threshold at 0.5 for Buy/Sell decision
        df['Signal'] = df['Trend_Probability'].apply(lambda x: 'Buy' if x > 0.5 else 'Sell')

        return df

    def plot_results(self, df: pd.DataFrame) -> None:
        """Plot price, moving averages, and trend probability with aligned x-axis."""
        # Enable shared x-axis
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

        # Plot Price with Moving Averages
        ax1.plot(df.index, df['Price'], label='Price', alpha=0.7, color='blue')
        ax1.plot(df.index, df['MA_Short'], label=f'{self.short_window}-Period MA', linewidth=2, color='orange')
        ax1.plot(df.index, df['MA_Long'], label=f'{self.long_window}-Period MA', linewidth=2, color='green')
        ax1.set_title('Price with Moving Averages')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(True)

        # Plot Trend Probability with threshold at 0.5
        ax2.plot(df.index, df['Trend_Probability'], label='Trend Probability', color='purple')
        ax2.axhline(0.5, color='black', linestyle='--', label='Buy/Sell Threshold')
        ax2.set_title('Trend Probability Over Time')
        ax2.set_ylabel('Probability')
        ax2.set_xlabel('Time')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()
        plt.savefig('probability-distribution.png')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Generate synthetic price data
    np.random.seed(42)
    time_steps = 200
    price_changes = np.random.normal(0, 1, time_steps)
    price_series = 100 + np.cumsum(price_changes)

    # Initialize the Trend Probability Calculator
    calculator = TrendProbabilityCalculator()

    # Compute trend probability and trading signals
    results = calculator.calculate_trend_probability(price_series)

    # Plot the results with aligned x-axis
    calculator.plot_results(results)

    ```