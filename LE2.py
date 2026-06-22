import pandas as pd
df = pd.read_csv("sleep_health_data.csv")

print(df.columns)
print()

# Question 1
lowest_sleep_occ = df.groupby("Occupation")["Sleep Duration"].mean().idxmin()
print("Occupation with the lowest average sleep duration:")
print(lowest_sleep_occ)
print()

# Question 2
lowest_sleep_quality_occ = df.groupby("Occupation")["Quality of Sleep"].mean().idxmin()
print("Occupation with the lowest average sleep quality:")
print(lowest_sleep_quality_occ)
print()

# Question 3
same_occ = lowest_sleep_occ == lowest_sleep_quality_occ
print("Is it the same occupation?")
print(same_occ)
print()