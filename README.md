# Bank_Loan_Predictor

This is a python application that allows you to predict if clients qualify for a bank loan or not. The user enters the details of a client on the application and that information is used to determine if the client's loan application is approved. After entering clients details and getting the predictions, the results can be exported to a csv file on the application.

The application uses Flask to create the graphical user interface and utilizes classification models to predict the loan approval status.

## How it works

A user enters the details of clients on the application and clicks the submit button, those details are used to determine if a client qualifies for a bank loan. If a client qualifies then an "approved" status is shown and if they don't then a "not approved" status is displayed on the user interface. The clients' details and predictions can be exported to a csv file using the "DOWNLOAD CSV" functionality on the application. 

The application uses Flask to create the graphical user interface and utilizes classification models to predict the loan approval status based on the clients information.

## Installation

To install the repository, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the application, execute the `app.py` file.
Run the following command in your terminal:

```
python app.py
```
