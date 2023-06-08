# from flask import Flask, render_template
from SpotifyProject import app

if __name__ == '__main__':
    app.run(debug=True)

app.config['SECRET_KEY'] = 'super secret string' #Had to have secret key to run
# app = Flask(__name__)

# # @app.route('/')
# # def home1():
# #     return render_template('home.html')

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/crap/')
# def crap():
#     return render_template('crap.html')

# @app.route('/crappy/') 
# def crappy():
#     return render_template('crappy.html')

# @app.route('/shit/')
# def shit():
#     return render_template('shit.html')

# app.run()