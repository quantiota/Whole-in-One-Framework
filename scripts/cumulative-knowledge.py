import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches

# Set seaborn style for better visualization
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Parameters
inflection_year = 1950
center_year = 2075
start_year = 1
end_year = 3000

# Generate data
years = np.linspace(start_year, end_year, 1000)
scaled_years = (years - center_year) / 125
y = sigmoid(scaled_years)

# Create figure with specific dimensions and DPI for better quality
plt.figure(figsize=(15, 10), dpi=100)

# Plot the main sigmoid curve with enhanced styling
plt.plot(years, y, label='Sigmoid Curve', color=sns.color_palette()[0], linewidth=3)

# Create era regions with more subtle colors
alpha_value = 0.2
plt.axvspan(start_year, 1440, color=sns.color_palette()[1], alpha=alpha_value, label='Pre-Print Era')
plt.axvspan(1440, 2025, color=sns.color_palette()[2], alpha=alpha_value, label='Print to Digital Era')
plt.axvspan(2025, end_year, color=sns.color_palette()[3], alpha=alpha_value, label='AI Era')

# Add transition lines with improved styling
transition_style = {'color': sns.color_palette("deep")[7], 'linestyle': '--', 'alpha': 0.5, 'linewidth': 1.5}
plt.axvline(1440, **transition_style)
plt.axvline(2025, **transition_style)

# Enhanced annotations with better positioning and styling
annotation_style = {
    'fontsize': 11,
    'bbox': dict(facecolor='white', edgecolor='none', alpha=0.7, pad=3),
    'ha': 'center'
}

plt.text(700, 0.15, 'Limited recorded knowledge\nDecisions based largely on\ntradition and experience', 
         **annotation_style)
plt.text(1700, 0.5, 'Exponential growth in knowledge\nSystematic documentation\nScientific method', 
         **annotation_style)
plt.text(2500, 0.85, 'AI-augmented knowledge\nData-driven decision making\nIncreased predictive capability', 
         **annotation_style)

# Add key event annotations with curved arrows
arrow_style = dict(
    arrowstyle='->',
    connectionstyle='arc3,rad=0.2',
    color=sns.color_palette("deep")[7],
    linewidth=2
)

plt.annotate('Printing Press (1440)\nDemocratization of Knowledge.\nHoly Bible', 
             xy=(1440, sigmoid((1440 - center_year) / 125)),
             xytext=(1200, 0.7),
             arrowprops=arrow_style,
             **annotation_style)

plt.annotate('Rise of AI (2025)\nTransformative Computing', 
             xy=(2025, sigmoid((2025 - center_year) / 125)),
             xytext=(2200, 0.3),
             arrowprops=arrow_style,
             **annotation_style)

# Enhance axes and labels
plt.xlabel('Year', fontsize=14)
plt.ylabel('Probabilistic Decision Value', fontsize=14)
plt.title('The Relationship Between Knowledge and Probabilistic Decision\nThrough Major Technological Transitions', 
          fontsize=16, pad=20)

# Customize legend
plt.legend(loc='upper left', framealpha=0.9, fontsize=12)

# Adjust layout to prevent text cutoff
plt.tight_layout()

# Save with high DPI for better quality
plt.savefig("knowledge_evolution_timeline.png", dpi=300, bbox_inches='tight', transparent=False)
plt.show()
