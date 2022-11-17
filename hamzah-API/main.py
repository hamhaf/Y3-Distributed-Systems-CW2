from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

# endpoint to get incomes
@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

#endpoint to post incomes
@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204