from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  # get URL parameters
  a = request.args.get('a')
  b = request.args.get('b')

  # validate the parameters
  if (a is None) or (b is None):
    return "some parameters are missing!"
  
  # convert parameters to numbers and calculate
  c = int(a) * int(b)

  # output the result
  return "<h1>" + str(c) + "</h1>"

if __name__ == '__main__':
  app.run(host='0.0.0.0')
  