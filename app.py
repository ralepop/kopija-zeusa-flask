from flask import Flask, render_template
from stranice import stranice

app = Flask(__name__)

@app.route('/')
@app.route('/pocetna/')
def index():
    return render_template('pocetna.html', title='Pocetna', stranice=stranice)

@app.route('/galerija/')
def galerija():
    return render_template('galerija.html', title='Galerija', stranice=stranice)

@app.route('/kontakt/')
def kontakt():
    return render_template('kontakt.html', title='Kontakt', stranice=stranice)

@app.route('/prijava/')
def prijava():
    return render_template('prijava.html', title='Prijava', stranice=stranice)
