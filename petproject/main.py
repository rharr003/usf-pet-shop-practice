from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
from models import Pet, connect_app, db
from forms import NewPetForm


app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rharr003:Dissidia1!@127.0.0.1:5432/petshoppractice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'Secret'

connect_app(app)


@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = NewPetForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
            db.session.add(new_pet)
            db.session.commit()
            return redirect('/')
        return render_template('add.html', form=form)
    return render_template('add.html', form=form)

@app.route('/<int:pet_id>')
def pet_detail(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet.html', pet=pet)

@app.route('/edit/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = NewPetForm(name=pet.name, age=pet.age, species=pet.species, available=pet.available, notes=pet.notes,
                      photo_url=pet.photo_url)
    if request.method == 'POST':
        pet.name = form.name.data
        pet.age = form.age.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        pet.image_url = form.photo_url.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', form=form, pet=pet)


app.run(debug=True)
