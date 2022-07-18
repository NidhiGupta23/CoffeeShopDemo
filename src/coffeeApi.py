# File focuses on get, post, update and delete coffee details with rest-apis using flask
# create and activate virtual environment 
# { python -m venv .venv
#   set FLASK_APP=coffeeApi.py
#   flask run
#  }
# use postman for post and delete methods


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class CoffeeDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cName = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(150))
    price = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f'{self.cName} - {self.description} - {self.price}'

        

@app.route('/')
def index():
    return ('Welcome here to our coffee shop')
 
@app.route('/coffeeDetails', methods=['GET'])
def get_coffeeDetails():
    coffeeD = CoffeeDetails.query.all()
    output = []
    for coffee in coffeeD:
        details = {'id': coffee.id, 'cName': coffee.cName, 'description': coffee.description, 'price': coffee.price}
        output.append(details)
    
    return {"coffee" : output}

@app.route('/coffeeDetails', methods=['POST'])
def add_coffeeDetails():
    coffeeD = CoffeeDetails(cName=request.json['cName'], description=request.json['description'], price=request.json['price'])
    db.session.add(coffeeD)
    db.session.commit()
    return {'id': coffeeD.id}

@app.route('/coffeeDetails/<id>', methods=['PUT'])
def update_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get(id)
    coffeeD.cName = request.json['cName']
    coffeeD.description = request.json['description']
    coffeeD.price = request.json['price']
    db.session.commit()
    return {'id': coffeeD.id, 'cName': coffeeD.cName, 'description': coffeeD.description, 'price': coffeeD.price}


@app.route('/coffeeDetails/<id>', methods=['DELETE'])
def delete_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get(id)    
    if coffeeD is None:
        return {'error': 'coffee does not exists'}
    db.session.delete(coffeeD)
    db.session.commit()
    return {'message': 'deletion successful'}

@app.route('/coffeeDetails/<id>')
def get_coffeeDetail(id):
    coffeeD = CoffeeDetails.query.get_or_404(id)
    return {'id': coffeeD.id, 'cName': coffeeD.cName, 'description': coffeeD.description, 'price': coffeeD.price}
