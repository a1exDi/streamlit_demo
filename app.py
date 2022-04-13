import streamlit 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_web.csv')
language = df["Язык"]
people_language = df["Носители языка, млн чел."]
print(language)
print(people_language)
plt.figure(figsize=(15, 10))
plt.barh(language, people_language)
plt.title('')

plt.ylabel('Язык')
plt.xlabel('Носителей языка')
plt.grid(True)
plt.show()