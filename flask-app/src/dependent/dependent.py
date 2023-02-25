from flask import Blueprint, jsonify, make_response, request, current_app
from src import db

dep_blueprint = Blueprint('dep_blueprint', __name__)

# get requests to display the current funds
@dep_blueprint.route('/dep/<userID>', methods=['GET'])
def get_dependents(userID):
    cursor = db.get_db().cursor()

    cursor.execute('SELECT i.hasBalance FROM Dependent d WHERE d.userID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    data = cursor.fetchall()
    for row in data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get request for budget

@dep_blueprint.route('/dep', methods=['GET'])
def get_budget(userID):
    cursor = db.get_db().cursor()

    cursor.execute('SELECT b.category, bal.currentFunds FROM Dependent d JOIN Balance bal\
     ON d.hasBalance = bal.balanceID JOIN Budget b ON b.budgetID = bal.balanceID\
      WHERE d.userID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    data = cursor.fetchall()
    for row in data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
