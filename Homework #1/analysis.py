"""Homework 1: explore the supplied CSV using pandas (Option B)."""

import pandas as pd
from pathlib import Path


def main():
    csv_path = Path(__file__).resolve().parent / "online food delivery dataset.csv"
    df = pd.read_csv(csv_path, encoding="utf-8-sig", dtype={"Pin code": str})
    print(f"Dataset: {df.shape[0]} records, {df.shape[1]} columns")

    # Task 1: Print the first 2 rows.
    print("\n1. First 2 rows:")
    print(df.head(2).to_string(index=False))

    # Task 2: Print the first row.
    print("\n2. First row:")
    print(df.iloc[0].to_string())

    # Task 3: Use Python's zero-based positions 10-19, inclusive.
    print("\n3. Rows at Python positions 10-19:")
    print(df.iloc[10:20].to_string())

    # Task 4: pandas labels the blank final header Unnamed: 13.
    print("\n4. Column names:")
    print(df.columns.tolist())

    # Task 5: Print the first 10 values of one column.
    print("\n5. First 10 values of Occupation:")
    print(df["Occupation"].head(10).to_string(index=False))

    # Task 6: Print the first 10 rows of three columns.
    selected_columns = ["Occupation", "Customer Type", "Feedback"]
    print("\n6. First 10 rows of Occupation, Customer Type, and Feedback:")
    print(df[selected_columns].head(10).to_string(index=False))

    # Task 7:

    # Question 1: How many records list Student as the occupation?
    student_count = (df["Occupation"].str.strip() == "Student").sum()
    print("\nQuestion 1: How many records list Student as the occupation?")
    print(f"Student records: {student_count}")

    # Question 2: How many records have Positive feedback?
    positive_count = (df["Feedback"].str.strip() == "Positive").sum()
    print("\nQuestion 2: How many records have Positive feedback?")
    print(f"Positive feedback records: {positive_count}")

    # Question 3: For each customer type, how many records have Positive
    # feedback and how many have Negative feedback?
    # Each count requires BOTH a matching customer type AND feedback label.
    feedback_breakdown = pd.crosstab(
        df["Customer Type"].str.strip(),
        df["Feedback"].str.strip(),
    ).reindex(columns=["Positive", "Negative"], fill_value=0)
    feedback_breakdown["Total"] = feedback_breakdown.sum(axis=1)
    print("\nQuestion 3: Feedback counts by customer type (two conditions):")
    print(feedback_breakdown.to_string())


if __name__ == "__main__":
    main()
