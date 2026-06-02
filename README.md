\# TaskFlow - CI/CD Deployment Project



TaskFlow is a simple Flask task management application created as a support application for a CI/CD deployment project.



\## Features



\- Add tasks

\- List tasks

\- Mark tasks as done

\- Delete tasks

\- Dashboard statistics



\## Technologies



\- Python

\- Flask

\- SQLite

\- HTML

\- CSS



\## Project Objective



The objective of this project is to use a simple web application as a support for implementing a CI/CD deployment workflow.



Workflow:



Code push → Pipeline trigger → Install dependencies → Run checks → Deploy to cloud → Verify application



\## Run Locally



```bash

python -m venv venv

venv\\\\Scripts\\\\activate

pip install -r requirements.txt

python app.py


