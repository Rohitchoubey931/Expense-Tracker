Exp = {
    "Month": ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"],
    "Cat_Wise": {
        "Travel": [],
        "Food & Groceries": [],
        "Education": [],
        "Outings": [],
        "Miscellaneous": []
    }
}

codes = {"T": "Travel", "FG": "Food & Groceries", "E": "Education",
         "O": "Outings", "M": "Miscellaneous"}

while True:   # outer loop: repeats the whole flow

    print("\nExpenses of the Month:", ", ".join(Exp["Month"]))
    for i in range(len(Exp["Month"])):
        print("For", Exp["Month"][i], "month Enter:", i + 1)

    while True:
        try:
            choice = int(input("Type for a month: "))

        except ValueError:
            print("Invalid Input")
            continue
        if 1 <= choice <= 12:
            month = Exp["Month"][choice - 1]
            print("You selected", month)
            break
        else:
            print("Invalid Input, Please enter again")

    print("\nAdding for which category?")
    print("Type T for Travel\nType FG for Food & Groceries\nType E for Education\nType O for Outings\nType M for Miscellaneous")

    while True:
        cat_choice = input("Type for the category: ").upper()

        if cat_choice in codes:
            category = codes[cat_choice]
            amount = float(input("Enter amount for " + category + ": "))
            Exp["Cat_Wise"][category].append(amount)
            print("Added", amount, "to", category)
            break
        else:
            print("Invalid category, please type again")

    while True:
        more = input("Do you want to add more expenses? (yes/no): ").lower()
        if more in ("yes", "no"):
            break
        print("Please type yes or no")

    if more == "no":   # now outside the yes/no loop
        break

print("\nThank you! Final expenses:")
for types in Exp["Cat_Wise"]:
    print(types, ":", Exp["Cat_Wise"][types])