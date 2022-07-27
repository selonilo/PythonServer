import os
from flask import Flask, render_template,request
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/verilerial', methods=['POST', 'GET'])
def verilerial():
   if request.method == 'POST':
      isim = request.get_json("isim")

      return jsonify(
          response=isim,
      )

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',5000)))