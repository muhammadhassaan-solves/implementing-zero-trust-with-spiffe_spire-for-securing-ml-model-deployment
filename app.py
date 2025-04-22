from flask import Flask, request, jsonify, render_template_string
import numpy as np
import joblib

app = Flask(__name__)

# Make sure the model is loaded here, before you run the app
try:
    model = joblib.load('linear_regression_model.pkl')  # Load the saved scikit-learn model
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)  # Exit if the model cannot be loaded, so app doesn't run without it

# HTML page served at root for browser interface
HTML_PAGE = '''
<!doctype html>
<html>
<head>
  <title>Linear Regression Predictor</title>
</head>
<body>
  <h1>Predict Value</h1>
  <input type="number" id="inputValue" placeholder="Enter a number" />
  <button onclick="predict()">Predict</button>
  <p id="result"></p>
  <script>
    async function predict() {
      const value = document.getElementById('inputValue').value;
      const res = await fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({input: value})
        });
      const data = await res.json();
      if (res.ok) {
        document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
      } else {
        document.getElementById('result').innerText = 'Error: ' + data.error;
      }
    }
  </script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_PAGE)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Expecting a single numeric input e.g. {"input": 6}
    try:
        value = float(data['input'])
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Provide a numeric "input".'}), 400
    inp = np.array([[value]])
    pred = model.predict(inp)[0]
    return jsonify({'prediction': pred})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('server.crt', 'server.key'))
