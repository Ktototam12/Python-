#!/usr/bin/env.python3
#--*-- coding: -utf-8--*-

import flask

import data_processing as dpr

app = flask.Flask('Pytrain2022')

@app.route('/', methods=['GET'])
def show_index_page():
    return 'Hello World!'
 
@app.get(' /word/<filename>/<filt>')
def process_word_filter(filename: str, filt: str):
    # return: flask. jsonify(dpr.filter_tweet_text(f'./data/{filename}.txt', filt).to_dict()['text'])
    tweets = list(dpr.filter_tweet_text(f'./data/{filename}.txt', filt).to_dict()['text'].values())
    return flask.render_template('filter.html', filtered_tweets=tweets)
    #-return-list (dpr.filter_tweet_text(f'. /data/{filename}.txt', filt).to_dict()[‘text'].values())
    
    if _name_ == 'main':
        app.run('0.0.0.0', port=9979, debug=True)
