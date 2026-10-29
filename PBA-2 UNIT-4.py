import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print("Employee details:")
print(df[["Name", "Department", "Salary"]])

average_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage salary by department:")
print(average_salary)

average_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()