# ---------- DATA ----------
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

codes = {"T": "Travel", "FG": "Food & Groceries", "E": "Education",
         "O": "Outings", "M": "Miscellaneous"}

# Exp["March"]["Travel"] -> list of travel amounts for March
Exp = {m: {cat: [] for cat in codes.values()} for m in months}


# ---------- FUNCTIONS ----------
def get_month():
    """Show the month menu, keep asking until valid, return the month name."""
    print("\nSelect a month:")
    for i in range(len(months)):
        print(i + 1, "-", months[i])

    while True:
        try:
            choice = int(input("Type a month number (1-12): "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue

        if 1 <= choice <= 12:
            print("You selected", months[choice - 1])
            return months[choice - 1]
        print("Invalid input, please enter again")


def get_category():
    """Show category codes, keep asking until valid, return the category name."""
    print("\nAdding for which category?")
    for code, name in codes.items():
        print("Type", code, "for", name)

    while True:
        cat_choice = input("Type for the category: ").upper()
        if cat_choice in codes:
            return codes[cat_choice]
        print("Invalid category, please type again")


def get_amount(category):
    """Ask for an amount, keep asking until it is a positive number, return it."""
    while True:
        try:
            amount = float(input("Enter amount for " + category + ": "))
        except ValueError:
            print("Please enter a number")
            continue

        if amount <= 0:
            print("Amount must be greater than 0")
            continue
        return amount


def ask_yes_no(question):
    """Ask a yes/no question. Return True for yes, False for no."""
    while True:
        answer = input(question + " (yes/no): ").lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("Please type yes or no")


def add_expense():
    """Collect month, category and amount, then store the expense."""
    month = get_month()
    category = get_category()
    amount = get_amount(category)
    Exp[month][category].append(amount)
    print("Added", amount, "to", category, "for", month)


def show_summary():
    """Print totals for every month that has at least one expense."""
    print("\nThank you! Final expenses:")
    grand_total = 0
    for m in months:
        month_total = sum(sum(v) for v in Exp[m].values())
        if month_total > 0:
            print("\n" + m, "- Total:", month_total)
            for cat, amounts in Exp[m].items():
                print("  ", cat, ":", amounts, "=", sum(amounts))
            grand_total += month_total
    print("\nGrand total:", grand_total)


def main():
    """Run the whole program."""
    while True:
        add_expense()
        if not ask_yes_no("Do you want to add more expenses?"):
            break
    show_summary()


main()