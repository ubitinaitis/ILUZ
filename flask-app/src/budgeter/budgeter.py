from flask import Blueprint, jsonify, make_response, request, current_app
from src import db

budgeter_blueprint = Blueprint('budget_blueprint', __name__)


# Get all the users that the budget manager supervises
@budgeter_blueprint.route('/budget/<emp>', methods=['GET'])
def get_dependents(emp):
    cursor = db.get_db().cursor()
    # Change the SQL here to the users being overseen by the budget manager
    cursor.execute('SELECT userID, email, lastName FROM Individual\
     JOIN BudgetCoach on Individual.customerRepID = BudgetCoach.employeeID\
      WHERE BudgetCoach.employeeID = {0}'.format(emp))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get request to see a general overview of all the data for all the clients they work with

# (so it would show each “family” with their general funds)

# get request for manager to click into a particular family to see  details about their funds
@budgeter_blueprint.route('/budget/<user1>', methods=['GET'])
def get_userinfo(user1):

    cursor = db.get_db().cursor()
    # Change the SQL here to the users being overseen by the budget manager
    cursor.execute('SELECT userID, email, firstName, lastName, hasBalance\
     FROM Individual WHERE Individual.customerRepID = {0}'.format(user1))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#POST request

@budgeter_blueprint.route('/budgeter', methods=['POST'])
def add_userinfo():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()

    userID = request.form['userID']
    email = request.form['email'] 
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    hasBalance = request.form['hasBalance']
    query = f'INSERT INTO BudgetCoach(userID, email, firstName, lastName, hasBalance) VALUES(\"{userID}\", \"{email}\", \"{firstName}\", \"{lastName}\", \"{hasBalance}\")' 
    cursor.execute(query)
    db.get_db().commit()
    return "Yippee!!!"


