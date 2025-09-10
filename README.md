# Employees CRUD App

A simple **Flask + PostgreSQL** web app to manage employees (add, view, edit, delete).  
Database is hosted on **Neon** and the app runs on **Replit**.

---

## Features
- Add employees (name, title, email)
- View all employees
- Edit employee details
- Delete employees

---

## Tech Used
- Flask (Python)
- PostgreSQL (Neon)
- SQLAlchemy
- HTML + CSS
- Replit (deployment)

---

## Run Locally
1. Clone repo:
   ```bash
   git clone https://github.com/G1DO/employees-app.git
   cd employees-app


Install packages:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Set environment:

export DATABASE_URL='postgresql://neondb_owner:npg_cbIAgfKl0w8t@ep-snowy-darkness-ad3p8k7t-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
export SECRET_KEY="$(python - <<<'import secrets;print(secrets.token_hex(16))')"


Start app:

python app.py


Open http://127.0.0.1:5000


## Live Link
[Live Demo](https://62412de1-d5bd-4658-995c-75966451e0d6-00-14kqg6zejs4kh.worf.replit.dev/)



