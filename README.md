# apartment-hunter
 
## Les différentes techniques de régression en apprentissage automatique

### 1. **Régression Linéaire**
<u>**Description**</u> : La régression linéaire est l'une des techniques de base en statistiques et en apprentissage automatique. Elle modélise la relation linéaire entre une variable dépendante (Y) et une ou plusieurs variables indépendantes (X). L'objectif est de trouver la meilleure ligne droite (ou hyperplan dans le cas multidimensionnel) qui minimise la somme des carrés des résidus. Elle est simple à interpréter et à mettre en œuvre, mais suppose une relation linéaire entre les variables.

<u>**Exemple**</u> : Prédire les prix des maisons en fonction de leur superficie, en supposant une relation linéaire entre la taille et le prix.

### 2. **Régression Polynomiale**
<u>**Description**</u> : La régression polynomiale est une extension de la régression linéaire qui permet de modéliser des relations non linéaires entre les variables. Elle introduit des termes polynomiaux (x², x³, etc.) dans l'équation de régression. Cela offre plus de flexibilité pour capturer des courbes et des formes complexes dans les données, mais peut être sujette au surapprentissage si le degré du polynôme est trop élevé.

<u>**Exemple**</u> : Modéliser la relation entre la température et le rendement des cultures, qui peut avoir une forme parabolique (augmentation jusqu'à un certain point, puis diminution).

### 3. **Régression Lasso (régularisation L1)**
<u>**Description**</u> : La régression Lasso (Least Absolute Shrinkage and Selection Operator) utilise une pénalité L1, qui est proportionnelle à la somme des valeurs absolues des coefficients. Contrairement à Ridge, Lasso peut réduire certains coefficients exactement à zéro, effectuant ainsi une sélection de caractéristiques. Cela la rend utile pour créer des modèles parcimonieux et identifier les variables les plus importantes.

<u>**Exemple**</u> : Identifier les facteurs les plus importants affectant le temps de récupération des patients à partir d'un grand ensemble de variables médicales, en éliminant automatiquement les facteurs moins influents.

### 4. **Régression Ridge (régularisation L2)**
<u>**Description**</u> : La régression Ridge ajoute un terme de pénalité L2 à la fonction de coût de la régression linéaire. Cette pénalité est proportionnelle à la somme des carrés des coefficients. Cela aide à réduire la variance du modèle en rétrécissant les coefficients vers zéro, sans les éliminer complètement. Ridge est particulièrement utile lorsqu'il y a de la multicolinéarité entre les variables prédictives.

<u>**Exemple**</u> : Prédire les prix des actions en utilisant plusieurs caractéristiques économiques corrélées, en évitant que certaines caractéristiques n'aient une influence disproportionnée.

### 5. **Régression Elastic Net**
<u>**Description**</u> : Elastic Net combine les pénalités L1 et L2 de Lasso et Ridge. Cette approche permet de bénéficier des avantages des deux méthodes : la capacité de sélection de variables de Lasso et la stabilité de Ridge en présence de forte multicolinéarité. L'importance relative des pénalités L1 et L2 peut être ajustée, offrant une grande flexibilité.

<u>**Exemple**</u> : Prédire la consommation d'énergie dans les bâtiments en utilisant un mélange de caractéristiques importantes (comme la taille du bâtiment) et de variables légèrement corrélées (comme différentes mesures de température).

### 6. **Régression Logistique**
<u>**Description**</u> : Malgré son nom, la régression logistique est utilisée pour la classification binaire. Elle modélise la probabilité qu'une instance appartienne à une classe particulière en utilisant la fonction logistique (sigmoïde). Cette fonction transforme une combinaison linéaire des variables d'entrée en une probabilité entre 0 et 1. Elle est largement utilisée en raison de sa simplicité et de son interprétabilité.

<u>**Exemple**</u> : Prédire si un e-mail est un spam ou non en fonction de son contenu et de ses métadonnées, en calculant la probabilité qu'il appartienne à la classe "spam".

### 7. **Régression pas à pas**
<u>**Description**</u> : La régression pas à pas est une méthode de sélection de variables qui ajoute ou supprime itérativement des prédicteurs dans le modèle. Il existe trois approches principales : forward (ajout progressif), backward (élimination progressive), et bidirectionnelle. À chaque étape, la méthode évalue l'importance statistique de l'ajout ou de la suppression d'une variable, généralement en utilisant des critères comme l'AIC (Akaike Information Criterion) ou le BIC (Bayesian Information Criterion).

<u>**Exemple**</u> : Déterminer quels indicateurs économiques parmi un grand ensemble sont les plus prédictifs de la croissance du PIB, en construisant progressivement un modèle avec les indicateurs les plus significatifs.

### 8. **Régression en Composantes Principales (PCR)**
<u>**Description**</u> : La PCR combine l'analyse en composantes principales (ACP) avec la régression linéaire. Elle commence par réduire la dimensionnalité des données en utilisant l'ACP pour créer de nouvelles variables non corrélées (composantes principales), puis effectue une régression sur ces composantes. Cette méthode est particulièrement utile pour gérer la multicolinéarité et réduire le bruit dans les données à haute dimension.

<u>**Exemple**</u> : Analyser des données spectrales en chimie pour prédire la concentration d'un composé, en utilisant les composantes principales des spectres comme prédicteurs plutôt que les longueurs d'onde individuelles.

### 9. **Régression des Moindres Carrés Partiels (PLS)**
<u>**Description**</u> : La régression PLS est similaire à la PCR, mais au lieu de maximiser uniquement la variance des prédicteurs (comme dans l'ACP), elle cherche à maximiser la covariance entre les prédicteurs et la variable de réponse. Cela signifie que les composantes créées sont directement pertinentes pour la prédiction de la variable cible. PLS est particulièrement utile lorsqu'il y a beaucoup de prédicteurs corrélés et peu d'observations.

<u>**Exemple**</u> : Prédire les rendements des cultures en fonction de diverses mesures du sol et du climat, en créant des composantes qui capturent au mieux la relation entre ces mesures et le rendement.

### 10. **Régression à Vecteurs de Support (SVR)**
<u>**Description**</u> : La SVR applique les principes des machines à vecteurs de support à la régression. Elle cherche à trouver une fonction qui s'écarte au maximum d'une valeur ε des points observés. La SVR peut être utilisée avec différents noyaux (linéaire, polynomial, RBF) pour capturer des relations non linéaires complexes. Elle est robuste aux outliers et peut gérer efficacement les espaces de caractéristiques de haute dimension.

<u>**Exemple**</u> : Prédire la puissance de sortie des éoliennes en fonction de la vitesse et de la direction du vent, en capturant des relations non linéaires complexes entre ces variables.

### 11. **Régression par Arbre de Décision**
<u>**Description**</u> : La régression par arbre de décision divise récursivement l'espace des caractéristiques en régions, où chaque région est représentée par une valeur constante (généralement la moyenne de la variable cible dans cette région). Les arbres sont faciles à interpréter, peuvent capturer des interactions complexes entre les variables, et gèrent naturellement les variables catégorielles et les valeurs manquantes. Cependant, ils peuvent être sujets au surapprentissage s'ils ne sont pas élagués ou régularisés.

<u>**Exemple**</u> : Estimer l'efficacité énergétique d'une voiture en fonction de ses caractéristiques comme le poids, la puissance et le nombre de cylindres, en divisant les voitures en groupes de plus en plus homogènes en termes d'efficacité.

### 12. **Régression par Forêt Aléatoire**
<u>**Description**</u> : La forêt aléatoire est une méthode d'ensemble qui construit de nombreux arbres de décision et combine leurs prédictions. Chaque arbre est construit sur un sous-ensemble aléatoire des données et des caractéristiques, ce qui réduit la variance et le surapprentissage. Les forêts aléatoires sont robustes, gèrent bien les données de haute dimension, et fournissent des mesures d'importance des variables.

<u>**Exemple**</u> : Prédire le nombre de ventes hebdomadaires d'un magasin de détail en fonction de divers facteurs comme les promotions, les jours fériés et les magasins concurrents, en combinant les prédictions de nombreux arbres différents.

### 13. **Régression par Boosting Gradient**
<u>**Description**</u> : Le boosting gradient est une technique d'ensemble qui construit des modèles (généralement des arbres de décision) de manière séquentielle. Chaque nouveau modèle est entraîné pour corriger les erreurs des modèles précédents. Cette approche peut capturer des relations très complexes et non linéaires, et est souvent très performante en pratique. Des variantes populaires incluent XGBoost, LightGBM et CatBoost.

<u>**Exemple**</u> : Prévoir la demande d'un produit en fonction des données de ventes historiques et des facteurs externes, en améliorant progressivement les prédictions à travers une série de modèles.

### 14. **Régression par Réseau de Neurones**
<u>**Description**</u> : Les réseaux de neurones pour la régression utilisent des couches interconnectées de "neurones" pour modéliser des relations complexes et non linéaires. Ils peuvent automatiquement apprendre des représentations hiérarchiques des données, ce qui les rend puissants pour des tâches complexes. Les architectures courantes incluent les perceptrons multicouches (MLP) et, pour les données séquentielles, les réseaux récurrents (RNN) ou les réseaux de neurones à convolution (CNN) pour les données spatiales.

<u>**Exemple**</u> : Prédire la production d'énergie d'un panneau solaire en fonction des conditions météorologiques, de l'heure de la journée et des caractéristiques du panneau, en capturant des interactions complexes entre ces variables.

### 15. **Régression de Poisson**
<u>**Description**</u> : La régression de Poisson est utilisée pour modéliser des données de comptage, où la variable de réponse suit une distribution de Poisson. Elle suppose que le logarithme de la valeur attendue peut être modélisé par une combinaison linéaire des prédicteurs. Cette méthode est particulièrement utile pour des phénomènes rares ou des événements discrets dans un intervalle de temps ou d'espace fixe.

<u>**Exemple**</u> : Prédire le nombre d'appels au service client qu'une entreprise recevra en une journée en fonction de divers facteurs comme le jour de la semaine, les promotions en cours et les récentes sorties de produits, en modélisant explicitement la nature discrète et non négative des données de comptage.

### 16. **Régression de Cox**
<u>**Description**</u> : La régression de Cox, ou modèle à risques proportionnels de Cox, est utilisée en analyse de survie pour étudier la relation entre le temps jusqu'à un événement et une ou plusieurs variables prédictives. Elle ne fait pas d'hypothèses sur la forme de la fonction de risque de base, ce qui la rend semi-paramétrique. Le modèle suppose que l'effet des variables prédictives sur le risque est constant dans le temps (hypothèse des risques proportionnels).

<u>**Exemple**</u> : Analyser les facteurs qui influencent le temps jusqu'à la défaillance d'une pièce de machine dans un cadre industriel, en tenant compte de variables comme la température de fonctionnement, la charge et la fréquence de maintenance, tout en gérant les données censurées (pièces qui n'ont pas encore échoué à la fin de l'étude).

## Choix des Techniques de Régression pour notre Problème

Pour un projet visant à déterminer le prix d'un appartement en fonction de ses caractéristiques, nous choississons de comparer les performances des techniques de régression suivantes :

### 1. Régression Linéaire Multiple:
- **Avantages** :  
    - Facile à interpréter et à expliquer aux parties prenantes non techniques.
    - Bonne performance, souvant suffisante pour capturer les relations linéaires entre les caractéristiques de l'appartement et son prix.
    - Rapide à entraîner et à déployer, ce qui est utile pour des itérations rapides et les tests.
- **Limitations** :  
    - Ne peut capturer que des relations linéaires entre les caractéristiques et le prix, ce qui peut être limitant pour des relations non linéaires qui peuvent exister dans le marché immobilier.
    - Sensible aux valeurs aberrantes et aux erreurs de mesure dans les données.

### 2. Forêt Aléatoire:
- **Avantages** :  
    - Gère bien les relations non linéaires et les interactions complexes entre les caractéristiques.
    - Robuste aux valeurs aberrantes et aux erreurs de mesure, grâce à l'agrégation de nombreux arbres.
    - Fournit des mesures d'importance des variables pour identifier les caractéristiques les plus influentes.
    - Bonne performance en général, même sans réglage fin.
- **Limitations** :  
    - Moins interprétable que la régression linéaire, ce qui peut être un inconvénient si l'explication du modèle est importante.
    - Peut être plus lent à entraîner et à déployer que la régression linéaire, en particulier pour de grandes forêts.

### 3. Gradient Boosting:
- **Avantages** :  
    - Performances généralement supérieures à la forêt aléatoire, en particulier pour des ensembles de données de taille moyenne à grande.
    - Peut capturer des relations très complexes et non linéaires entre les caractéristiques et le prix.
    - Robuste aux valeurs aberrantes et aux erreurs de mesure, grâce à l'agrégation de nombreux modèles.
    - Permet un réglage fin des hyperparamètres pour optimiser les performances.
- **Limitations** :
    - Plus complexe à mettre en œuvre et à régler que la forêt aléatoire, nécessitant plus d'expertise et de temps.
    Risque de surapprentissage si les hyperparamètres ne sont pas correctement réglés.
    Temps d'entraînement plus long que les autres méthodes, en particulier pour des ensembles de données volumineux.

Ces trois algorithmes offrent un bon équilibre entre simplicité, performance et interprétabilité. Pour notre problème de prédiction des prix des appartements, nous commencerons par entraîner et évaluer un modèle de régression linéaire multiple afin de construire une base de comparaison. Ensuite, nous explorerons les performances de la forêt aléatoire et du boosting gradient pour voir si des modèles plus complexes peuvent améliorer les prédictions. Nous comparerons les résultats en fonction de mesures de performance telles que l'erreur quadratique moyenne (RMSE) et le coefficient de détermination (R²), ainsi que de l'interprétabilité des modèles.