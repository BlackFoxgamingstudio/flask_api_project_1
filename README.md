# flask_api_project_1
 - 2nd Derivative Overview - Center of Excellence

# BF Design Principles:
    - Always use general available doc
    - Always create check list of actionable steps
    - Always keep a repository of your research & development

# Problem Overview:
This project is designed to address complexity of Technical github Projects. Many tech evangelists desire quick execution of demos to educate communities on highly technical concepts like “the Cloud and AI”. Due to the high learning curve for Github, DevOps and automation Blackfox R&D feels it is necessary to Build a Simple, scalable solution.*
	
# Use Case:
Using OpenAI we can provide communities with a clear action checklist to help them deploy any repository and its content to the cloud.

# Solution Overview:
By creating a Ci/CD devops pipe, using MongoDB, a Flask API and OpenAI’s REST API, BlackFox Studio has created a Scalable Microservice to provide a “Training Service” as a COE Project deliverable.

# DEMO:
https://blackfoxgamingstudio.github.io/black_lion_blogs/checklist_demo.html

# API:
https://github-search-v5sx.onrender.com/

# Repo:
https://github.com/BlackFoxgamingstudio/flask_api_project_1
documentation: README

# Run: 
gunicorn -w 4 main:app -b :5081

# Local test: - Pass
curl http://localhost:8000/getChecklist/https://github.com/pulumi/examples

# Project Website: 
 - https://sites.google.com/blackfoxstudios.org/blackfoxstudios/coming-soon/center-of-excellence?authuser=4