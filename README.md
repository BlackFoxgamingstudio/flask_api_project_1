# flask_api_project_1

run: gunicorn -w 4 main:app -b :5081

local test: Pass
curl http://127.0.0.1:8000 