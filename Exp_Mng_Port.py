Exp = {
    "Month": ["Jan", "Feb", "Mar"],
    "Category": ["Travel", "Food", "Housing", "Education"],
    "Cat_Wise": {
        "Travel": [],
        "Food": [],
        "Housing": [],
        "Education": []
    }
}

codes = {"T": "Travel", "F": "Food", "H": "Housing", "E": "Education"}

print("Expenses of the Month:", ", ".join(Exp["Month"]))
print("For Jan type 1\nFor Feb type 2\nFor Mar type 3")

choice = int(input("Type for a month: "))

if 1 <= choice <= 3:
    month = Exp["Month"][choice - 1]
    print("You selected", month)

    print("Adding for which category?")
    print("Type T for Travel\nType F for Food\nType H for Housing\nType E for Education")

    cat_choice = input("Type for the category: ").upper()

    if cat_choice in codes:
        category = codes[cat_choice]
        amount = float(input("Enter amount for " + category + ": "))
        Exp["Cat_Wise"][category].append(amount)
        print("Added", amount, "to", category)
        print(Exp["Cat_Wise"])
    else:
        print("Invalid category")
else:
    print("Invalid month")

    

