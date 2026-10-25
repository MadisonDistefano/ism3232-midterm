# ISM3232 Midterm: Harvest Table Catering

Madison Distefano
Class: ISM 3232, Business Application Development



## Project Notes & Reflection
*(Note: I initially started building a custom midterm project inspired by my job at LongHorn Steakhouse based on a misinterpretation of the Github Midterm instructions. Once I realized we were given a template in Canvas, I adapted and updated this repository with the correct project specifications, business rules, and test cases.)*



## What This Program Does
This program helps Harvest Table Catering figure out the costs and details for a list of eight different events. It calculates food prices, applies the right discounts and service fees based on how many people are attending, and checks whether an event needs a manager's sign-off or an extra chef. Finally, it prints out a clear, line-by-line report for each event along with a helpful summary for the owner.



## Business Rules
1. **Food Cost:** Calculated as `price_per_guest × number_of_guests`.
2. **Discount Tiers:**
   - **Fewer than 25 guests:** 0% discount
   - **25 to 99 guests:** 5% discount
   - **100 or more guests:** 12% discount *(Nonprofits only)*
3. **Nonprofit Rule:** The 12% discount applies strictly to registered nonprofits. Any other event with 100 or more guests receives the standard 5% discount.
4. **Service Fee:** A $75 service fee is added if the discounted food cost is $500 or less.
5. **Manager Sign-Off:** Required if the final event total exceeds $2,500.
6. **Second Chef Requirement:** Required if the event has more than 80 guests **OR** if the event total is $3,000 or more.

1. **Subtotal:** the plate price times the number of plates.
2. **Discount:** fewer than 5 plates get no discount. 5 to 9 plates get 15% off.
   10 or more plates get 20% off, but only if it is a birthday party. A group of
   10 or more that is not a birthday party gets 15% off.
3. **Small order fee:** if the cost after the discount is under $40.00, a $5.00
   fee is added.
4. **Order total:** the discounted cost plus the fee, plus 7.5% sales tax on
   that amount (6% Florida plus 1.5% Hillsborough County). Everything is rounded
   to the nearest cent.
5. **Big order:** any order with a total of $100.00 or more



## How to Run


###  Using Git
1. Open the terminal and clone the repository:
   git clone https://github.com/MadisonDistefano/ism3232-midterm.git
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
   
## How To Test

ruff format --check .
ruff check .
pytest -v

## Files In This Repository

- `business_rules.py`: Contains the eight core functions implementing the business logic.
- `main.py`: Iterates through the eight events, executes calculations, and displays the formatted report and summary.
- `commands.md`: Record of terminal commands executed and their output.
- `README.md`: Project documentation and overview.
- `requirements.txt`: Project dependencies (`pytest` and `ruff`).
- `.gitignore`: Specifies files ignored by Git (e.g., `.venv/`, `__pycache__/`).
- `tests/__init__.py`: Package initialization file allowing `pytest` to discover modules.
- `tests/test_business_rules.py`: Test suite containing 27 unit tests.


## AI Use statement: I did not use AI
