from flask import Flask, render_template, request, jsonify
import random
from ai_req import ai_req
from waitress import serve
# from database_functions import return_all, update_rapper_score

def get_two_random_items(characters):
    random_items = random.sample(characters, 2)
    return random_items

characters = ["Harry Potter", "Sherlock Holmes", "Darth Vader", "Frodo Baggins", "Hermione Granger", "Luke Skywalker", "James Bond", "Wonder Woman", "Spider-Man", "Superman", "Mickey Mouse", "Captain Jack Sparrow", "Gandalf", "Batman", "Iron Man", "Captain America", "Miles Morales", "Hulk", "Thor", "Black Widow", "Wolverine", "Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Hannibal Lecter", "Sherlock Holmes", "Winnie the Pooh", "Mulan", "Elsa", "Simba", "James T. Kirk", "Spock", "Homer Simpson", "Dora the Explorer", "Mickey Mouse", "Bart Simpson", "SpongeBob SquarePants", "Shrek", "Pikachu", "Goku", "Naruto Uzumaki", "Katniss Everdeen", "Ron Weasley", "Albus Dumbledore", "Severus Snape", "Gollum", "Jay Gatsby", "Tom Sawyer", "Huckleberry Finn", "Ebenezer Scrooge", "Hamlet", "Juliet Capulet", "Macbeth", "Dracula", "Frankenstein's Monster", "Alice (in Wonderland)", "Dr. Jekyll and Mr. Hyde", "Robinson Crusoe", "Tarzan", "Odysseus", "Robin Hood", "King Arthur", "Lara Croft", "Indiana Jones", "Ellen Ripley", "Tony Stark", "Leia Organa", "Rocky Balboa", "Neo", "Ellie (The Last of Us)", "Joel (The Last of Us)", "Mr. Beast", "Kratos", "Link", "Master Chief", "Mario", "Luigi", "Princess Peach"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', artists = get_two_random_items(characters))

@app.route('/get-rap', methods=['POST'])
def get_rap():
    data = request.json
    character_one = data.get('character_one')
    character_two = data.get('character_two')
    response = ai_req(character_one, character_two)
    return jsonify(response)

app.config["TEMPLATES_AUTO_RELOAD"] = True

if __name__ == '__main__':
   #  serve(app, host="0.0.0.0", port=8080)
   app.run()