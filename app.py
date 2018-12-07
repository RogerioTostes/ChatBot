from flask import Flask, render_template, request
from chatterbot import ChatBot
import os

from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot('Test')

bot.set_trainer(ListTrainer )

for Conversas in os.listdir('Conversas'):
	chats = open('Conversas/' + Conversas, 'r').readlines()
	bot.train(chats)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
