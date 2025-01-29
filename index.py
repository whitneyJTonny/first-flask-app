#Assignment

#Create a first flask App that returns your name
#Ignore the virtual environment while pushing your work to github(should have a .gitignore file)

#solution

from flask import Flask

app = Flask('__name__') #creating the app instance
@app.route('/')
def home():
   return '<h2> Nanyunja Whitney Josephin</h2>'
if __name__ == '__main__':
   app.run(debug=True)