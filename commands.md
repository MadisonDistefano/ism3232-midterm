## ISM3232 Midterm: Harvest Table Catering

# Create
cd ~/ism3232
mkdir ism3232-midterm && cd ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
printf '.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n.DS_Store\n' > .gitignore
touch business_rules.py main.py commands.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
git init && git branch -M main
git remote add origin https://github.com/MadisonDistefano/ism3232-midterm.git
git add . && git commit -m 'Initial project structure and setup' && git push -u origin main

# run it and check it
python3 main.py
ruff format . && ruff check . && python3 -m pytest -v

# commit each part
git add business_rules.py && git commit -m 'Add business rules functions'

git add main.py && git commit -m 'Add main.py order report'

git add tests/test_business_rules.py && git commit -m 'Add pytest tests'

# I forgot to add my README earlier, so I added it here
touch README.md
git add README.md && git commit -m 'Add README'
git push
git pull

# tools and commit for this file
git add commands.md && git commit -m 'Add commands.md with terminal output' && git push

# Virtual Enviornment 
Users/maddiy/ism3232/ism3232-midterm/.venv/bin/python3
(.venv) maddiy@Madisons-MacBook-Air-138 ism3232-midterm % 

The output shows that my virtual environment is active because Python executable is located inside the .venv directory within my ism3232-midterm project. 

# Project Structure
tree -L 2
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
The .venv folder is on my computer but not in my GitHub repository because it contains the local Python environment and dependencies, which are excluded from version control through .gitignore.

## rg 'def '
The business_rules.py file defines 8 functions, and tests/test_business_rules.py defines 27 test functions. All 27 tests pass, as confirmed by pytest.

## rg -l 'print'
main.py
README.md
commands.md
The Python file that prints output is main.py, which displays the program's results to the user. business_rules.py is not listed because it contains the business logic and does not use print().

## git log --oneline
At this point, my repository has 3 commits documenting the progress of my midterm project.
(This is due to the fact that I had commited work that I did in error and now I will commit the correct work)