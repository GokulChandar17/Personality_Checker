import os
import pandas as pd
from flask import Flask, render_template, request
from pyresparser import ResumeParser
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


class TrainModel:
    def __init__(self):
        self.train()

    def train(self):
        data = pd.read_csv('training_dataset.csv')
        array = data.values

        for i in range(len(array)):
            if array[i][0] == "Male":
                array[i][0] = 1
            else:
                array[i][0] = 0

        df = pd.DataFrame(array)

        main_df = df[[0, 1, 2, 3, 4, 5, 6]]
        main_array = main_df.values

        temp = df[7]
        train_y = temp.values

        self.mul_lr = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
        self.mul_lr.fit(main_array, train_y)

    def test(self, test_data):
        try:
            test_predict = [int(i) for i in test_data]
            y_pred = self.mul_lr.predict([test_predict])
            return y_pred
        except Exception as e:
            print("Error:", e)


model = TrainModel()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            candidate_name = request.form['candidate_name']
            cv_location = request.form['cv_location']
            gender = int(request.form['gender'])
            age = int(request.form['age'])
            openness = int(request.form['openness'])
            neuroticism = int(request.form['neuroticism'])
            conscientiousness = int(request.form['conscientiousness'])
            agreeableness = int(request.form['agreeableness'])
            extraversion = int(request.form['extraversion'])

            personality_values = (gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion)

            personality = model.test(personality_values)[0]

            resume_data = ResumeParser(cv_location).get_extracted_data()
            resume_data = {k.replace('_', ' ').title(): v for k, v in resume_data.items()}

            return render_template('result.html', candidate_name=candidate_name, personality=personality,
                                   resume_data=resume_data)

        except Exception as e:
            print("Error:", e)
            return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
