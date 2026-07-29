# Pandas Series & DataFrame Complete Guide

> A comprehensive reference for Pandas Series and DataFrames.

---

# Table of Contents

1. What is Pandas?
2. Importing Pandas
3. Pandas Series
4. Creating Series
5. Series Properties
6. Series Functions
7. Indexing & Slicing
8. DataFrame
9. Creating DataFrames
10. DataFrame Properties
11. Selecting Data
12. Adding Columns
13. Deleting Columns
14. Renaming Columns
15. Filtering Data
16. Sorting
17. Missing Values
18. String Operations
19. Mathematical Operations
20. GroupBy
21. Merge, Join & Concat
22. Reading & Writing Files
23. Common Errors
24. Best Practices
25. Most Frequently Used Functions

---

# 1. What is Pandas?

Pandas is a Python library used for

- Data Analysis
- Data Cleaning
- Data Manipulation
- Data Visualization Preparation

Import Pandas:

```python
import pandas as pd
```

---

# 2. Pandas Data Structures

There are two main structures:

## Series

One-dimensional labeled array.

Example:

```python
import pandas as pd

s = pd.Series([10,20,30])
print(s)
```

Output

```
0    10
1    20
2    30
dtype: int64
```

---

## DataFrame

Two-dimensional table.

Example

```python
data = {
    "Name":["Alice","Bob"],
    "Age":[20,21]
}

df = pd.DataFrame(data)
```

---

# 3. Creating a Series

From List

```python
s = pd.Series([10,20,30])
```

From Dictionary

```python
s = pd.Series({
    "A":100,
    "B":200
})
```

Custom Index

```python
s = pd.Series([10,20,30], index=["a","b","c"])
```

Single Value

```python
s = pd.Series(100, index=range(5))
```

---

# 4. Series Properties

| Property | Description |
|-----------|------------|
| index | Returns index |
| values | Returns NumPy array |
| dtype | Data type |
| shape | Shape |
| size | Number of elements |
| ndim | Number of dimensions |
| name | Name of Series |

Example

```python
s.size
s.shape
s.dtype
```

---

# 5. Series Functions

Head

```python
s.head()
```

Tail

```python
s.tail()
```

Describe

```python
s.describe()
```

Mean

```python
s.mean()
```

Median

```python
s.median()
```

Mode

```python
s.mode()
```

Maximum

```python
s.max()
```

Minimum

```python
s.min()
```

Count

```python
s.count()
```

Sum

```python
s.sum()
```

Unique

```python
s.unique()
```

Number of unique values

```python
s.nunique()
```

Value counts

```python
s.value_counts()
```

Sorting

```python
s.sort_values()
```

Sort Index

```python
s.sort_index()
```

---

# 6. Accessing Series

By Position

```python
s.iloc[0]
```

By Label

```python
s.loc["A"]
```

Slicing

```python
s.iloc[1:4]
```

Boolean

```python
s[s>50]
```

---

# 7. Creating DataFrame

Dictionary

```python
df = pd.DataFrame({
    "Name":["Alice","Bob"],
    "Age":[20,21]
})
```

List of Dictionaries

```python
data = [
    {"A":1,"B":2},
    {"A":3,"B":4}
]

df = pd.DataFrame(data)
```

List of Lists

```python
df = pd.DataFrame(
[
[1,2],
[3,4]
],
columns=["A","B"]
)
```

CSV

```python
df = pd.read_csv("data.csv")
```

Excel

```python
df = pd.read_excel("data.xlsx")
```

---

# 8. DataFrame Properties

| Property | Description |
|-----------|------------|
| shape | Rows & columns |
| columns | Column names |
| index | Row index |
| dtypes | Data types |
| size | Total elements |
| ndim | Number of dimensions |
| values | NumPy array |

Example

```python
df.shape
df.columns
df.dtypes
```

---

# 9. DataFrame Inspection

```python
df.head()
```

```python
df.tail()
```

```python
df.info()
```

```python
df.describe()
```

```python
df.sample(5)
```

---

# 10. Selecting Data

Single Column

```python
df["Age"]
```

Multiple Columns

```python
df[["Name","Age"]]
```

Row by Position

```python
df.iloc[0]
```

Rows

```python
df.iloc[1:5]
```

Row by Label

```python
df.loc[0]
```

Specific Cell

```python
df.loc[2,"Age"]
```

---

# 11. Adding Columns

```python
df["Salary"]=[1000,2000]
```

Calculated Column

```python
df["Bonus"]=df["Salary"]*0.10
```

---

# 12. Renaming Columns

Correct

```python
df.rename(columns={"Employee_ID":"EID"})
```

Permanent

```python
df.rename(columns={"Employee_ID":"EID"}, inplace=True)
```

Rename Multiple

```python
df.rename(columns={
"Age":"Years",
"Salary":"Income"
})
```

---

# 13. Delete Columns

```python
df.drop("Age", axis=1)
```

Multiple

```python
df.drop(["Age","Salary"], axis=1)
```

Permanent

```python
df.drop("Age", axis=1, inplace=True)
```

---

# 14. Delete Rows

```python
df.drop(0)
```

```python
df.drop([0,2])
```

---

# 15. Filtering

```python
df[df["Age"]>20]
```

AND

```python
df[(df["Age"]>20) & (df["Salary"]>5000)]
```

OR

```python
df[(df["Age"]>20) | (df["Salary"]>5000)]
```

isin()

```python
df[df["City"].isin(["Delhi","Mumbai"])]
```

---

# 16. Sorting

Ascending

```python
df.sort_values("Age")
```

Descending

```python
df.sort_values("Age",ascending=False)
```

Multiple

```python
df.sort_values(["Age","Salary"])
```

---

# 17. Missing Values

Find Missing

```python
df.isnull()
```

Count Missing

```python
df.isnull().sum()
```

Drop Missing

```python
df.dropna()
```

Fill Missing

```python
df.fillna(0)
```

Forward Fill

```python
df.ffill()
```

Backward Fill

```python
df.bfill()
```

---

# 18. Duplicate Data

Find

```python
df.duplicated()
```

Remove

```python
df.drop_duplicates()
```

---

# 19. String Operations

Uppercase

```python
df["Name"].str.upper()
```

Lowercase

```python
df["Name"].str.lower()
```

Contains

```python
df["Name"].str.contains("A")
```

Length

```python
df["Name"].str.len()
```

Replace

```python
df["Name"].str.replace("A","X")
```

Split

```python
df["Name"].str.split()
```

---

# 20. Mathematical Operations

```python
df.sum()
```

```python
df.mean()
```

```python
df.max()
```

```python
df.min()
```

```python
df.std()
```

```python
df.var()
```

---

# 21. GroupBy

```python
df.groupby("Department").mean()
```

Count

```python
df.groupby("Department").count()
```

Sum

```python
df.groupby("Department").sum()
```

Multiple

```python
df.groupby(["Department","Gender"]).mean()
```

---

# 22. Merge

```python
pd.merge(df1,df2,on="ID")
```

Left

```python
pd.merge(df1,df2,on="ID",how="left")
```

Right

```python
pd.merge(df1,df2,on="ID",how="right")
```

Outer

```python
pd.merge(df1,df2,on="ID",how="outer")
```

---

# 23. Concat

Rows

```python
pd.concat([df1,df2])
```

Columns

```python
pd.concat([df1,df2],axis=1)
```

---

# 24. Reading Files

CSV

```python
pd.read_csv("data.csv")
```

Excel

```python
pd.read_excel("data.xlsx")
```

JSON

```python
pd.read_json("data.json")
```

SQL

```python
pd.read_sql(query, connection)
```

---

# 25. Saving Files

CSV

```python
df.to_csv("output.csv")
```

Excel

```python
df.to_excel("output.xlsx")
```

JSON

```python
df.to_json("output.json")
```

---

# 26. Common Errors

### Wrong

```python
df.rename(columns={"A","B"})
```

Reason:

```
Set is passed instead of dictionary.
```

Correct

```python
df.rename(columns={"A":"B"})
```

---

### Wrong

```python
df["Age","Salary"]
```

Correct

```python
df[["Age","Salary"]]
```

---

### Wrong

```python
df.iloc["Age"]
```

Correct

```python
df["Age"]
```

---

# 27. Best Practices

✔ Use meaningful column names

✔ Prefer vectorized operations

✔ Avoid loops whenever possible

✔ Handle missing values before analysis

✔ Use `.loc` and `.iloc` instead of chained indexing

✔ Keep data types consistent

✔ Use `inplace=True` only when necessary

✔ Save cleaned datasets separately

---

# 28. Most Frequently Used Functions

| Function | Purpose |
|-----------|---------|
| head() | First rows |
| tail() | Last rows |
| info() | Dataset summary |
| describe() | Statistics |
| shape | Dimensions |
| columns | Column names |
| dtypes | Data types |
| rename() | Rename columns |
| drop() | Delete rows/columns |
| sort_values() | Sort data |
| groupby() | Group data |
| merge() | Join DataFrames |
| concat() | Combine DataFrames |
| fillna() | Fill missing values |
| dropna() | Remove missing values |
| duplicated() | Detect duplicates |
| drop_duplicates() | Remove duplicates |
| value_counts() | Frequency count |
| unique() | Unique values |
| nunique() | Count unique values |
| loc[] | Label-based selection |
| iloc[] | Position-based selection |
| to_csv() | Save CSV |
| read_csv() | Read CSV |

---

# Summary

## Series
- One-dimensional
- Has Index
- Like one column

## DataFrame
- Two-dimensional
- Rows + Columns
- Most commonly used Pandas object

Master these concepts:
- Creating
- Selecting
- Filtering
- Cleaning
- Sorting
- Grouping
- Merging
- Saving