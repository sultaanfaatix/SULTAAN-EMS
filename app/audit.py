from flask import request
from flask_login import current_user

from . import db
from .models import AuditLog


def audit(action, details=""):
    username = "anonymous"
    if current_user and current_user.is_authenticated:
        username = current_user.username
    forwarded_for = request.headers.get("X-Forwarded-For", "")
    ip_address = forwarded_for.split(",")[0].strip() or request.remote_addr
    db.session.add(AuditLog(username=username, ip_address=ip_address, action=action, details=details))

