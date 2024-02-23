from flask import Flask
from flask import make_response, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
  # get cookie value
  cnt_s = request.cookies.get('cnt')
  if cnt_s is None:
    cnt = 0
  else:
    cnt = int(cnt_s)

  cnt += 1
  response = make_response("""
    <h1>Visit count: {}</h1>                     
  """.format(cnt))

  max_age = 60 * 60 * 24 * 90 # 90 days
  expires = int(datetime.now().timestamp()) + max_age
  response.set_cookie('cnt', value=str(cnt), max_age=max_age, expires=expires)
  # usually set either max_age or expires
  
  return response

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
