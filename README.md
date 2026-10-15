# Expense Tracker (Python Using Dictionaries)

A simple command-line expense tracker built with core Python. Pick a month, choose a category, enter an amount, and get a month-wise summary of your spending at the end.

## Features

- Select any of the 12 months from a numbered menu
- Add expenses under 5 categories: Travel, Food & Groceries, Education, Outings, Miscellaneous
- Add multiple expenses in one session
- Input validation for invalid months, categories, and yes/no answers
- Final summary showing each category's entries and totals, per month

## Concepts Used

- Dictionaries and nested dictionaries
- Lists
- while and `fo loops
- input() and type conversion
- try / except for error handling

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run


git clone https://github.com/<rohitchoubey931>/expense-tracker.git
cd expense-tracker
python expense_tracker.py


## Example Session

Type for a month: 3
You selected March

Adding for which category?
Type T for Travel
Type FG for Food & Groceries
Type E for Education
Type O for Outings
Type M for Miscellaneous
Type for the category: fg
Enter amount for Food & Groceries: 450
Added 450.0 to Food & Groceries
Do you want to add more expenses? (yes/no): no

March - Total: 450.0
   Food & Groceries : [450.0] = 450.0


## Project Structure

expense-tracker/
├── expense_tracker.py
└── README.md


## Future Improvements

- [ ] Save data to a file or SQLite so it persists between runs
- [ ] View the summary of a single month
- [ ] Edit or delete an expense
- [ ] Export to CSV
- [ ] Charts with pandas and matplotlib
- [ ] Web version using Flask

## Author

Rohit Choubey

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
# 💰 Monthly Expense Tracker (Python CLI)

A simple command-line application built in Python to record daily expenses month-wise and category-wise, and to view a clear summary of total spending at the end.

This project is built using only core Python (functions, dictionaries, lists, loops, and input validation). No external libraries are needed.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Data Structure](#-data-structure)
- [Code Explanation](#-code-explanation)
- [How to Run](#-how-to-run)
- [Sample Output](#-sample-output)
- [Concepts Used](#-concepts-used)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## ✨ Features

- Add expenses for any of the **12 months**
- Five expense categories: **Travel, Food & Groceries, Education, Outings, Miscellaneous**
- Add **multiple expenses** in a single run
- **Input validation** everywhere: invalid month, category, or amount never crashes the program, it simply asks again
- Category codes are **case-insensitive** (`t` and `T` both work)
- Final summary showing:
  - Total spending per month
  - Category-wise breakdown with every individual amount
  - Grand total across all months
- Months with no expenses are skipped in the summary

---

## 🛠 Tech Stack

| Item | Details |
|------|---------|
| Language | Python 3 |
| Libraries | None (standard Python only) |
| Interface | Command line / terminal |

---

## ⚙️ How It Works

1. The program shows a menu of months and asks you to pick one (1 to 12).
2. It then shows the category codes and asks you to choose a category.
3. It asks for the amount spent in that category.
4. The amount is stored under the selected month and category.
5. The program asks, *"Do you want to add more expenses?"*
   - **yes** goes back to step 1
   - **no** shows the final summary and ends
6. The summary prints month-wise totals, category-wise breakdowns, and the grand total.

**Category codes:**

| Code | Category |
|------|----------|
| `T` | Travel |
| `FG` | Food & Groceries |
| `E` | Education |
| `O` | Outings |
| `M` | Miscellaneous |

---

## 🗂 Data Structure

All expenses are stored in a **nested dictionary** named `Exp`:

```python
Exp = {m: {cat: [] for cat in codes.values()} for m in months}
```

This creates a structure like:

```python
Exp = {
    "January":  {"Travel": [], "Food & Groceries": [], "Education": [], "Outings": [], "Miscellaneous": []},
    "February": {"Travel": [], "Food & Groceries": [], ...},
    ...
}
```

So `Exp["March"]["Travel"]` gives a **list of all travel expenses entered for March**, for example `[250.0, 120.0]`.

**Why this design?**
- A dictionary lets you look up data directly by month and category name.
- A list for each category lets you store *multiple* expenses and still calculate totals easily with `sum()`.
- A dictionary comprehension builds the whole structure in one line, so there is no repeated code.

---

## 🧩 Code Explanation

The program is divided into small functions, each with one clear job.

### `get_month()`
Displays the numbered list of months and keeps asking until the user enters a valid number from 1 to 12. It uses `try/except` to handle non-numeric input (like letters) and returns the month name.

### `get_category()`
Displays the category codes and keeps asking until a valid code is entered. The input is converted to uppercase with `.upper()`, so lowercase input also works. Returns the full category name.

### `get_amount(category)`
Asks for the amount for the chosen category. It keeps asking until the value is a number **greater than 0**. Letters and zero or negative values are rejected with a helpful message.

### `ask_yes_no(question)`
A reusable helper that asks a yes/no question and only accepts `yes` or `no`. Returns `True` for yes and `False` for no.

### `add_expense()`
Combines the three functions above. It collects the month, category, and amount, then stores the amount in the `Exp` dictionary using `.append()`.

### `show_summary()`
Loops through all months, calculates each month's total using `sum()`, and prints only the months that have expenses. For each month it also prints the category-wise amounts and their totals. It finally prints the grand total.

### `main()`
Controls the program flow. It keeps calling `add_expense()` until the user chooses not to add more, then calls `show_summary()`.

---

## ▶️ How to Run

**1. Make sure Python 3 is installed:**

```bash
python --version
```

(On some systems, use `python3` instead of `python`.)

**2. Clone this repository:**

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

**3. Run the program:**

```bash
python expense_tracker.py
```

(Replace `expense_tracker.py` with your actual file name.)

---

## 🖥 Sample Output

```
Select a month:
1 - January
2 - February
3 - March
...
12 - December
Type a month number (1-12): 3
You selected March

Adding for which category?
Type T for Travel
Type FG for Food & Groceries
Type E for Education
Type O for Outings
Type M for Miscellaneous
Type for the category: t
Enter amount for Travel: 250
Added 250.0 to Travel for March
Do you want to add more expenses? (yes/no): yes

... (second entry: March, FG, 1200) ...

Do you want to add more expenses? (yes/no): no

Thank you! Final expenses:

March - Total: 1450.0
   Travel : [250.0] = 250.0
   Food & Groceries : [1200.0] = 1200.0
   Education : [] = 0
   Outings : [] = 0
   Miscellaneous : [] = 0

Grand total: 1450.0
```

---

## 📚 Concepts Used

- Functions and docstrings
- Dictionaries and nested dictionaries
- Dictionary comprehension
- Lists and `.append()`
- `for` and `while` loops
- Exception handling (`try / except ValueError`)
- Input validation
- String methods (`.upper()`, `.lower()`)
- Built-in functions (`sum()`, `len()`, `range()`)
- Modular, reusable code design

---

## ⚠️ Limitations

- Data is stored **in memory only**, so everything is lost when the program closes.
- No option to edit or delete an expense once added.
- Command-line only (no graphical interface).

---

## 🚀 Future Improvements

- Save and load expenses using a **CSV or JSON file**
- Store data in a **MySQL database**
- Add options to **edit or delete** expenses
- Show **charts** (monthly spending, category share) using Matplotlib
- Analyse spending with **Pandas** (highest-spending month, category averages)
- Add a **budget limit** with an overspending warning
- Build a web version using **Flask** or **FastAPI**

---

## 👤 Author

**Rohit Choubey**
MCA (2026) | Python | SQL | Flask | FastAPI

- GitHub: [your-github-link]
- LinkedIn: [your-linkedin-link]

---

⭐ If you found this project helpful, feel free to star the repository!
