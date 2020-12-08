from app import app
import os
from datetime import datetime, date, time

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    date_time = datetime.today()
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!</br>{date_time}</br><img src='https://ananyev.me/images/profile-img.jpg'>"

    return "Hello from Flask"
