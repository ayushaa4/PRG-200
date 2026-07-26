import pandas as pd
df= pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]
    }
)

print(df)

age=pd.Series([22,35,58],name="Age")
print(age)


print("Minimum Age:", age.min())
print("Maximum Age:", age.max())
print("Average Age:", age.mean())