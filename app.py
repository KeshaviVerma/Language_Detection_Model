from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Initialize Flask app
app = Flask(__name__)

# Load and train the model
data = pd.read_csv("dataset.csv")
cv = CountVectorizer()
X = cv.fit_transform(np.array(data['Text']))
y = np.array(data['language'])
model = MultinomialNB()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        transformed_input = cv.transform([user_input]).toarray()
        prediction = model.predict(transformed_input)[0]
        return render_template("index.html", prediction=prediction, user_input=user_input)
    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
