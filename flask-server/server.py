import csv
from flask import Flask

app = Flask(__name__)

CSV_FILE = "creditcards.csv"

def read_credit_cards_from_csv(csv_file):
    credit_cards = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        for row in reader:
            credit_card = row[0] + " " + row[1]  # Combine column 1 and column 2
            credit_cards.append(credit_card)
    return credit_cards

@app.route("/members")
def members():
    return {"members" : ["Member1", "Member2", "Member3"]}

@app.route("/creditcards")
def creditcards():
    credit_cards = read_credit_cards_from_csv(CSV_FILE)
    return {"creditcards": credit_cards}

if __name__ == "__main__":
    app.run(debug=True)
    