# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt





#PART 1: Exercise Dataset

# Load dataset
exercise = pd.read_csv("Exercise_Data.csv")

# Heatmap of pulse data
pulse_data = exercise[['1 min', '15 min', '30 min']]

plt.figure(figsize=(8,6))
sns.heatmap(pulse_data, cmap="coolwarm", annot=True)

plt.title("Heatmap of Pulse Rates Over Time")
plt.xlabel("Time After Exercise")
plt.ylabel("Participant ID")
plt.tight_layout()
plt.show()

pulse_long = exercise.melt(id_vars=['diet','kind'], value_vars=['1 min','15 min','30 min'], var_name="time", value_name="pulse")

# Pulse by Diet
plt.figure(figsize=(8,6))
sns.catplot(data=pulse_long, x="time", y="pulse", hue="diet", kind="bar", height=6, aspect=1.3)

plt.title("Average Pulse by Diet Type")
plt.xlabel("Time After Exercise")
plt.ylabel("Pulse Rate")
plt.show()

# Pulse by Exercise Type
plt.figure(figsize=(8,6))
sns.catplot(data=pulse_long, x="time", y="pulse", hue="kind", kind="bar",height=6, aspect=1.3)

plt.title("Average Pulse by Exercise Type")
plt.xlabel("Time After Exercise")
plt.ylabel("Pulse Rate")
plt.show()

# Explanation: The data shows that when people exercise, their heart rate increases to pump blood throughout the body. Different types of exercise and diets can affect heart rate as well. Those who ran had higher pulse rates than those who walked, and those on the no fat diet had higher pulse rates than those on the low fat diet. 

# PART 2: Planets Dataset
planets = sns.load_dataset("planets")


# RELATIONAL PLOTS (2)


# 1. Distance vs Orbital Period
plt.figure(figsize=(8,6))
sns.scatterplot(data=planets, x="distance", y="orbital_period", hue="method")

plt.title("Distance vs Orbital Period of Planets")
plt.xlabel("Distance from Earth")
plt.ylabel("Orbital Period")
plt.show()


# 2. Mass vs Orbital Period
plt.figure(figsize=(8,6))
sns.lineplot(data=planets, x="mass", y="orbital_period")

plt.title("Planet Mass vs Orbital Period")
plt.xlabel("Planet Mass")
plt.ylabel("Orbital Period")
plt.show()

# DISTRIBUTIONAL PLOTS (2)

# 1. Distribution of Planet Mass
plt.figure(figsize=(8,6))
sns.histplot(planets['mass'], bins=30, kde=True)

plt.title("Distribution of Planet Mass")
plt.xlabel("Mass")
plt.ylabel("Count")
plt.show()


# 2. Distribution of Orbital Period
plt.figure(figsize=(8,6))
sns.kdeplot(planets['orbital_period'], fill=True)

plt.title("Distribution of Orbital Period")
plt.xlabel("Orbital Period")
plt.ylabel("Density")
plt.show()

# CATEGORICAL PLOTS (2)


# 1. Number of Planets by Discovery Method
plt.figure(figsize=(10,6))
sns.countplot(data=planets, x="method")

plt.title("Planets Discovered by Method")
plt.xlabel("Discovery Method")
plt.ylabel("Number of Planets")
plt.xticks(rotation=45)
plt.show()


# 2. Orbital Period by Discovery Method
plt.figure(figsize=(10,6))
sns.boxplot(data=planets, x="method", y="orbital_period")

plt.title("Orbital Period by Discovery Method")
plt.xlabel("Discovery Method")
plt.ylabel("Orbital Period")
plt.xticks(rotation=45)
plt.show()



# Planets Dataset Explanation: One of the graphs scatterplot of distance vs orbital period shows that planets farther from Earth tend to have longer orbital periods. The line plot of mass vs orbital period indicates that more massive planets generally have longer orbital periods. Another notable one is the count plot showing planets discovered by method, which reveals that the radial and transit are the most common methods for discovering planets. 

