import math
import matplotlib.pyplot as plt

# Define the normal distribution probability density function (pdf)
def normal_pdf(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-(x - mean)**2 / (2 * std_dev**2))

# Define the cumulative distribution function (cdf) for normal distribution
def normal_cdf(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

# Calculate the probabilities
prob_x_less_than_1 = normal_cdf(1, 0, 1)
prob_x_greater_than_mean_plus_2std = 1 - normal_cdf(175 + 2*3, 175, 3)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot N(0, 1) PDF and shade area for x < 1
x_values = [i * 0.1 for i in range(-50, 51)]
pdf_values = [normal_pdf(x, 0, 1) for x in x_values]
plt.plot(x_values, pdf_values, label='N(0, 1) PDF')
plt.fill_between(x_values, pdf_values, where=[x < 1 for x in x_values], color='lightblue', alpha=0.5)
plt.axvline(x=1, color='blue', linestyle='--', label='x=1')
plt.text(-4, 0.3, f'P(x<1) = {prob_x_less_than_1:.4f}', fontsize=12)

# Plot N(175, 3) PDF and shade area for x > μ+2σ
x_values = [i * 0.1 for i in range(1600, 1901)]
pdf_values = [normal_pdf(x, 175, 3) for x in x_values]
plt.plot(x_values, pdf_values, label='N(175, 3) PDF')
plt.fill_between(x_values, pdf_values, where=[x > (175 + 2*3) for x in x_values], color='lightcoral', alpha=0.5)
plt.axvline(x=(175 + 2*3), color='red', linestyle='--', label='x=μ+2σ')
plt.text(180, 0.02, f'P(x>μ+2σ) = {prob_x_greater_than_mean_plus_2std:.4f}', fontsize=12)

plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Probability Density Functions')
plt.legend()
plt.grid(True)
plt.show()

