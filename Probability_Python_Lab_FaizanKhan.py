"""
Probability.py
Hands-on Python probability lab from classical probability to Bayesian inference.
Each lab section includes clear comment headers matching the worksheet structure.
"""

import itertools
import math
import random
from collections import Counter
from fractions import Fraction


# ============================================================================
# LAB 1 - Basic Probability Concepts
# ============================================================================

# LAB 1 - Starter Code: Dice Probability
sample_space = [1, 2, 3, 4, 5, 6]


def classical_prob(event, space):
    """P(A) = n(A) / n(S)"""
    return len(event) / len(space)


# Define events
# LAB 1 - Starter Code: Dice Probability events
event_even = [x for x in sample_space if x % 2 == 0]
event_gt4 = [x for x in sample_space if x > 4]
event_prime = [x for x in sample_space if x in [2, 3, 5]]

print("LAB 1 - Basic Probability Concepts")
print("Sample space:", sample_space)
print("Even numbers:", event_even)
print(f"P(even) = {classical_prob(event_even, sample_space):.4f}")
print(f"P(> 4) = {classical_prob(event_gt4, sample_space):.4f}")
print(f"P(prime) = {classical_prob(event_prime, sample_space):.4f}")

# LAB 1 - Complement Rule
p_even = classical_prob(event_even, sample_space)
print(f"P(not even) = 1 - {p_even} = {1 - p_even:.4f}")


# LAB 1 - Empirical Probability by Simulation

def roll_die(n_rolls):
    """Simulate rolling a fair 6-sided die n_rolls times."""
    return [random.randint(1, 6) for _ in range(n_rolls)]


def empirical_prob(outcomes, condition_fn):
    """P(A) = count(A happened) / total trials"""
    favourable = sum(1 for x in outcomes if condition_fn(x))
    return favourable / len(outcomes)


# LAB 1 - Empirical Probability by Simulation run
random.seed(42)
for n in [10, 100, 1000, 10000, 100000]:
    rolls = roll_die(n)
    p_emp = empirical_prob(rolls, lambda x: x % 2 == 0)
    print(f"n={n:7d} Empirical P(even) = {p_emp:.4f} Error from true: {abs(p_emp - 0.5):.4f}")


# LAB 1 - Exercise 1A: Coin Flip Probabilities

def coin_sample_space():
    return ["".join(t) for t in itertools.product(["H", "T"], repeat=3)]


# LAB 1 - Exercise 1A: Coin Flip Probabilities solution
coin_space = coin_sample_space()
all_heads = [x for x in coin_space if x == "HHH"]
exactly_two_heads = [x for x in coin_space if x.count("H") == 2]
at_least_one_tail = [x for x in coin_space if "T" in x]

print("\nLAB 1 - Exercise 1A: Coin Flip Probabilities")
print("Sample space:", coin_space)
print("P(all three heads) =", classical_prob(all_heads, coin_space))
print("P(exactly two heads) =", classical_prob(exactly_two_heads, coin_space))
print("P(at least one tail) =", classical_prob(at_least_one_tail, coin_space))
print("Fraction form:")
print("  P(all three heads) =", Fraction(len(all_heads), len(coin_space)))
print("  P(exactly two heads) =", Fraction(len(exactly_two_heads), len(coin_space)))
print("  P(at least one tail) =", Fraction(len(at_least_one_tail), len(coin_space)))

# LAB 1 - Exercise 1A: Coin Flip Probabilities empirical verification
random.seed(1)
n_trials = 50000
coin_rolls = ["".join(random.choice(["H", "T"]) for _ in range(3)) for _ in range(n_trials)]
print("Empirical verification with 50000 trials:")
print("  P(all three heads) =", sum(1 for x in coin_rolls if x == "HHH") / n_trials)
print("  P(exactly two heads) =", sum(1 for x in coin_rolls if x.count("H") == 2) / n_trials)
print("  P(at least one tail) =", sum(1 for x in coin_rolls if "T" in x) / n_trials)


# LAB 1 - Challenge: Birthday Problem

def birthday_problem(n_people, n_simulations=20000):
    """Estimate P(at least one shared birthday) for a group of n_people."""
    shared = 0
    for _ in range(n_simulations):
        birthdays = [random.randint(1, 365) for _ in range(n_people)]
        if len(set(birthdays)) < len(birthdays):
            shared += 1
    return shared / n_simulations


# LAB 1 - Challenge run
print("\nLAB 1 - Challenge: Birthday Problem")
random.seed(2)
for n_people in [10, 20, 23, 30, 50]:
    print(f"n={n_people:2d}  P(shared birthday) ≈ {birthday_problem(n_people):.4f}")


# ============================================================================
# LAB 2 - Set Theory & Probability Rules
# ============================================================================

# LAB 2 - Starter Code: Set Operations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [(v, s) for s in suits for v in values]

A = set(c for c in deck if c[1] == "Hearts")
B = set(c for c in deck if c[0] == "K")
A_union_B = A | B
A_intersect_B = A & B
A_only = A - B

print("\nLAB 2 - Set Theory & Probability Rules")
print(f"Total cards in deck: {len(deck)}")
print(f"|A| Hearts = {len(A)}")
print(f"|B| Kings = {len(B)}")
print(f"|A ∪ B| = {len(A_union_B)}")
print(f"|A ∩ B| = {len(A_intersect_B)} <- King of Hearts")

N = len(deck)
P_A = len(A) / N
P_B = len(B) / N
P_A_inter_B = len(A_intersect_B) / N
P_A_union_B = P_A + P_B - P_A_inter_B
print(f"P(Heart) = {P_A:.4f}")
print(f"P(King) = {P_B:.4f}")
print(f"P(Heart ∩ King) = {P_A_inter_B:.4f}")
print(f"P(Heart ∪ King) = {P_A_union_B:.4f} (addition rule)")
print(f"Verified by counting: {len(A_union_B)/N:.4f}")


# LAB 2 - Exercise 2A: Venn Diagram Probability
maths = set(range(0, 18))
physics = set(range(7, 22))
union_students = maths | physics
intersection_students = maths & physics
only_maths = maths - physics

print("\nLAB 2 - Exercise 2A: Venn Diagram Probability")
print(f"P(Maths OR Physics) = {len(union_students) / 40:.4f}")
print(f"P(ONLY Maths) = {len(only_maths) / 40:.4f}")
print(f"P(Maths ∩ Physics) = {len(intersection_students) / 40:.4f}")


# LAB 2 - Exercise 2B: Complement Trick - At Least One Problem
print("\nLAB 2 - Exercise 2B: Complement Trick")
random.seed(3)
n_trials = 100000
at_least_one_blue = 0
for _ in range(n_trials):
    draw = random.choices(["R", "B"], weights=[6, 4], k=3)
    if "B" in draw:
        at_least_one_blue += 1
p_emp_blue = at_least_one_blue / n_trials
p_no_blue = (0.6) ** 3
print(f"P(at least one blue) theoretical = {1 - p_no_blue:.4f}")
print(f"P(at least one blue) empirical   = {p_emp_blue:.4f}")


# LAB 2 - Challenge: Two Dice Sample Space
print("\nLAB 2 - Challenge: Two Dice")
two_dice_space = list(itertools.product(range(1, 7), repeat=2))

def dice_event(space, condition):
    return [x for x in space if condition(x)]


event_sum_7 = dice_event(two_dice_space, lambda x: sum(x) == 7)
event_sum_11 = dice_event(two_dice_space, lambda x: sum(x) == 11)
event_even_or_first3 = dice_event(two_dice_space, lambda x: (sum(x) % 2 == 0) or (x[0] == 3))
event_doubles = dice_event(two_dice_space, lambda x: x[0] == x[1])

print(f"P(sum=7) = {len(event_sum_7) / len(two_dice_space):.4f}")
print(f"P(sum=7 OR sum=11) = {len(set(event_sum_7) | set(event_sum_11)) / len(two_dice_space):.4f}")
print(f"P(sum even OR first die=3) = {len(event_even_or_first3) / len(two_dice_space):.4f}")
print(f"P(doubles) = {len(event_doubles) / len(two_dice_space):.4f}")


# ============================================================================
# LAB 3 - Independence & Mutual Exclusivity
# ============================================================================

# LAB 3 - Starter Code: Testing Independence
random.seed(99)
n = 10000
exercise = [1 if random.random() < 0.6 else 0 for _ in range(n)]
diet = [1 if random.random() < 0.5 else 0 for _ in range(n)]
P_E = sum(exercise) / n
P_D = sum(diet) / n
P_ED = sum(e and d for e, d in zip(exercise, diet)) / n
expected_if_independent = P_E * P_D

print("\nLAB 3 - Independence & Mutual Exclusivity")
print(f"P(Exercise) = {P_E:.4f}")
print(f"P(Good diet) = {P_D:.4f}")
print(f"P(Exercise AND Diet) = {P_ED:.4f}")
print(f"P(E) * P(D) = {expected_if_independent:.4f}")
print(f"Difference: {abs(P_ED - expected_if_independent):.4f}")
print("Independent?", abs(P_ED - expected_if_independent) < 0.01)


# LAB 3 - Starter Code: Dependent Events (Without Replacement)
def draw_two_hearts_with_replacement(n_trials):
    """Independent: drawing with replacement"""
    count = 0
    for _ in range(n_trials):
        card1 = random.randint(1, 52)
        card2 = random.randint(1, 52)
        if card1 <= 13 and card2 <= 13:
            count += 1
    return count / n_trials


def draw_two_hearts_without_replacement(n_trials):
    """Dependent: drawing without replacement"""
    count = 0
    for _ in range(n_trials):
        card1 = random.randint(1, 52)
        if card1 <= 13:
            card2 = random.randint(1, 51)
            if card2 <= 12:
                count += 1
    return count / n_trials


random.seed(7)
n = 100000
p_with = draw_two_hearts_with_replacement(n)
p_without = draw_two_hearts_without_replacement(n)
theory_with = (13 / 52) * (13 / 52)
theory_without = (13 / 52) * (12 / 51)
print("--- With Replacement (Independent) ---")
print(f"Simulated: {p_with:.4f}")
print(f"Theoretical: {theory_with:.4f}")
print("--- Without Replacement (Dependent) ---")
print(f"Simulated: {p_without:.4f}")
print(f"Theoretical: {theory_without:.4f}")


# LAB 3 - Exercise 3A: Independence Checker Function

def check_independence(P_A, P_B, P_A_and_B, tolerance=0.001):
    expected = P_A * P_B
    diff = abs(P_A_and_B - expected)
    status = "INDEPENDENT" if diff < tolerance else "DEPENDENT"
    print(f"P(A) = {P_A:.4f}")
    print(f"P(B) = {P_B:.4f}")
    print(f"P(A AND B) = {P_A_and_B:.4f}")
    print(f"P(A) * P(B) = {expected:.4f}")
    print(f"Difference = {diff:.4f}")
    print(status)
    return status


print("\nLAB 3 - Exercise 3A: Independence Checker")
check_independence(0.5, 0.4, 0.20)
check_independence(0.3, 0.6, 0.25)
check_independence(0.7, 0.3, 0.0)


# ============================================================================
# LAB 4 - Counting, Permutations & Combinations
# ============================================================================

print("\nLAB 4 - Counting, Permutations & Combinations")
print("=== Factorials ===")
for n_val in range(0, 8):
    print(f"{n_val}! = {math.factorial(n_val)}")

print("=== Permutations P(n,r) ===")
n_val, r_val = 10, 3
perm = math.perm(n_val, r_val)
print(f"P({n_val},{r_val}) = {perm}")

print("=== Combinations C(n,r) ===")
n_val, r_val = 52, 5
comb = math.comb(n_val, r_val)
print(f"C({n_val},{r_val}) = {comb:,}")

print("=== Probabilities ===")
lottery = math.comb(49, 6)
print(f"C(49,6) = {lottery:,}")
print(f"P(lottery jackpot) = 1/{lottery:,} = {1/lottery:.10f}")


# LAB 4 - Starter Code: Listing Combinations
print("\nLAB 4 - Starter Code: Listing Combinations")
items = ["A", "B", "C"]
all_perms = list(itertools.permutations(items))
print(f"All permutations of {items}:")
for p in all_perms:
    print(" ".join(p))
print(f"Total: {len(all_perms)} = {len(items)}! = {math.factorial(len(items))}")

items = ["A", "B", "C", "D"]
all_combs = list(itertools.combinations(items, 2))
print(f"All C({len(items)},2) combinations: {all_combs}")
print(f"Total: {len(all_combs)} = C({len(items)},2) = {math.comb(len(items), 2)}")


# LAB 4 - Exercise 4A: Poker Hand Probabilities
print("\nLAB 4 - Exercise 4A: Poker Hand Probabilities")
total_hands = math.comb(52, 5)

def exactly_one_pair_count():
    return math.comb(13, 1) * math.comb(4, 2) * math.comb(12, 3) * (4 ** 3)

p_pair = exactly_one_pair_count() / total_hands
p_at_least_one_ace = 1 - math.comb(48, 5) / total_hands
print(f"P(pair) = {p_pair:.6f}")
print(f"P(at least one Ace) = {p_at_least_one_ace:.6f}")

# LAB 4 - Exercise 4A simulation
random.seed(10)
card_deck = [(v, s) for s in suits for v in values]
ace_count = 0
n_trials = 100000
for _ in range(n_trials):
    hand = random.sample(card_deck, 5)
    if any(card[0] == "A" for card in hand):
        ace_count += 1
print(f"Simulated P(at least one Ace) = {ace_count / n_trials:.6f}")


# LAB 4 - Exercise 4B: Committee Selection
print("\nLAB 4 - Exercise 4B: Committee Selection")
team_total = math.comb(13, 4)
team_2e_2m = math.comb(8, 2) * math.comb(5, 2)
p_2e_2m = team_2e_2m / team_total
p_at_least_1_manager = 1 - math.comb(8, 4) / team_total
print(f"Total teams: {team_total}")
print(f"Exactly 2 engineers and 2 managers: {team_2e_2m}")
print(f"Probability = {p_2e_2m:.6f}")
print(f"P(at least 1 manager) = {p_at_least_1_manager:.6f}")


# LAB 4 - Challenge: Password Security Analysis
print("\nLAB 4 - Challenge: Password Security Analysis")
seconds_per_year = 31_536_000
rate = 10_000_000_000
policies = {
    "A": 26 ** 6,
    "B": 26 ** 8,
    "C": 52 ** 8,
    "D": 62 ** 8,
    "E": 62 ** 12,
}
for name, possibilities in policies.items():
    years = possibilities / rate / seconds_per_year
    print(f"Policy {name}: {possibilities:.3e} possibilities, ~{years:.6f} years to crack")


# ============================================================================
# LAB 5 - Joint, Marginal & Conditional Probability
# ============================================================================

# LAB 5 - Starter Code: Contingency Table
print("\nLAB 5 - Joint, Marginal & Conditional Probability")
data = {
    ("Studies", "Pass"): 420,
    ("Studies", "Fail"): 80,
    ("NoStudy", "Pass"): 140,
    ("NoStudy", "Fail"): 360,
}
total = sum(data.values())
print(f"Total students surveyed: {total}")

joint = {k: v / total for k, v in data.items()}
print("--- Joint Probabilities ---")
for k, p in joint.items():
    print(f" P({k[0]}, {k[1]}) = {p:.4f}")

P_studies = joint[("Studies", "Pass")] + joint[("Studies", "Fail")]
P_nostudy = joint[("NoStudy", "Pass")] + joint[("NoStudy", "Fail")]
P_pass = joint[("Studies", "Pass")] + joint[("NoStudy", "Pass")]
P_fail = joint[("Studies", "Fail")] + joint[("NoStudy", "Fail")]
print("--- Marginal Probabilities ---")
print(f" P(Studies) = {P_studies:.4f}")
print(f" P(No Study) = {P_nostudy:.4f}")
print(f" P(Pass) = {P_pass:.4f}")
print(f" P(Fail) = {P_fail:.4f}")

P_pass_given_studies = joint[("Studies", "Pass")] / P_studies
P_pass_given_nostudy = joint[("NoStudy", "Pass")] / P_nostudy
print("--- Conditional Probabilities ---")
print(f" P(Pass | Studies) = {P_pass_given_studies:.4f}")
print(f" P(Pass | No Study) = {P_pass_given_nostudy:.4f}")
print(f" Overall P(Pass) = {P_pass:.4f}")
print(f" Studying increases pass rate by: {(P_pass_given_studies - P_pass_given_nostudy) * 100:.1f} percentage points")


# LAB 5 - Exercise 5A: Build a Probability Table Printer

def prob_table(data_dict):
    total = sum(data_dict.values())
    labels_1 = sorted({k[0] for k in data_dict})
    labels_2 = sorted({k[1] for k in data_dict})

    print("\nProbability Table")
    print(f"Total count: {total}")
    print("Counts and probabilities:")
    for a in labels_1:
        for b in labels_2:
            count = data_dict.get((a, b), 0)
            print(f"  ({a}, {b}) = {count} -> {count / total:.4f}")

    row_totals = {a: sum(data_dict.get((a, b), 0) for b in labels_2) for a in labels_1}
    col_totals = {b: sum(data_dict.get((a, b), 0) for a in labels_1) for b in labels_2}
    print("Marginals:")
    for a, c in row_totals.items():
        print(f"  P({a}) = {c / total:.4f}")
    for b, c in col_totals.items():
        print(f"  P({b}) = {c / total:.4f}")

    print("Conditional probabilities:")
    for a in labels_1:
        for b in labels_2:
            cond1 = data_dict.get((a, b), 0) / row_totals[a] if row_totals[a] else 0
            cond2 = data_dict.get((a, b), 0) / col_totals[b] if col_totals[b] else 0
            print(f"  P({b} | {a}) = {cond1:.4f}")
            print(f"  P({a} | {b}) = {cond2:.4f}")


print("\nLAB 5 - Exercise 5A: Weather vs Sales")
weather_sales = {
    ("Sunny", "HighSales"): 300,
    ("Sunny", "LowSales"): 100,
    ("Rainy", "HighSales"): 150,
    ("Rainy", "LowSales"): 450,
}
prob_table(weather_sales)

print("Does weather affect sales?")
print("P(HighSales | Sunny) =", 300 / 400)
print("P(HighSales | Rainy) =", 150 / 600)
print("Conclusion: sales are more likely on sunny days in this dataset.")


# LAB 5 - Exercise 5B: Conditional Probability Simulation
print("\nLAB 5 - Exercise 5B: Conditional Probability Simulation")
random.seed(11)
trials = 100000
sum8 = 0
sum8_and_first3 = 0
first3 = 0
for _ in range(trials):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total_roll = d1 + d2
    if total_roll == 8:
        sum8 += 1
        if d1 == 3:
            sum8_and_first3 += 1
    if d1 == 3:
        first3 += 1

p_sum8 = sum8 / trials
p_sum8_given_first3 = sum(1 for _ in range(trials) if (random.randint(1, 6) == 3 and (random.randint(1, 6) + 3 == 8)))
# Recompute properly for reporting with a fresh simulation structure
sum8_given_first3_trials = 0
sum8_given_first3_count = 0
first3_and_sum8 = 0
sum8_total = 0
for _ in range(trials):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    s = d1 + d2
    if s == 8:
        sum8_total += 1
        if d1 == 3:
            first3_and_sum8 += 1
    if d1 == 3:
        sum8_given_first3_trials += 1
        if s == 8:
            sum8_given_first3_count += 1

p_sum8 = sum8_total / trials
p_sum8_given_first3 = sum8_given_first3_count / sum8_given_first3_trials
p_first3_given_sum8 = first3_and_sum8 / sum8_total
print(f"P(sum=8) ≈ {p_sum8:.4f}")
print(f"P(sum=8 | first die=3) ≈ {p_sum8_given_first3:.4f}")
print(f"P(first die=3 | sum=8) ≈ {p_first3_given_sum8:.4f}")
print(f"Check: P(A|B)P(B) ≈ {p_sum8_given_first3 * (sum8_given_first3_trials / trials):.4f}")
print(f"Check: P(B|A)P(A) ≈ {p_first3_given_sum8 * p_sum8:.4f}")


# LAB 5 - Challenge: Simpson's Paradox
print("\nLAB 5 - Challenge: Simpson's Paradox")
hospital_A_mild_treated, hospital_A_mild_survived = 800, 790
hospital_A_severe_treated, hospital_A_severe_survived = 200, 150
hospital_B_mild_treated, hospital_B_mild_survived = 100, 98
hospital_B_severe_treated, hospital_B_severe_survived = 900, 680

A_overall = (hospital_A_mild_survived + hospital_A_severe_survived) / (hospital_A_mild_treated + hospital_A_severe_treated)
B_overall = (hospital_B_mild_survived + hospital_B_severe_survived) / (hospital_B_mild_treated + hospital_B_severe_treated)
A_mild = hospital_A_mild_survived / hospital_A_mild_treated
B_mild = hospital_B_mild_survived / hospital_B_mild_treated
A_severe = hospital_A_severe_survived / hospital_A_severe_treated
B_severe = hospital_B_severe_survived / hospital_B_severe_treated
print(f"Hospital A overall survival = {A_overall:.4f}")
print(f"Hospital B overall survival = {B_overall:.4f}")
print(f"Mild cases: A={A_mild:.4f}, B={B_mild:.4f}")
print(f"Severe cases: A={A_severe:.4f}, B={B_severe:.4f}")
print("Paradox: A does better in both groups, but B treats far more severe cases, which lowers its overall rate.")


# ============================================================================
# LAB 6 - Bayesian Probability
# ============================================================================

# LAB 6 - Starter Code: Bayes' Theorem Function

def bayes(prior, likelihood_given_true, likelihood_given_false):
    """
    Apply Bayes' theorem.
    prior = P(H)
    likelihood_given_true = P(E|H)
    likelihood_given_false = P(E|H')
    Returns: posterior P(H|E)
    """
    p_evidence = (likelihood_given_true * prior + likelihood_given_false * (1 - prior))
    posterior = (likelihood_given_true * prior) / p_evidence
    return posterior


print("\nLAB 6 - Bayesian Probability")
prior = 0.01
sens = 0.95
false_pos = 0.10
posterior = bayes(prior, sens, false_pos)
print("=== Medical Test Example ===")
print(f"Prior P(disease) = {prior:.4f} ({prior*100:.1f}%)")
print(f"P(positive | disease) = {sens}")
print(f"P(positive | no disease) = {false_pos}")
print(f"Posterior P(disease | positive test) = {posterior:.4f} ({posterior*100:.1f}%)")


# LAB 6 - Starter Code: Sequential Bayesian Updating

def sequential_bayes(initial_prior, likelihood_true, likelihood_false, n_positive):
    """Apply Bayes n_positive times, each time using the posterior as new prior."""
    prior = initial_prior
    print(f"Start: Prior = {prior:.6f} ({prior*100:.3f}%)")
    for i in range(1, n_positive + 1):
        prior = bayes(prior, likelihood_true, likelihood_false)
        print(f"After test {i}: Prior = {prior:.6f} ({prior*100:.3f}%)")
    return prior


print("=== Sequential Testing: Same disease, 3 positive tests ===")
final = sequential_bayes(initial_prior=0.01, likelihood_true=0.95, likelihood_false=0.10, n_positive=3)
print(f"After 3 positive tests: {final*100:.1f}% chance of disease.")


# LAB 6 - Starter Code: Naive Bayes Spam Filter
P_spam = 0.30
P_ham = 0.70
word_probs = {
    "FREE": {"spam": 0.80, "ham": 0.05},
    "WINNER": {"spam": 0.70, "ham": 0.02},
    "meeting": {"spam": 0.05, "ham": 0.40},
    "report": {"spam": 0.10, "ham": 0.35},
    "URGENT": {"spam": 0.65, "ham": 0.03},
    "attached": {"spam": 0.20, "ham": 0.45},
}


def classify_email(words_in_email):
    """Naive Bayes: update prior for each word sequentially."""
    p = P_spam
    print(f"Starting prior P(spam) = {p:.4f}")
    for word in words_in_email:
        if word in word_probs:
            p = bayes(p, word_probs[word]["spam"], word_probs[word]["ham"])
            print(f' After seeing "{word:10s}": P(spam) = {p:.4f}')
    return p


print('=== Email 1: "FREE WINNER URGENT" ===')
p1 = classify_email(["FREE", "WINNER", "URGENT"])
print(f'Final verdict: {"SPAM" if p1 > 0.5 else "HAM"} ({p1*100:.1f}% spam)')
print('=== Email 2: "meeting report attached" ===')
p2 = classify_email(["meeting", "report", "attached"])
print(f'Final verdict: {"SPAM" if p2 > 0.5 else "HAM"} ({p2*100:.1f}% spam)')


# LAB 6 - Exercise 6A: Prior Sensitivity Analysis
print("\nLAB 6 - Exercise 6A: Prior Sensitivity Analysis")
priors = [0.001, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90]
print("Prior P(H) | Posterior P(H | positive test)")
for p in priors:
    post = bayes(p, 0.95, 0.10)
    print(f"{p:9.3f} | {post: .4f}")


# LAB 6 - Exercise 6B: Bayesian A/B Testing
print("\nLAB 6 - Exercise 6B: Bayesian A/B Testing")
random.seed(21)
true_b_rate = 0.07
prior_b_better = 0.50
for i in range(1, 1001):
    converted = random.random() < true_b_rate
    if converted:
        prior_b_better = bayes(prior_b_better, 0.07, 0.05)
    else:
        prior_b_better = bayes(prior_b_better, 1 - 0.07, 1 - 0.05)
    if i % 100 == 0:
        print(f"After {i} visitors: P(B converts at > 5%) = {prior_b_better*100:.2f}%")


# LAB 6 - Challenge: Full Naive Bayes Classifier from Scratch
print("\nLAB 6 - Challenge: Full Naive Bayes Classifier from Scratch")
training_emails = [
    ("spam", "FREE prize"),
    ("spam", "WINNER click"),
    ("spam", "URGENT money"),
    ("spam", "FREE cash"),
    ("spam", "click WIN"),
    ("ham", "meeting tomorrow"),
    ("ham", "project report"),
    ("ham", "lunch meeting"),
    ("ham", "call scheduled"),
    ("ham", "report done"),
]


def tokenize(text):
    return text.lower().split()


spam_words = []
ham_words = []
vocab = set()
for label, text in training_emails:
    words = tokenize(text)
    vocab.update(words)
    if label == "spam":
        spam_words.extend(words)
    else:
        ham_words.extend(words)

spam_counts = Counter(spam_words)
ham_counts = Counter(ham_words)
spam_total = len(spam_words)
ham_total = len(ham_words)
vocab_size = len(vocab)
prior_spam = sum(1 for label, _ in training_emails if label == "spam") / len(training_emails)
prior_ham = 1 - prior_spam


def word_likelihood(word, class_counts, class_total, vocab_size):
    return (class_counts[word] + 1) / (class_total + vocab_size)


def classify_naive_bayes(email_text):
    words = tokenize(email_text)
    log_spam = math.log(prior_spam)
    log_ham = math.log(prior_ham)
    for word in words:
        log_spam += math.log(word_likelihood(word, spam_counts, spam_total, vocab_size))
        log_ham += math.log(word_likelihood(word, ham_counts, ham_total, vocab_size))
    max_log = max(log_spam, log_ham)
    spam_score = math.exp(log_spam - max_log)
    ham_score = math.exp(log_ham - max_log)
    posterior_spam = spam_score / (spam_score + ham_score)
    label = "spam" if posterior_spam > 0.5 else "ham"
    return label, posterior_spam


for test_email in ["FREE money WIN", "project meeting tomorrow", "URGENT meeting"]:
    label, posterior_spam = classify_naive_bayes(test_email)
    print(f'Email: "{test_email}" -> {label.upper()} ({posterior_spam*100:.1f}% spam)')


