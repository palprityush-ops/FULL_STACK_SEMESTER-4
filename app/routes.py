from flask import Blueprint, render_template, request, redirect
from app.models import Employee
from app import db

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        emp = Employee(name=name, email=email)
        db.session.add(emp)
        db.session.commit()
        return redirect("/")

    employees = Employee.query.all()
    return render_template("index.html", employees=employees)


@main.route("/delete/<int:sno>")
def delete(sno):
    emp = Employee.query.get_or_404(sno)
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")


@main.route("/edit/<int:sno>", methods=["GET", "POST"])
def edit(sno):
    emp = Employee.query.get_or_404(sno)

    if request.method == "POST":
        emp.name = request.form["name"]
        emp.email = request.form["email"]
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", emp=emp)
