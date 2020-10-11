from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import api_twitter 
import pandas as pd

app = Flask(__name__)
api = Api(app) 

@app.route('/')
def index():
    return 'Bem Vindo'




def abort_if_city_doesnt_exist(cidade):
    if cidade.lower() not in cidades.values:
        abort(404, message="Cidade {} nao existe".format(cidade))


def abort_if_words_doesnt_exist(twitter):
    if twitter == 'null':
        abort(404, message="Palavras chaves {} nao encontradas".format(cidade))

parser = reqparse.RequestParser()
parser.add_argument('task')





class Cidade(Resource):
    def get(self, cidade):
        abort_if_city_doesnt_exist(cidade)
        return {'cidade': cidade, 'informacoes': 'Cidade encontrada'}


def comma_separated_params_to_list(param):
    result = []
    for val in param.split(','):
        if val:
            result.append(val)
    return result




class MensagensTwitter(Resource):
    def get(self, cidade, palavras_chaves):
         
        palavras_chaves = comma_separated_params_to_list(palavras_chaves)

        twt_selected, user_selected = api_twitter.selecionar_twitter(palavras_chaves, cidade)

        abort_if_words_doesnt_exist(twt_selected)

        return {'Twitter': twt_selected, "User": user_selected}

    

##
## Actually setup the Api resource routing here
##

api.add_resource(Cidade, '/<cidade>')
api.add_resource(MensagensTwitter, '/<cidade>/<palavras_chaves>')


if __name__ == '__main__':
    cidades = pd.read_csv('cidades.csv')
    app.run(debug=False)