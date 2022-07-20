# File focuses on get, post, update and delete coffee details with rest-apis using flask
# create and activate virtual environment 
# { python -m venv .venv
#   set FLASK_APP=coffeeApi.py
#   flask run
#  }
# use postman for post and delete methods


from enum import unique
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/CoffeeData.db'
app.config['SQLALCHEMY_BINDS'] = {'customer' : 'sqlite:///../database/CustomersData.db'}

db = SQLAlchemy(app)

# For handling database
class CoffeeDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cName = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(150))
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.cName} - {self.description} - {self.price}'
        
class CustomersData(db.Model):
    __bind_key__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True)
    pwd = db.Column(db.String(50))
    credit = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.fname}  {self.lname}  '


@app.route('/')
def index():
    return ('Welcome here to our coffee shop')

######################################################################################################################
                       ########## IMPLEMENTING REST API FOR PRODUCT CUSTOMER ##########

@app.route('/customDetails', methods=['GET'])
def get_customerDetails():
    customers = CustomersData.query.all()
    output = []
    for customer in customers:
        details = {'id': customer.id, 'fname': customer.fname, 'lname': customer.lname, 'email': customer.email, 'credit': customer.credit}
        output.append(details)    
    return {"Customers" : output}


@app.route('/customDetails', methods=['POST'])
def add_customerDetails():
    customer = CustomersData(fname=request.json['fname'], lname=request.json['lname'], email=request.json['email'], pwd=request.json['pwd'], credit=request.json['credit'])
    db.session.add(customer)
    db.session.commit()
    return {'id': customer.id}

@app.route('/customDetails/<id>', methods=['PUT'])
def update_customerDetail(id):
    customer = CustomersData.query.get(id)
    customer.fname = request.json['fname']
    customer.lname = request.json['lname']
    customer.email = request.json['email']
    customer.pwd = request.json['pwd']
    customer.creddit = request.json['credit']
    db.session.commit()
    return {'id': customer.id, 'fname': customer.fname, 'lname': customer.lname, 'email': customer.email, 'credit': customer.credit}

# delete a particular customer
@app.route('/customDetails/<id>', methods=['DELETE'])
def delete_customerDetail(id):
    customer = CustomersData.query.get(id)    
    if customer is None:
        return {'error': 'customer does not exists'}
    db.session.delete(customer)
    db.session.commit()
    return {'message': 'deletion successful'}

# display details of specific customer
@app.route('/customDetails/<id>')
def get_customDetail(id):
    customer = CustomersData.query.get_or_404(id)
    return {'id': customer.id, 'fname': customer.fname, 'lname': customer.lname, 'email': customer.email, 'credit': customer.credit}

######################################################################################################################
                       ########## IMPLEMENTING REST API FOR PRODUCT COFFEE ##########

@app.route('/coffeeDetails', methods=['GET'])
def get_coffeeDetails():
    coffeeD = CoffeeDetails.query.all()
    output = []
    for coffee in coffeeD:
        details = {'id': coffee.id, 'cName': coffee.cName, 'description': coffee.description, 'price': coffee.price}
        output.append(details)    
    return {"coffee" : output}

# add coffee details into the database
@app.route('/coffeeDetails', methods=['POST'])
def add_coffeeDetails():
    coffeeD = CoffeeDetails(cName=request.json['cName'], description=request.json['description'], price=request.json['price'])
    db.session.add(coffeeD)
    db.session.commit()
    return {'id': coffeeD.id}

# update the details of particular coffee
@app.route('/coffeeDetails/<id>', methods=['PUT'])
def update_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get(id)
    coffeeD.cName = request.json['cName']
    coffeeD.description = request.json['description']
    coffeeD.price = request.json['price']
    db.session.commit()
    return {'id': coffeeD.id, 'cName': coffeeD.cName, 'description': coffeeD.description, 'price': coffeeD.price}

# delete a particular coffee
@app.route('/coffeeDetails/<id>', methods=['DELETE'])
def delete_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get(id)    
    if coffeeD is None:
        return {'error': 'coffee does not exists'}
    db.session.delete(coffeeD)
    db.session.commit()
    return {'message': 'deletion successful'}

# display details of specific coffee
@app.route('/coffeeDetails/<id>')
def get_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get_or_404(id)
    return {'id': coffeeD.id, 'cName': coffeeD.cName, 'description': coffeeD.description, 'price': coffeeD.price}
