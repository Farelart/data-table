from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = (
    ("Rolf", "Software Engineer", "$42,000.00"),
    ("Amy", "Product Owner", "$55,000.00"),
    ("Bob", "Security Engineer", "$45,000.00"),
)


@app.route("/")
def table():
    return render_template("table.html", headings=headings, data=data)

if __name__ == "__main__":
    app.run(host="localhost", port=int(5000), debug=True)


