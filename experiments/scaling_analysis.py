import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

# Data extracted from our experiments
# Tokens (D) and corresponding MLM Losses (L)
data = {
    'Meitei (TB)': {
        'tokens': [109374, 224311, 355368, 488292, 612406],
        'loss': [9.608, 9.384, 8.969, 8.831, 8.822] # log(PPL)
    },
    'Assamese (IA)': {
        'tokens': [163460, 325014, 488658, 653515, 811642],
        'loss': [7.662, 7.788, 7.725, 7.659, 7.743]
    }
}

def fit_scaling_law(tokens, loss):
    # Log-log transformation for power law: log(L) = log(B) - beta * log(D)
    log_d = np.log10(tokens)
    log_l = np.log10(loss)
    slope, intercept, r_value, p_value, std_err = linregress(log_d, log_l)
    return -slope, r_value**2

print("--- Scaling Law Results ---")
for lang, values in data.items():
    beta, r2 = fit_scaling_law(values['tokens'], values['loss'])
    print(f"{lang}: Beta = {beta:.4f}, R^2 = {r2:.4f}")

# Generate Figure 1: Scaling Frontiers
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

for lang, values in data.items():
    plt.plot(np.log10(values['tokens']), np.log10(values['loss']), 'o-', label=lang)

plt.title("Figure 1: Scaling Frontiers in NE Indian Contact Zone")
plt.xlabel("log10(Tokens)")
plt.ylabel("log10(Loss)")
plt.legend()
plt.show()
