from flask import Flask
from flask import request, jsonify
# from sklearn import datasets
# from sklearn.neighbors import KNeighborsClassifier
from joblib import load

app = Flask(__name__)


def getName(val):
    val = int(val)

    if val == 0:
        return 'Setosa'
    elif val == 1:
        return 'Versicolor'
    elif val == 2:
        return 'Virginica'
    else:
        return 'Unkown'


@app.route('/api', methods=['GET'])
def predict():
    sl = float(str(request.args['sl']))
    sw = float(str(request.args['sw']))
    pl = float(str(request.args['pl']))
    pw = float(str(request.args['pw']))

    # sl = int(sepal_length)
    # sw = int(sepal_width)
    # pl = int(petal_length)
    # pw = int(petal_width)

    # dataset = datasets.load_iris()
    # x = dataset.data
    # y = dataset.target
    #
    # knn = KNeighborsClassifier()
    # knn.fit(x, y)

    knn = load('iris_model_knn.joblib')

    predicted_flower_num = knn.predict([[sl, sw, pl, pw]])[0]
    # predicted_flower_num = knn.predict([[1, 2, 3, 4]])[0]
    predicted_flower = getName(int(predicted_flower_num))

    json_file = {}
    json_file['query'] = predicted_flower
    # json_file['flower_number'] = str(predicted_flower_num)
    return jsonify(json_file)


if __name__ == '__main__':
    app.run()
