from flask import Flask, request, render_template
from itertools import islice 
import random
app = Flask(__name__)

#players = []

@app.route('/')
def scrim_sort():
    return render_template('scrim-sort.html')

@app.route('/', methods=['POST'])
def scrim_sort():
    text_input = request.form['text']
    processed_text = text_input.upper()
    
    players = [str(x) for x in processed_text.split(', ')] 
    ##print("\nThe values of input are", L)  
    random.shuffle(players)
    squad = iter(players) 
    split_me_open = [3, 3, 3, 3, 3, 3, 3, 3]
    teams = [list(islice(squad, i)) 
              for i in split_me_open]     
    return(str(teams))
    #return(str(players))