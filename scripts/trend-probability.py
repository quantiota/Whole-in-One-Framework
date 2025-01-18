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
        df = pd.DataFrame({'Price': prices})
        ma_short = df['Price'].rolling(window=self.short_window).mean()
        ma_long = df['Price'].rolling(window=self.long_window).mean()
        return ma_short.values, ma_long.values

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-self.sensitivity * x))

    def calculate_trend_probability(self, prices: np.ndarray) -> pd.DataFrame:
        ma_short, ma_long = self.compute_moving_averages(prices)
        df = pd.DataFrame({
            'Price': prices,
            'MA_Short': ma_short,
            'MA_Long': ma_long
        })

        df['Delta_MA'] = df['MA_Short'] - df['MA_Long']
        df['Normalized_Delta'] = df['Delta_MA'] / df['Price']
        df['Trend_Probability'] = self.sigmoid(df['Normalized_Delta'])

        # Apply a single threshold at 0.5
        df['Signal'] = df['Trend_Probability'].apply(lambda x: 'Buy' if x > 0.5 else 'Sell')

        return df

    def plot_results(self, df: pd.DataFrame) -> None:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

        # Price and Moving Averages plot
        ax1.plot(df['Price'], label='Price', alpha=0.7)
        ax1.plot(df['MA_Short'], label=f'{self.short_window}-period MA', linewidth=2)
        ax1.plot(df['MA_Long'], label=f'{self.long_window}-period MA', linewidth=2)
        ax1.set_title('Price with Moving Averages')
        ax1.legend()
        ax1.grid(True)

        # Trend Probability plot
        ax2.plot(df['Trend_Probability'], label='Trend Probability', color='purple')
        ax2.axhline(0.5, color='black', linestyle='--', label='Buy/Sell Threshold')
        ax2.set_title('Trend Probability')
        ax2.set_ylabel('Probability')
        ax2.set_xlabel('Time')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()
        plt.savefig('probability-distribution-claude-thresold1.png', transparent=True)
        plt.show()

# Example usage
if __name__ == "__main__":
    np.random.seed(42)
    time_steps = 200
    price_changes = np.random.normal(0, 1, time_steps)
    price_series = 100 + np.cumsum(price_changes)

    calculator = TrendProbabilityCalculator()
    results = calculator.calculate_trend_probability(price_series)

    calculator.plot_results(results)
