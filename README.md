# 💧 Analyse de l'Irrigation et de la Consommation d'Eau

## 📌 Objectif du Projet (But)
Ce projet vise à analyser les données quotidiennes de température et d'humidité du sol afin d'évaluer les besoins réels en eau d'irrigation et d'optimiser l'utilisation de l'eau dans le domaine agricole.

---

## 📂 Structure du Répertoire
* `agricultural_data.csv` : Ensemble de données réelles contenant la date, la température, l'humidité du sol, la quantité d'eau d'irrigation et l'état des cultures.
* `analysis.py` : Script Python permettant de calculer les moyennes et d'identifier les jours de stress hydrique.

---

## 📊 Résultats et Constatations (Résultats)
Après l'analyse des données via le script Python :
* **Détection du besoin en eau :** Une baisse de l'humidité du sol en dessous de **30%** nécessite une augmentation directe du volume d'eau d'irrigation.
* **Impact de la température :** Les températures élevées (supérieures à **33°C**) augmentent la vitesse d'assèchement du sol.
* **Recommandation :** Automatiser le déclenchement de l'irrigation en se basant sur les seuils d'humidité du sol pour éviter le gaspillage d'eau.

---

## 🛠️ Outils Utilisés
* **Google Sheets / Excel** (Création et structuration des données)
* **Python - Pandas** (Analyse automatique des données)
* **GitHub** (Hébergement et gestion du projet)
