import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

@app.route("/api/alive", methods = ['GET'])
def fonctionne():
    return make_response(jsonify({ "message": "Alive" }), 200)

@app.route("/api/associations", methods = ['GET'])
def liste():
    listeassos = associations_df['id'].to_list()
    return make_response(jsonify({ "message": f"{listeassos}" }), 200)

@app.route("/api/association/<int:id>", methods = ['GET'])
def nom(id):
    if id in associations_df['id'].to_list() :
        nomassos = associations_df[associations_df.id==id]['description'].to_list() #erreurs d'affichage mais ca marche un peu
        return make_response(jsonify({ "message": f"{nomassos}" }), 200)
    else :
        return make_response(jsonify({ "error": "Association not found" }), 404)

@app.route("/api/evenements", methods = ['GET'])
def liste2():
    listeevent = evenements_df["id"].to_list()
    return make_response(jsonify({ "message": f"{listeevent}" }), 200)

@app.route("/api/evenement/<int:id>", methods = ['GET'])
def nom2(id):
    if id in evenements_df["id"].to_list() :
        nomevent = evenements_df[evenements_df.id==id]['description'].to_list()
        return make_response(jsonify({ "message": f"{nomevent}" }), 200)
    else :
        return make_response(jsonify({ "error": "Event not found" }), 404)

@app.route("/api/association/<int:id>/evenements", methods = ['GET'])
def listeeventsasso(id):
    nomsevent = evenements_df[evenements_df.association_id==id]["nom"].to_list()
    return make_response(jsonify({ "message": f"{nomsevent}" }), 200)

@app.route("/api/associations/type/<type>", methods = ['GET'])
def listetype(type):
    listeassos = associations_df[associations_df.type==type]['nom']
    return make_response(jsonify({ "message": f"{listeassos}" }), 200)


if __name__ == '__main__':
    app.run(debug=True)
