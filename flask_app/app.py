from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('flask_app/models/linear_regression_model.pkl', 'rb') as file_linear:
    linear_model = pickle.load(file_linear)

with open('flask_app/models/random-forest_model.pkl', 'rb') as file_rf:
    rf_model = pickle.load(file_rf)

with open('flask_app/models/xgboost_model.pkl', 'rb') as file_boost:
    xgboost_model = pickle.load(file_boost)

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
            n_bathrooms = int(request.form['n_bathrooms'])
            rent_price = float(request.form['rent_price'])
            price_per_sqm = float(request.form['PricePerSqM'])
            buy_price_by_area = float(request.form['buy_price_by_area'])

            # Créer le tableau des features
            features = np.array([[sq_mt_built, n_rooms, n_bathrooms, rent_price, price_per_sqm, buy_price_by_area]])

            # Prédire avec le modèle
            prediction_linear = linear_model.predict(features)
            print(prediction_linear)

            return render_template('linear.html', prediction_linear = prediction_linear[0],
                                   sq_mt_built = sq_mt_built,
                                   n_rooms = n_rooms,
                                   n_bathrooms = n_bathrooms,
                                   rent_price = rent_price,
                                   price_per_sqm = price_per_sqm,
                                   buy_price_by_area = buy_price_by_area
                                   )

        except Exception as e:
            return f"Erreur : {str(e)}"
    
    return render_template('linear.html', prediction_linear = None)

# Page pour la Random Forest
@app.route('/random_forest', methods=['GET', 'POST'])
def random_forest():
    if request.method == 'POST':
        try:
            # Récupérer les valeurs d'entrée du formulaire
            sq_mt_built = float(request.form['sq_mt_built'])
            n_rooms = int(request.form['n_rooms'])
            n_bathrooms = int(request.form['n_bathrooms'])
            rent_price = float(request.form['rent_price'])
            price_per_sqm = float(request.form['PricePerSqM'])
            buy_price_by_area = float(request.form['buy_price_by_area'])

            # Créer le tableau des features
            features = np.array([[sq_mt_built, n_rooms, n_bathrooms, rent_price, price_per_sqm, buy_price_by_area]])

            # Prédire avec le modèle
            prediction_rf = rf_model.predict(features)

            return render_template('random_forest.html', prediction_rf = prediction_rf[0],
                                   sq_mt_built = sq_mt_built,
                                   n_rooms = n_rooms,
                                   n_bathrooms = n_bathrooms,
                                   rent_price = rent_price,
                                   price_per_sqm = price_per_sqm,
                                   buy_price_by_area = buy_price_by_area)

        except Exception as e:
            return f"Erreur : {str(e)}"
    
    return render_template('random_forest.html', prediction_rf = None)

# Page pour la Random Forest
@app.route('/xgboost', methods=['GET', 'POST'])
def xgboost():
    if request.method == 'POST':
        try:
            # Récupérer les valeurs d'entrée du formulaire
            sq_mt_built = float(request.form['sq_mt_built'])
            n_rooms = int(request.form['n_rooms'])
            n_bathrooms = int(request.form['n_bathrooms'])
            rent_price = float(request.form['rent_price'])
            price_per_sqm = float(request.form['PricePerSqM'])
            buy_price_by_area = float(request.form['buy_price_by_area'])

            # Créer le tableau des features
            features = np.array([[sq_mt_built, n_rooms, n_bathrooms, rent_price, price_per_sqm, buy_price_by_area]])

            # Prédire avec le modèle
            prediction_boost = xgboost_model.predict(features)

            return render_template('xgboost.html', prediction_boost = prediction_boost[0],
                                   sq_mt_built = sq_mt_built,
                                   n_rooms = n_rooms,
                                   n_bathrooms = n_bathrooms,
                                   rent_price = rent_price,
                                   price_per_sqm = price_per_sqm,
                                   buy_price_by_area = buy_price_by_area)

        except Exception as e:
            return f"Erreur : {str(e)}"
    
    return render_template('xgboost.html', prediction_boost = None)

if __name__ == '__main__':
    app.run(debug=True)