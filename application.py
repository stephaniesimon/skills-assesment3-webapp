from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/application-form")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application", methods=["POST"])
def show_application_results():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_req = "$" + request.form.get("salary")
    job_title= request.form.get("jobtitle")

   
    return render_template("completed_application.html", firstname = first_name, lastname = last_name, salary = salary_req, jobtitle = job_title)
    

if __name__ == "__main__":
    app.run(debug=True)