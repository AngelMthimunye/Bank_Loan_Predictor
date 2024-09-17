import numpy as np
from flask import Flask, request, render_template, send_file
import pickle
import csv
import os
import tempfile

app = Flask(__name__)
model = pickle.load(open("bank_loan_approval.pkl", "rb"))

# Temporary directory for storing the CSV file
TEMP_DIR = tempfile.gettempdir()
CSV_FILE_PATH = os.path.join(TEMP_DIR, "loan_prediction.csv")

# Mappings for descriptive words
job_mapping = {
    "0": "Admin", "1": "Blue-Collar", "2": "Entrepreneur", "3": "Housemaid",
    "4": "Management", "5": "Retired", "6": "Self-Employed", "7": "Services",
    "8": "Student", "9": "Technician", "10": "Unemployed", "11": "Unknown"
}
housing_mapping = {"0": "No", "1": "Yes"}
deposit_mapping = {"0": "No", "1": "Yes"}
month_mapping = {
    "0": "April", "1": "August", "2": "February", "3": "December",
    "4": "January", "5": "July", "6": "June", "7": "March",
    "8": "May", "9": "November", "10": "October", "11": "September"
}

@app.route("/")
def home():
    return render_template("loan.html")

@app.route("/predict", methods=["POST"])
def predict():
    status = ""
    
    # Extract and process form values
    form_values = list(request.form.values())
    features = [float(x) for x in form_values]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    
    # Set the status message based on the prediction
    if prediction == 0:
        status = "Not Approved"
    else:
        status = "Approved"
    
    # Convert form values to descriptive words
    data = [
        form_values[0],  # Client ID
        job_mapping[form_values[1]],  # Job
        form_values[2],  # Age
        housing_mapping[form_values[3]],  # Housing
        form_values[4],  # Pdays
        form_values[5],  # Balance
        form_values[6],  # Duration
        deposit_mapping[form_values[7]],  # Deposit
        month_mapping[form_values[8]],  # Month
        form_values[9],  # Campaign
        "Qualified" if prediction[0] == 1 else "Not Qualified"  # Prediction
    ]
    
    # Append data to CSV file
    try:
        # Check if the CSV file already exists
        file_exists = os.path.isfile(CSV_FILE_PATH)
        
        with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header only if the file does not exist
            if not file_exists:
                header = ["Client ID", "Job", "Age", "Housing", "Pdays", "Balance", "Duration", "Deposit", "Month", "Campaign", "Prediction"]
                writer.writerow(header)
            writer.writerow(data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")
    
    return render_template("loan.html", prediction_text="STATUS: {}".format(status))

@app.route("/download", methods=["GET"])
def download():
    # Check if the file exists
    if os.path.exists(CSV_FILE_PATH):
        return send_file(CSV_FILE_PATH, as_attachment=True)
    else:
        return "Error: The file does not exist."

if __name__ == "__main__":
    app.run(debug=True)
