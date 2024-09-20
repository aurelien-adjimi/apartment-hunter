from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('./models/linear_regression_model.pkl', 'rb') as file:
    linear_model = pickle.load(file)

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page pour la régression linéaire
@app.route('/linear', methods=['GET', 'POST'])
def linear():
    if request.method == 'POST':
        try:
            # Récupérer les valeurs d'entrée du formulaire
            sq_mt_built = float(request.form['sq_mt_built'])
            n_rooms = int(request.form['n_rooms'])
            buy_price_by_area = float(request.form['buy_price_by_area'])
            price_per_sqm = float(request.form['PricePerSqM'])

            # Créer le tableau des features
            features = np.array([[sq_mt_built, n_rooms, buy_price_by_area, price_per_sqm]])

            # Prédire avec le modèle
            prediction = linear_model.predict(features)

            return render_template('linear.html', prediction=prediction[0])

        except Exception as e:
            return f"Erreur : {str(e)}"
    
    return render_template('linear.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)