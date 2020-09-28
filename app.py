from flask import Flask, request, render_template
from itertools import islice 
import random
app = Flask(__name__)


### Main Page #####################################
@app.route('/')
def base():
    return render_template('base.html')

### Home #####################################
@app.route('/home/')
def home():
    return render_template('home.html')

### Squad Sorting Page #####################################
@app.route('/squads/')
def scrim_template_render():
    return render_template('squads.html')
@app.route('/squads/', methods=['POST'])
def scrim_sort():
    text_input = request.form['text']
    processed_text = text_input.upper()
    players = [str(x) for x in processed_text.split(', ')]
    random.shuffle(players)
    squad = iter(players)
    split_me_open = [3, 3, 3, 3, 3, 3, 3, 3]
    teams = [list(islice(squad, i))
              for i in split_me_open]
    return(str(teams))
######################################################