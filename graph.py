# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 00:28:33 2017

@author: Saniyah
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/runscript")
def run_script():
    rand = {}
    for x in range(8):
        num = random.choice(range(100))
        rand.update({x:num})
    # print (rand)
    plot_emotions(rand, 'testing')
    return render_template('index.html')

def getColor(i):
    colors = ['green', 'purple', 'blue', 'red', 'orange', 'yellow', 'black', 'pink', 'gray']
    i = i % len(colors)
    return colors[i]

# dict is a dictionary of emotions to integer plotting values
def plot_emotions(dic, save):
    plt.figure(1)
    y = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    plt.xticks(np.arange(0, 110, 10))
    y_ticks_labels = ['disgust', 'shame', 'sadness', 'anger', 'fear', 'joy', 'guilt']
    for i in range(len(y)-1):    
        ax = plt.gcf().gca()
        ax.add_patch(patches.Rectangle((0,i+0.25), dic[int(i)], 0.5, facecolor=getColor(i)))
    plt.xlabel('Percentages')
    plt.ylabel('Emotions')
    for elt in y:
        elt = elt * 50
    plt.yticks(y)
    ax.set_yticklabels(y_ticks_labels, rotation='horizontal', fontsize=12)
    plt.suptitle('Percentage of Each Emotion')
    plt.savefig(save + '.png', bbox_inches='tight')
    plt.show()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug = True