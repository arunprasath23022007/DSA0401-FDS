
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Age and body fat data
age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 58, 60, 61]

fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
       34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

df = pd.DataFrame({"Age": age, "Body Fat": fat})

# Statistical calculations
print("Mean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

# Boxplot
df.boxplot()
plt.title("Boxplot of Age and Body Fat")
plt.show()

# Scatter plot
plt.scatter(age, fat)
plt.xlabel("Age")
plt.ylabel("Body Fat")
plt.title("Age vs Body Fat")
plt.show()

# Q-Q plot using normal scores
def qq_plot(data, title):
    values = sorted(data)
    n = len(values)
    scores = [statistics.NormalDist().inv_cdf((i - 0.5) / n)
              for i in range(1, n + 1)]

    plt.scatter(scores, values)
    plt.xlabel("Theoretical Normal Values")
    plt.ylabel("Observed Values")
    plt.title(title)
    plt.show()

qq_plot(age, "Q-Q Plot of Age")
qq_plot(fat, "Q-Q Plot of Body Fat")

