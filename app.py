from flask import Flask,render_template,request,jsonify
import json
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)


# Load FAQ data

with open("data/faq.json") as file:
    faqs=json.load(file)


questions=[
    faq["question"] for faq in faqs
]


answers=[
    faq["answer"] for faq in faqs
]


# NLP Model

vectorizer=TfidfVectorizer()

vectors=vectorizer.fit_transform(questions)



def chatbot_response(user_text):

    user_vector=vectorizer.transform([user_text])


    similarity=cosine_similarity(
        user_vector,
        vectors
    )


    index=similarity.argmax()


    score=similarity[0][index]


    if score < 0.2:
        return "Sorry, I don't understand your question."


    return answers[index]





@app.route("/")
def home():

    return render_template("index.html")




@app.route("/chat",methods=["POST"])
def chat():

    user_message=request.json["message"]

    reply=chatbot_response(user_message)


    return jsonify({
        "answer":reply
    })




if __name__=="__main__":

    app.run(debug=True)