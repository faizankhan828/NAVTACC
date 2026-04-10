'''
Data Analysis Lab – Thinking Like a Data
Scientist
'''


# Step 1 - Identify Data Type
# Step 2 - Identify Variables
# Step 3 - Determine Analysis Type (Univariate / Bivariate / Multivariate)
# Step 4 - Choose Statistical Measures
# Step 5 - Check Distribution Shape
# Step 6 - Select Visualizations
# Step 7 - Interpret Results
#
# Final Task - Build a Data Analysis Algorithm
# Step 8 - Identify data type (structured / unstructured)
# Step 9 - Identify variables
# Step 10 - Determine number of variables
# Step 11 - Select statistical measures
# Step 12 - Analyze distribution characteristics
# Step 13 - Choose visualization techniques
# Step 14 - Interpret and communicate results

import math

def mean(values):
    return sum(values) / len(values)


def median(values):
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def std_dev(values):
    return math.sqrt(variance(values))


def z_scores(values):
    m = mean(values)
    sd = std_dev(values)
    if sd == 0:
        return [0 for _ in values]
    return [(x - m) / sd for x in values]


def skewness(values):
    m = mean(values)
    sd = std_dev(values)
    if sd == 0:
        return 0
    n = len(values)
    return sum(((x - m) / sd) ** 3 for x in values) / n


def kurtosis(values):
    m = mean(values)
    sd = std_dev(values)
    if sd == 0:
        return 0
    n = len(values)
    return sum(((x - m) / sd) ** 4 for x in values) / n


def correlation(x_values, y_values):
    if len(x_values) != len(y_values):
        raise ValueError("x and y must have the same length")

    x_bar = mean(x_values)
    y_bar = mean(y_values)

    num = sum((x - x_bar) * (y - y_bar) for x, y in zip(x_values, y_values))
    den_x = math.sqrt(sum((x - x_bar) ** 2 for x in x_values))
    den_y = math.sqrt(sum((y - y_bar) ** 2 for y in y_values))

    if den_x == 0 or den_y == 0:
        return 0
    return num / (den_x * den_y)


def detect_unusual(values, threshold=2.0):
    """Return index-value-z tuples where absolute z-score crosses threshold."""
    zs = z_scores(values)
    unusual = []
    for idx, (value, z) in enumerate(zip(values, zs), start=1):
        if abs(z) >= threshold:
            unusual.append((idx, value, round(z, 2)))
    return unusual


def print_univariate_summary(title, values):
    print(f"\n{title}")
    print("-" * len(title))
    print(f"Data: {values}")
    print("Step 1 - Data Type: Structured, quantitative numeric data")
    print("Step 2 - Variable: Single continuous variable")
    print("Step 3 - Analysis Type: Univariate")
    print("Step 4 - Statistical Measures:")
    print(f"  Mean: {mean(values):.2f}")
    print(f"  Median: {median(values):.2f}")
    print(f"  Variance: {variance(values):.2f}")
    print(f"  Standard Deviation: {std_dev(values):.2f}")
    print("Step 5 - Distribution Characteristics:")
    print(f"  Skewness: {skewness(values):.2f}")
    print(f"  Kurtosis: {kurtosis(values):.2f}")
    print("Step 6 - Suggested Visualizations: Histogram, Box Plot")

    unusual = detect_unusual(values, threshold=2.0)
    if unusual:
        print("Unusual Observations (|z| >= 2):")
        for item in unusual:
            print(f"  Position {item[0]} -> value={item[1]}, z={item[2]}")
    else:
        print("Unusual Observations: None detected using |z| >= 2")

    print("Step 7 - Interpretation: Compare center, spread, and possible outliers.")


def question_1_warehouse_productivity():
    workers = ["W1", "W2", "W3", "W4", "W5", "W6"]
    packages_per_hour = [45, 52, 47, 49, 110, 50]

    print("\nQuestion 1 - Warehouse Worker Productivity")
    print("=" * 45)
    # Step 1 - Identify the data type.
    print("Step 1 - Data Type: Structured quantitative numeric data")

    # Step 2 - Identify the variable(s).
    print("Step 2 - Variables:")
    print("  Worker ID (categorical identifier)")
    print("  Packages per Hour (quantitative variable)")

    # Step 3 - Determine analysis type.
    print("Step 3 - Analysis Type: Univariate (productivity measure) with worker labels")

    # Step 4 - Choose statistical measures to summarize productivity.
    print("Step 4 - Statistical Summary:")
    print(f"  Mean: {mean(packages_per_hour):.2f}")
    print(f"  Median: {median(packages_per_hour):.2f}")
    print(f"  Variance: {variance(packages_per_hour):.2f}")
    print(f"  Standard Deviation: {std_dev(packages_per_hour):.2f}")

    # Step 5 - Detect unusual worker performance.
    unusual = detect_unusual(packages_per_hour, threshold=2.0)
    if unusual:
        print("Step 5 - Unusual Worker Performance Detected:")
        for pos, value, z in unusual:
            print(f"  {workers[pos - 1]} packed {value} (z={z})")
    else:
        print("Step 5 - No unusual worker detected using |z| >= 2")

    # Step 6 - Select suitable plots.
    print("Step 6 - Suitable Plots: Histogram, Box Plot, Dot Plot")


def question_2_customer_spending():
    spending = [25, 30, 40, 45, 50, 60, 70, 120, 200]

    print("\nQuestion 2 - Online Store Customer Spending")
    print("=" * 44)
    print(f"Typical Spending (Median): ${median(spending):.2f}")
    print(f"Average Spending (Mean): ${mean(spending):.2f}")
    print(f"Spread (Variance): {variance(spending):.2f}")
    print(f"Spread (Std Dev): {std_dev(spending):.2f}")

    sk = skewness(spending)
    print(f"Skewness: {sk:.2f}")
    if sk > 0:
        print("Distribution Shape: Right-skewed (high spend outliers pull the mean up)")
    elif sk < 0:
        print("Distribution Shape: Left-skewed")
    else:
        print("Distribution Shape: Approximately symmetric")

    print("Appropriate Visualizations: Histogram, Box Plot, Violin Plot")


def question_3_marketing_campaign():
    budget = [2000, 3000, 4000, 5000, 6000]
    visitors = [150, 200, 260, 310, 390]

    print("\nQuestion 3 - Marketing Campaign Analysis")
    print("=" * 40)
    print("Analysis Type: Bivariate (2 variables)")
    print("Variables: Advertising Budget and Website Visitors")

    r = correlation(budget, visitors)
    print(f"Statistical Method: Correlation (Pearson r) = {r:.3f}")

    print("Best Visualization: Scatter Plot with trend line")
    print("Interpretation: Positive relationship expected if higher budgets drive more visitors.")


def question_4_medical_scenario():
    print("\nQuestion 4 - Medical Data Analysis")
    print("=" * 34)
    print("Variables: Age, BMI, Daily Steps, Blood Pressure")
    print("Analysis Type: Multivariate (4 variables)")

    print("Statistical Techniques:")
    print("- Correlation matrix for pairwise linear relationships")
    print("- Multiple linear regression (predict blood pressure)")
    print("- Group comparison tests if categories exist")

    print("Recommended Plots:")
    print("- Pair plot (scatter matrix)")
    print("- Correlation heatmap")
    print("- Box plots by age/BMI groups")


def question_5_social_media_scenario():
    print("\nQuestion 5 - Social Media Engagement")
    print("=" * 38)
    print("Variables: Post Length, Likes, Comments, Shares")
    print("Relevant Focus Variables:")
    print("- Predictor: Post Length")
    print("- Response metrics: Likes, Comments, Shares")

    print("Statistical Techniques:")
    print("- Correlation analysis")
    print("- Multiple regression (engagement metrics as targets)")
    print("- Principal component analysis for engagement patterns")

    print("Recommended Visualizations:")
    print("- Scatter plots (Post Length vs each engagement metric)")
    print("- Heatmap of correlations")
    print("- Bubble chart (likes/comments/shares in one view)")


def print_general_algorithm():
    print("Data Analysis Algorithm (Systematic Thinking)")
    print("=" * 43)
    print("1. Identify data type (structured or unstructured)")
    print("2. Identify variables")
    print("3. Determine number of variables")
    print("4. Select statistical measures")
    print("5. Analyze distribution characteristics")
    print("6. Choose visualization techniques")
    print("7. Interpret and communicate results")


def main():
    print_general_algorithm()

    # Example from prompt (ride-sharing trip duration)
    trip_duration = [12, 15, 13, 16, 14, 12, 13, 40]
    print_univariate_summary("Example - Trip Duration (minutes)", trip_duration)

    # Student questions
    question_1_warehouse_productivity()
    question_2_customer_spending()
    question_3_marketing_campaign()
    question_4_medical_scenario()
    question_5_social_media_scenario()


if __name__ == "__main__":
    main()
