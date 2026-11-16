# Name: Tingqi FENG
# Group: B
# Q1: What goes in?
# I read scenarios_B.csv, which uses semicolons and has 14 columns.
# Num identifies the scenario, and Situation describes the event.
# Each option has Choice, Money, Buzz and Reaction columns.
# Money changes the budget, and Buzz changes the reputation.
# I convert number strings to integers and handle Unicode minus signs.

# Q2: What happens each day?
# Show the day, budget, reputation, situation and three options.
# Ask for a choice until the player enters A, B or C.
# Apply the choice and show its feedback.
# Keep reputation at a maximum of 100.
# Record the move and stop if either gauge is zero or below.

# Q3: What comes out?
# Show the final budget, reputation and title.
# If fired, show the reason. Otherwise, show the final score.
# Show the best and worst moves based on reputation changes.
# Append name, budget, reputation, title and date to results.csv.

# Q4: What could go wrong?
# Invalid choices: keep asking until the input is valid.
# Empty name: ask the player to enter a name again.
# Missing scenario file: display an error message.
# Invalid CSV numbers or columns: display an error message.
# Budget or reputation at zero or below: end the game immediately.
# Failure to save results: display a warning.

# Feature: Difficulty selection.
# Easy starts with 15000 EUR, and hard starts with 6000 EUR.
# I chose this feature to offer different levels of challenge.
import csv
import random
from datetime import datetime

# Convert text values to integers, including Unicode minus signs.
def to_integer(value):
    return int(value.strip().replace("−", "-"))


# Load the scenarios and store each option as a tuple.
def load_scenarios():
    scenarios = []

    with open("scenarios_B.csv", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            options = {}

            for letter in ("A", "B", "C"):
                options[letter] = (
                    row[f"{letter}_Choice"],
                    to_integer(row[f"{letter}_Money"]),
                    to_integer(row[f"{letter}_Buzz"]),
                    row[f"{letter}_Reaction"]
                )

            scenario = {
                "situation": row["Situation"],
                "options": options
            }
            scenarios.append(scenario)

    return scenarios


# Keep asking until the player enters A, B or C.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()

        if choice in ("A", "B", "C"):
            return choice

        print("Please type A, B or C.")


# Apply the selected option and return the two updated gauges.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option

    budget += budget_change
    reputation = min(100, reputation + reputation_change)

    print(feedback)
    print(
        f"Budget {budget_change:+d} EUR, "
        f"Reputation {reputation_change:+d}"
    )

    return budget, reputation

# Append one game result and add a header if the file is empty.
def save_result(name, budget, reputation, title):
    with open("results.csv", "a+", encoding="utf-8", newline="") as file:
        file.seek(0)
        is_empty = file.read(1) == ""

        writer = csv.writer(file)

        if is_empty:
            writer.writerow(
                ["name", "budget", "reputation", "title", "date"]
            )

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            datetime.now().isoformat(timespec="seconds")
        ])

    print("Saved in results.csv")
# Test one day before adding the full ten-day game.
# Play ten different scenarios and stop if either gauge reaches zero.
def main():
    scenarios = load_scenarios()

    if len(scenarios) < 10:
        print("You need at least 10 scenarios to play.")
        return

    name = input("Your name: ").strip()
    while not name:
        name = input("Please enter your name: ").strip()

        # Let the player choose the starting budget.
    difficulty = input("Choose difficulty (easy/hard): ").strip().lower()

    while difficulty not in ("easy", "hard"):
        difficulty = input("Please type easy or hard: ").strip().lower()

    if difficulty == "easy":
        budget = 15000
    else:
        budget = 6000

    reputation = 50
    history = []

    random.shuffle(scenarios)

    for day, scenario in enumerate(scenarios[:10], start=1):
        print(f"\n--- Day {day} ---")
        print(
            f"[Budget: {budget} EUR | "
            f"Reputation: {reputation}/100]"
        )
        print(scenario["situation"])

        for letter in ("A", "B", "C"):
            option = scenario["options"][letter]
            print(f"{letter}: {option[0]}")

        choice = ask_choice()
        selected_option = scenario["options"][choice]

        budget, reputation = apply_choice(
            budget, reputation, selected_option
        )

        # Record the reputation impact, day and chosen option.
        text, money_change, buzz_change, feedback = selected_option
        history.append((buzz_change, day, text))

        if budget <= 0 or reputation <= 0:
            print("\nYou are fired!")

            if budget <= 0:
                print("Reason: your budget reached zero or below.")

            if reputation <= 0:
                print("Reason: your reputation reached zero or below.")

            break

    # Calculate a title only when the player survives.
    if budget > 0 and reputation > 0:
        score = reputation + budget // 200

        if score < 95:
            title = "Eternal Intern"
        elif score < 120:
            title = "Growth Hacker"
        elif score < 140:
            title = "CMO Material"
        else:
            title = "Viral Legend"

        print("\nQuarter survived!")
        print(f"Final score: {score}")
    else:
        title = "Fired"

    # Compare the history tuples to find the best and worst moves.
    best_change, best_day, best_text = max(history)
    worst_change, worst_day, worst_text = min(history)

    print(f"\n{name}, your title: {title}")
    print(f"Budget left: {budget} EUR")
    print(f"Reputation: {reputation}/100")
    print(
        f"Best move: day {best_day}, "
        f"{best_text} ({best_change:+d})"
    )
    print(
        f"Worst move: day {worst_day}, "
        f"{worst_text} ({worst_change:+d})"
    )

    # Save the result whether the player survived or was fired.
    try:
        save_result(name, budget, reputation, title)
    except OSError as error:
        print("Could not save the result:", error)


# Show a helpful message if the scenario file cannot be loaded.
if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print("Cannot find scenarios_B.csv. Put it beside this Python file.")
    except (KeyError, ValueError, TypeError, csv.Error) as error:
        print("Please check the CSV columns and number format:", error)
    except (EOFError, KeyboardInterrupt):
        print("\nGame stopped.")