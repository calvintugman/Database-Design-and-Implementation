# Asking Questions with CSV Data

## Why I chose this dataset

I chose the online food delivery dataset because it connects an everyday service with questions about customer characteristics and feedback. Its categories make it possible to practice filtering and counting.

## Dataset and approach

- **File:** `online food delivery dataset.csv`
- **Size:** 388 data records, excluding the header, and 14 columns 
- **Categorical columns:** Examples include `Occupation`, `Customer Type`, and `Feedback`.
- **Implementation:** Option B, pandas using a DataFrame.
- **Source:** [Online Food Ordering Dataset on Kaggle](https://www.kaggle.com/datasets/srisyra02/online-food-ordering-dataset?resource=download), the original download link supplied for this CSV.

###
## Three data questions

### Question 1: How many records list Student as the occupation?

```python
# How many records list Student as the occupation?
student_count = (df["Occupation"].str.strip() == "Student").sum()
```

**Output:**

```text
Student records: 207
```

**Why the structure supports this question:** Every record has an `Occupation` field. Filtering that field for the category `Student` and counting the matches answers the question directly. The result describes student records in this file.

### Question 2: How many records have Positive feedback?

```python
# How many records have Positive feedback?
positive_count = (df["Feedback"].str.strip() == "Positive").sum()
```

**Output:**

```text
Positive feedback records: 317
```

**Why the structure supports this question:** Feedback is stored in a separate field on each row. Comparing its value to `Positive` lets the program count matching records consistently.

### Question 3: For each customer type, how many records have Positive feedback and how many have Negative feedback?

```python
# For each customer type, how many records have Positive or Negative feedback?
feedback_breakdown = pd.crosstab(
    df["Customer Type"].str.strip(),
    df["Feedback"].str.strip(),
).reindex(columns=["Positive", "Negative"], fill_value=0)
feedback_breakdown["Total"] = feedback_breakdown.sum(axis=1)
```

**Output:**

```text
Feedback       Positive  Negative  Total
Customer Type
Frequent            120        26    146
New                  18         6     24
Regular             179        39    218
```

**Why the structure supports this question:** Each row connects a `Customer` value to a `Feedback` value. `pd.crosstab()` builds a frequency table from the two columns. Each table cell counts records satisfying two conditions at once: the specified customer type **and** the specified feedback. This shows how relationships can be explored within a file without joining separate tables.

## What the data cannot answer

I would like to know whether longer delivery times cause negative feedback, but this dataset cannot answer that question. It contains feedback labels but lacks order timestamps, delivery durations, and information about food quality or order accuracy. It also lacks unique customer and order identifiers that would connect feedback to specific deliveries or repeated purchases. 

## Submission files

- `analysis.py`
- `README.md`
- `online food delivery dataset.csv`


