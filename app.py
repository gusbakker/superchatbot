import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_pymongo import PyMongo

MONGODB_NAME = os.environ.get('MONGODB_NAME', None)
MONGODB_URI = os.environ.get('MONGODB_URI', None)

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

english_bot = ChatBot("English Bot",
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = MONGODB_NAME,
                     database_uri = MONGODB_URI)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(english_bot.get_response(user_text))


if __name__ == "__main__":
    app.run()
