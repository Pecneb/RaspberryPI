from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from web.db import get_db
from web.auth import login_required

bp = Blueprint('events', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('events/index.html')