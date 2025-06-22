# Coffee Machine CLI Project

Welcome to **Coffee Machine** — a command-line coffee vending machine simulation built in Python.  
This project simulates a simple coffee shop experience where the machine accepts coins, checks resources, and brews your favorite drinks like a true desi frown barista.

## 🚀 Features

- Order options:
  - `espresso`
  - `latte`
  - `cappuccino`
- Ingredient check before preparing drink
- Accepts coins:
  - quarters, dimes, nickles, and pennies
- Handles:
  - Change
  - Refunds
- Tracks profit in real-time
- `report` command to check current status
- `off` command to turn off the machine


##  How It Works

1. User selects a drink (espresso, latte, or cappuccino)
2. Machine verifies if resources (water, milk, coffee) are sufficient
3. Accepts coin input from the user
4. Compares inserted amount to drink cost
5. Returns change or refund based on amount
6. Updates resources and logs profit

##  Sample Run

```bash
Kya lega bro : latte/cappuccino/espresso? (off/report bhi likh)

👉 latte
☕ Tera order:
 - water: 200
 - milk: 150
 - coffee: 24
💸 Cost: $2.5
Kitne quarters? (1 quarters = 0.25): 10
Kitne dimes? (1 dimes = 0.1): 0
Kitne nickles? (1 nickles = 0.05): 0
Kitne pennies? (1 pennies = 0.01): 0
Tune total diya: $2.5
latte ban gaya bro ☕✅
Bacha hua resource: {'water': 800, 'milk': 650, 'coffee': 126}
💰 Total kamaya abhi tak: $2.5
````

## How to Run

> Make sure you have **Python 3.x** installed.

```bash
python coffee_machine.py
```


## Will Work this out in , atm it's just a model

* Add a GUI using Tkinter or Streamlit
* Add admin password for access to reports and refills
* Refill command to top-up ingredients
* Sales tracker per drink
* Export daily reports to file (CSV/JSON)



