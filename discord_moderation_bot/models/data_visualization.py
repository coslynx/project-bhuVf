# File: discord_moderation_bot/models/data_visualization.py (Python)

import matplotlib.pyplot as plt
import pandas as pd

def generate_bar_chart(data, title, x_label, y_label):
    df = pd.DataFrame(data, columns=[x_label, y_label])
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_label], df[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generate_pie_chart(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.show()

# Other necessary data visualization functions can be added here.