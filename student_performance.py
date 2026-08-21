import pandas as pd

df = pd.read_csv("Q37_student_performance.csv")

df["assignment_score"] = pd.to_numeric(df["assignment_score"], errors="coerce")
df["assignment_score"] = df["assignment_score"].fillna(df["assignment_score"].mean())

df = df.drop_duplicates(subset="student_id")

df["attendance_percent"] = pd.to_numeric(df["attendance_percent"], errors="coerce")
df = df[(df["attendance_percent"] >= 0) & (df["attendance_percent"] <= 100)]

df["internal_assessment_average"] = (
    df["assignment_score"] + df["internal_marks"]
) / 2

df["attendance_category"] = pd.cut(
    df["attendance_percent"],
    bins=[-1, 59, 74, 100],
    labels=["Low", "Medium", "High"]
)

df["study_hour_group"] = pd.cut(
    df["study_hours_per_week"],
    bins=[-1, 10, 20, float("inf")],
    labels=["Low", "Medium", "High"]
)

print("\nAttendance Performance")
print(
    df.groupby("attendance_category", observed=True)[
        ["internal_assessment_average", "final_exam_marks"]
    ].mean()
)

print("\nStudy Hour Performance")
print(
    df.groupby("study_hour_group", observed=True)[
        ["internal_assessment_average", "final_exam_marks"]
    ].mean()
)

print("\nFinal Dataset")
print(df)

df.to_csv("Q37_student_performance_processed.csv", index=False)