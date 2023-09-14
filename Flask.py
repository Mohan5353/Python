from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    username = request.form["username"]
    # Add more fields as needed

    # Create a dictionary with the sign-up details
    signup_details = {
        "Name": name,
        "Email": email,
        "Username": username,
        # Add more fields here
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(signup_details, index=[0])

    # Save the DataFrame to an Excel file
    df.to_excel("signup_details.xlsx", index=False)

    return "Sign-up details saved successfully!"


if __name__ == "__main__":
    app.run()
