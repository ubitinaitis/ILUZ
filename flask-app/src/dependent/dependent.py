from flask import Blueprint, jsonify, make_response, request
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


# post requests to add funds to a particular budget for independent and dependent
# (ex. post request for an independent to add that they just spent x dollars on groceries)
