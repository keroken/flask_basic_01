from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return """
    <html><body>
      <form action="/hello" method="GET">
        name: <input type="text" name="name">
        <input type="submit" value="send">
      </form>
    </body><html>
  """

@app.route('/hello')
def hello():
  name = request.args.get('name')
  if name is None: name = 'no name'

  return """
    <h1>Hello {0}!</h1>
  """.format(name)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
  