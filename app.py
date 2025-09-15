from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",model_columns=model_columns)  # Show HTML form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect data from form
        data = {col: request.form.get(col) for col in model_columns}

        # Convert numeric fields
        for col in data:
            try:
                data[col] = float(data[col])
            except:
                pass

        # Convert to DataFrame with correct column order
        df = pd.DataFrame([data], columns=model_columns)

        # Prediction
        pred_class = model.predict(df)[0]
        pred_proba = model.predict_proba(df)[0]

        return render_template(
            "result.html",
            prediction=pred_class,
            probabilities=pred_proba
        )

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
