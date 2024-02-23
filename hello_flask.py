from flask import Flask

# create Flask instance
app = Flask(__name__)

# set route
@app.route('/')
def index():
  return "Hello Flask!"

# execute the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)