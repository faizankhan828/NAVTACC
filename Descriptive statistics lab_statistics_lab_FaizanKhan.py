"""
Descriptive Statistics Lab
Scenario 1: City General Hospital
Scenario 2: Nova Commerce

"""

import math


# ============================================================================
# Utility Functions (from scratch formulas)
# ============================================================================

def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def mode_values(data):
    freq = {}
    for value in data:
        freq[value] = freq.get(value, 0) + 1
    max_count = max(freq.values())
    modes = sorted([k for k, v in freq.items() if v == max_count])
    return modes, max_count


def population_variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def population_std_dev(data):
    return math.sqrt(population_variance(data))


def coefficient_of_variation_percent(data):
    m = mean(data)
    if m == 0:
        return 0
    return (population_std_dev(data) / m) * 100


def descriptive_stats(data):
    modes, mode_count = mode_values(data)
    return {
        "n": len(data),
        "mean": mean(data),
        "median": median(data),
        "modes": modes,
        "mode_count": mode_count,
        "min": min(data),
        "max": max(data),
        "range": max(data) - min(data),
        "variance": population_variance(data),
        "std_dev": population_std_dev(data),
        "cv": coefficient_of_variation_percent(data),
    }


def cv_label(cv_percent):
    if cv_percent < 15:
        return "Low variability"
    if cv_percent <= 30:
        return "Moderate variability"
    return "High variability"


def print_summary(name, stats, money=False):
    symbol = "$" if money else ""

    if len(stats["modes"]) == 1:
        mode_text = f"{symbol}{stats['modes'][0]}"
    else:
        mode_text = "No clear single mode"

    print("-----------------------------------------")
    print(f"Dataset : {name}")
    print(f"n       : {stats['n']}")
    print(f"Mean    : {symbol}{stats['mean']:.2f}")
    print(f"Median  : {symbol}{stats['median']:.2f}")
    print(f"Mode    : {mode_text} (count={stats['mode_count']})")
    print(f"Min     : {symbol}{stats['min']}")
    print(f"Max     : {symbol}{stats['max']}")
    print(f"Range   : {symbol}{stats['range']}")
    print(f"Var (σ²): {stats['variance']:.4f}")
    print(f"Std (σ) : {symbol}{stats['std_dev']:.4f}")
    print(f"CV (%)  : {stats['cv']:.4f}% [{cv_label(stats['cv'])}]")


# ============================================================================
# SCENARIO 1 - CITY GENERAL HOSPITAL
# ============================================================================

# Part A - Datasets
general_ward = [
    12, 18, 22, 15, 19, 25, 14, 20, 17, 23,
    16, 21, 13, 18, 24, 19, 15, 22, 20, 17,
    14, 18, 21, 16, 19, 23, 15, 20, 18, 22,
    17, 14, 21, 19, 16, 18, 20, 15, 22, 19,
    13, 17, 21, 18, 15, 20, 16, 23, 19, 14,
    18, 21, 16, 20, 15, 22, 18, 19, 17, 14,
]

trauma_ward = [
    8, 45, 12, 67, 5, 32, 88, 14, 6, 55,
    42, 9, 71, 18, 3, 50, 27, 83, 11, 38,
    7, 62, 15, 44, 91, 10, 33, 58, 4, 76,
    20, 47, 9, 65, 13, 40, 86, 17, 6, 53,
    29, 8, 72, 19, 5, 48, 31, 80, 12, 37,
    11, 60, 16, 43, 89, 10, 35, 57, 7, 74,
]

# Part A - Q1 pre-code visual interpretation (comment answer)
# Q1 Answer:
# Trauma Ward is clearly more variable by visual inspection.
# Clue 1: General Ward values are tightly clustered (~13 to 25).
# Clue 2: Trauma Ward spans very small to very large values (~3 to 91).
# Clue 3: Trauma data has extreme jumps and likely outliers.

print("SCENARIO 1 - CITY GENERAL HOSPITAL")
print("Q1 quick range check (visual clue support):")
print(f"General Ward min/max: {min(general_ward)} / {max(general_ward)}")
print(f"Trauma Ward min/max : {min(trauma_ward)} / {max(trauma_ward)}")

# Part B - Task 1 to Task 5 using from-scratch functions
general_stats = descriptive_stats(general_ward)
trauma_stats = descriptive_stats(trauma_ward)

# Part C - Results table outputs
print("\nPart C - Computed Results")
print_summary("General Ward", general_stats, money=False)
print_summary("Trauma Ward", trauma_stats, money=False)

# Part D - Interpretation Questions (printed answers)
print("\nPart D - Interpretation Answers")

# Q2 - Mean vs Median in Trauma Ward
print("Q2:")
print(
    "Trauma Ward mean and median differ noticeably. The mean is pulled by high values, "
    "suggesting a right-skewed distribution (long tail of long waits)."
)

# Q3 - Mode interpretation
print("Q3:")
if len(general_stats["modes"]) == 1:
    print(
        f"General Ward has a clear mode ({general_stats['modes'][0]}), "
        "which indicates a common typical waiting-time value."
    )
else:
    print("General Ward has multiple repeated common values.")
print(
    "Trauma Ward may show no clear single mode or many tied modes because waits are spread "
    "across a wide range."
)

# Q4 - Standard deviation meaning
print("Q4:")
print(
    "The ward with higher standard deviation is less predictable. For a patient, expected wait "
    "time is uncertain and can vary a lot from short to very long."
)

# Q5 - CV quality target
print("Q5:")
for ward_name, st in [("General Ward", general_stats), ("Trauma Ward", trauma_stats)]:
    status = "PASS" if st["cv"] < 30 else "FAIL"
    print(f"{ward_name}: CV={st['cv']:.2f}% -> {status} ({cv_label(st['cv'])})")
print(
    "It is not surprising that Trauma may fail due to extreme high waits and broad spread."
)

# Part E - Bonus: Paediatric Ward
paediatric_ward = [
    10, 12, 11, 14, 13, 9, 15, 12, 11, 10,
    13, 12, 14, 11, 10, 13, 12, 15, 11, 14,
    10, 12, 13, 11, 14, 10, 12, 13, 11, 9,
    14, 12, 11, 13, 10, 15, 12, 11, 14, 13,
    10, 12, 11, 14, 13, 9, 12, 11, 10, 13,
    14, 12, 11, 10, 13, 15, 12, 11, 14, 10,
]

paediatric_stats = descriptive_stats(paediatric_ward)
print("\nPart E - Bonus: Paediatric Ward")
print_summary("Paediatric Ward", paediatric_stats, money=False)

# Q6 - Rank hospital wards by consistency (lowest CV is most consistent)
ward_cvs = [
    ("General Ward", general_stats["cv"]),
    ("Trauma Ward", trauma_stats["cv"]),
    ("Paediatric Ward", paediatric_stats["cv"]),
]
ward_cvs_sorted = sorted(ward_cvs, key=lambda x: x[1])
print("Q6 - Ward ranking by consistency (most -> least):")
for name, cv in ward_cvs_sorted:
    print(f"{name}: CV={cv:.2f}%")
print(
    "As a patient, the most consistent ward (lowest CV) gives the most predictable wait time."
)


# ============================================================================
# SCENARIO 2 - NOVA COMMERCE
# ============================================================================

# Part A - Datasets
electronics = [
    4200, 8750, 3100, 12400, 5600, 9300, 2800, 15000, 6700, 4100,
    7800, 11200, 3500, 9600, 4900, 13500, 6100, 8200, 3200, 10800,
    5300, 7400, 14200, 4600, 9100, 3800, 11800, 6500, 8900, 4300,
    7200, 12600, 5100, 9800, 3700, 13100, 6800, 8400, 4000, 10500,
    5700, 7600, 11500, 4400, 9400, 3600, 12900, 6200, 8700, 4700,
    7100, 14800, 5400, 9200, 3900, 11100, 6400, 8100, 4800, 10200,
]

fashion = [
    1850, 2100, 1750, 2300, 1950, 2050, 1800, 2200, 1900, 2150,
    1700, 2250, 2000, 1850, 2100, 1950, 1800, 2350, 1750, 2000,
    2100, 1900, 2050, 1850, 2200, 1700, 2100, 1950, 1800, 2300,
    2000, 1850, 2150, 1900, 2050, 1800, 2250, 1750, 2100, 1950,
    1900, 2000, 1850, 2200, 1750, 2050, 1900, 2300, 1800, 2100,
    2050, 1850, 2150, 1700, 2000, 1900, 2250, 1800, 2100, 1950,
]

# Part A - Q7 expectation (comment answer)
# Q7 Answer:
# Electronics is expected to have higher CV because promotions, stockouts, and high-ticket
# products create bigger swings. Fashion demand is usually steadier and seasonally smoother.

print("\n\nSCENARIO 2 - NOVA COMMERCE")

# Part B - Task 1 and Task 2
electronics_stats = descriptive_stats(electronics)
fashion_stats = descriptive_stats(fashion)

# Part B - Task 3 formatted report
print("Part B/C - Formatted Summary Report")
print_summary("Electronics", electronics_stats, money=True)
print_summary("Fashion", fashion_stats, money=True)

# Part D - Interpretation Questions
print("\nPart D - Interpretation Answers")
print("Q8:")
print(
    "A higher mean is not always better. Electronics may generate higher average sales but with "
    "higher volatility and planning risk. Trade-off: reward vs predictability."
)

print("Q9:")
print(
    "Standard deviation is scale-dependent, so direct comparison is misleading when means differ. "
    "CV standardizes spread relative to mean, enabling fair comparison across categories."
)

print("Q10:")
safer = "Electronics" if electronics_stats["cv"] < fashion_stats["cv"] else "Fashion"
riskier = "Fashion" if safer == "Electronics" else "Electronics"
print(
    f"Safer for predictable returns: {safer} (lower CV). "
    f"Riskier but potentially more rewarding: {riskier} (higher CV or larger upside swings)."
)

# Part E - Outlier Sensitivity Task (Bonus)
electronics_with_flash = electronics + [45000]
mean_before = mean(electronics)
median_before = median(electronics)
mean_after = mean(electronics_with_flash)
median_after = median(electronics_with_flash)

print("\nPart E - Outlier Sensitivity")
print(f"Mean before outlier : ${mean_before:.2f}")
print(f"Median before outlier: ${median_before:.2f}")
print(f"Mean after outlier  : ${mean_after:.2f}")
print(f"Median after outlier : ${median_after:.2f}")
print("Q11:")
print(
    "Mean changes more than median after adding a large outlier, showing median is more "
    "resistant (robust) to extreme values."
)


# ============================================================================
# FINAL REFLECTION + OVERALL SUMMARY TABLE
# ============================================================================

print("\n\nFINAL REFLECTION")

print("Q12:")
print(
    "Use median when data is skewed or has outliers. Example: Trauma Ward where extreme high "
    "waits pull the mean upward."
)

print("Q13:")
print(
    "CV compares variability fairly across datasets with different units/scales by dividing "
    "standard deviation by mean."
)

print("Q14:")
print(
    "Population std dev uses all values (divide by n). Sample std dev estimates population from "
    "a subset (divide by n-1). Use population when you have the full group; sample for inference."
)

# Q15 - Rank all four datasets (General, Trauma, Electronics, Fashion)
all_cvs = [
    ("General Ward", general_stats["cv"]),
    ("Trauma Ward", trauma_stats["cv"]),
    ("Electronics", electronics_stats["cv"]),
    ("Fashion", fashion_stats["cv"]),
]
all_cvs_sorted = sorted(all_cvs, key=lambda x: x[1])

print("Q15 - Consistency ranking by CV (most -> least):")
for name, cv in all_cvs_sorted:
    print(f"{name}: CV={cv:.2f}%")

print("\nOverall Summary Table (computed)")
print("Name | Mean | Median | Mode | Std Dev (σ) | CV (%) | Most Consistent?")

def mode_text(stats):
    if len(stats["modes"]) == 1:
        return str(stats["modes"][0])
    return "multi/no clear"

summary_rows = [
    ("General Ward", general_stats),
    ("Trauma Ward", trauma_stats),
    ("Electronics", electronics_stats),
    ("Fashion", fashion_stats),
]

best_cv = min(st["cv"] for _, st in summary_rows)
for name, st in summary_rows:
    consistent_tag = "Yes" if abs(st["cv"] - best_cv) < 1e-9 else "No"
    print(
        f"{name} | {st['mean']:.2f} | {st['median']:.2f} | {mode_text(st)} | "
        f"{st['std_dev']:.2f} | {st['cv']:.2f}% | {consistent_tag}"
    )


