"""
lab6.py
By: Vanessa Arreola
November 23, 2021
SDEV 300
"""
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # Homepage route
@app.route("/home")
def home():
    """Pass the date/time, title, and heading as arguments to the html template"""
    current_time = datetime.now()  # current date and time
    date_time = current_time.strftime("%d/%m/%Y, %H:%M:%S")  # create date/time to string
    return render_template('home.html', date_time=date_time, title='Cuban Cuisine',
    heading='Cuban Cuisine')

@app.route("/maindishes")  # Main dishes route
def mains():
    """Pass the title and heading as arguments to the html template"""
    return render_template('maindishes.html', title="Main Dishes", heading="Main Dishes")

@app.route("/sides")  # Side dishes route
def sides():
    """Pass the title and heading as arguments to the html template"""
    return render_template('sides.html', title="Side Dishes", heading="Side Dishes")
