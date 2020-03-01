from flask import Flask, render_template, request
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.trainers import ListTrainer

app = Flask(__name__)

#bot = ChatBot("Candice")
#bot.set_trainer(ListTrainer)
#bot.train(['What is your name?', 'My name is Candice'])
#bot.train(['Who are you?', 'I am a bot' ])
#bot.train(['Do created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return processText(userText)
    #return str(bot.get_response(userText))

def processText(userText):
    if(userText=='hi'):
        return 'fuck you'
    else:
        return 'lol'

if __name__ == "__main__":
    app.run()
