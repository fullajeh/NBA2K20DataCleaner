import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

csv = pd.read_csv("nba2k-full.csv")
csv.dropna()
csv.drop_duplicates()
csv.columns = [col.strip().lower().replace(" ", "_") for col in csv.columns]


print(csv.head)
print(csv.info)

ratings = csv.sort_values(by="rating", ascending=False).head(15)
print(ratings)

sample_dataGuards = csv[]

plt.bar(ratings["full_name"], ratings['rating'])
plt.xticks(rotation=45)
plt.xlabel("Players")
plt.ylabel("Overall Ratings")
plt.tight_layout()
plt.show()

print(sample_dataGuards)