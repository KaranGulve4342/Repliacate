from gevent.pywsgi import WSGIServer
from flask import Flask, render_template
import replicate
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['GET'])
def get_response():
    os.environ["REPLICATE_API_TOKEN"] = "r8_chetwFDt8Crc8pIbhtJVyPdfrEOyQzl20GHV0"
    output = replicate.run(
        "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": "Hello, What is Python? "}
    )
    result = "\n".join(output)  # Join items with newline for plain text response
    return result  # Sending plain text response directly

if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
