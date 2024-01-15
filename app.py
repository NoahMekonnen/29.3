"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, flash, session,jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Godalone1."
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()

@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    json_cupcakes = [{'id':cupcake.id,'flavor': cupcake.flavor, 'size':cupcake.size, 'rating': cupcake.rating, 'image':cupcake.image} 
                     for cupcake in cupcakes]
    return jsonify(cupcakes=json_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    json_cupcake = {'id':cupcake.id, 'flavor': cupcake.flavor, 'size':cupcake.size, 'rating': cupcake.rating, 'image':cupcake.image}
    return jsonify({'cupcake':json_cupcake})

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    res = request.json
    cupcake = Cupcake(flavor=res['flavor'], size=res['size'], rating=res['rating'], image=res['image'])

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify({'cupcake':{
        'id':cupcake.id, 
        'flavor': cupcake.flavor,
        'size':cupcake.size,
        'rating': cupcake.rating,
        'image':cupcake.image
    }}),201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Updates all of cupcake"""
    res = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = res.get('flavor',cupcake.flavor)
    cupcake.size = res.get('size',cupcake.size)
    cupcake.rating = res.get('rating',cupcake.rating)
    cupcake.image = res.get('image',cupcake.image)

    db.session.commit()

    return jsonify({
        'id':cupcake.id, 
        'flavor': cupcake.flavor,
        'size':cupcake.size,
        'rating': cupcake.rating,
        'image':cupcake.image
    })

@app.route('/api/cupcakes/<int:cupcake_id>',methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    Cupcake.query.filter_by(id=cupcake_id).delete()
    db.session.commit()
    return jsonify({'message':'Deleted'})

@app.route('/')
def home():
    return render_template('home.html')
