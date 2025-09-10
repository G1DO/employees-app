import os
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base, Employee

DATABASE_URL = os.getenv("DATABASE_URL")  # e.g. postgres://user:pwd@host/db?sslmode=require
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-me")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Base.metadata.create_all(engine)
SessionLocal = scoped_session(sessionmaker(bind=engine))

@app.teardown_appcontext
def remove_session(exc=None):
    SessionLocal.remove()

@app.route("/")
def index():
    db = SessionLocal()
    employees = db.query(Employee).order_by(Employee.id.desc()).all()
    return render_template("index.html", employees=employees)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"].strip()
        title = request.form["title"].strip()
        email = request.form["email"].strip()
        if not (name and title and email):
            flash("All fields are required.")
            return redirect(url_for("create"))
        db = SessionLocal()
        db.add(Employee(name=name, title=title, email=email))
        db.commit()
        flash("Employee added.")
        return redirect(url_for("index"))
    return render_template("form.html", action="Create", employee=None)

@app.route("/edit/<int:emp_id>", methods=["GET", "POST"])
def edit(emp_id):
    db = SessionLocal()
    emp = db.get(Employee, emp_id)
    if not emp:
        flash("Employee not found.")
        return redirect(url_for("index"))
    if request.method == "POST":
        emp.name = request.form["name"].strip()
        emp.title = request.form["title"].strip()
        emp.email = request.form["email"].strip()
        db.commit()
        flash("Employee updated.")
        return redirect(url_for("index"))
    return render_template("form.html", action="Update", employee=emp)

@app.route("/delete/<int:emp_id>", methods=["POST"])
def delete(emp_id):
    db = SessionLocal()
    emp = db.get(Employee, emp_id)
    if emp:
        db.delete(emp); db.commit()
        flash("Employee deleted.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
