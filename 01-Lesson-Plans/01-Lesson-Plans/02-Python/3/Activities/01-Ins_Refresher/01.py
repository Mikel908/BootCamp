from re import X


customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]
def create_greeting (first_name, last_name, revenue)
    greeting =" "
    if revenue > 3000:
        greeting = f"Hi (first_name ) (lastname)"