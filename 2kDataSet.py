import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

csv = pd.read_csv("nba2k-full.csv")
csv.dropna() #Drop null values
csv.drop_duplicates() #Drop duplicate values
csv.columns = [col.strip().lower().replace(" ", "_") for col in csv.columns] #Seperate the Comma and Space seperated values into columns.


print(csv.head)
print(csv.info)

ratings = csv.sort_values(by="rating", ascending=False).head(15)
print(ratings)

plt.bar(ratings["full_name"], ratings['rating']) #Set the X and Y axis data for a Bar Chart.
plt.xticks(rotation=45) # Rotate the player's names so they won't get cut off.
plt.xlabel("Players") # X axis label
plt.ylabel("Overall Ratings") # Y axis label
plt.tight_layout() # Make the chart tighter to fit all the information properly
plt.show()
