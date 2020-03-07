from flask import Flask
import secrets
import  datetime

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(256)
app.permanent_session_lifetime = datetime.timedelta(days=1)

from app import views
from app import admin_views