import dill
from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
import re
from razdel import tokenize
import nltk
from nltk.corpus import stopwords
import pymorphy2
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

nltk.download('stopwords')
stopword_ru = stopwords.words('russian')
dill._dill._reverse_typemap['ClassType'] = type

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)

with open('app/models/NB_pipeline.dill', 'rb') as in_strm:
    model = dill.load(in_strm)


@app.route("/", methods=["GET"])
def general():
    return """Добро пожаловать на сервис анализа тональности комментариев\n
	        Для анализа необходимо сделать POST запрос на 'http://127.0.0.1/predict'"""

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":

        comment = ""
        request_json = request.get_json()

        if request_json["comment"]:
            comment = request_json['comment']

        try:
            preds = model.predict_proba(pd.DataFrame({"comment" : [comment]}))


        except AttributeError as e:

            logger.warning(f'{dt} Exception: {str(e)}')

            data['predictions'] = str(e)

            data['success'] = False

            return jsonify(data)

        data["predictions"] = preds[:, 1][0]
        data["comment"] = comment
	    # indicate that the request was a success
        data["success"] = True

	# return the data dictionary as a JSON response
    return jsonify(data)


if __name__ == '__main__':
    print(("Загрузка сервера..."))
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', debug=True, port=port)