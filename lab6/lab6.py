from flask import Flask, render_template
app = Flask(__name__)

# main_recipes = ('Fricasé de Pollo (Chicken Fricaseé)', 
#                'Ajiaco Criolla con Casabe (Creole Stew and Yucca Flatbread)',
#                'Quimbombó con Platano (Okra Stew with Plantain Dumplings)')

# side_recipes = ('Moros y Cristianos (Black Beans and Rice)',
#                'Yucca con Mojo (Yucca with Creole Garlic Sauce)',
#                'Platanós Maduros (Ripe Plantains')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Cuban Cuisine', heading='Cuban Cuisine')

@app.route("/maindishes")
def mains():
    return render_template('maindishes.html', title="Main Dishes", heading="Main Dishes")

@app.route("/sides")
def sides():
    return render_template('sides.html', title="Side Dishes", heading="Side Dishes")
