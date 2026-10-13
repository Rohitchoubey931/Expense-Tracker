# Expense Tracker (Python CLI)

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
