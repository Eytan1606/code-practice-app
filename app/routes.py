from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from app.models import User, Attempt
import io
from contextlib import redirect_stdout
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        new_user = User(username=username)
        new_user.set_password(password)  # ⬅️ הצפנת הסיסמה כאן

        db.session.add(new_user)
        db.session.commit()

        flash('Registered successfully! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):  # ⬅️ בדיקת סיסמה עם הצפנה
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))



# Dashboard (optional, example)
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f"<h2>Welcome, user #{session['user_id']}!</h2>"
    else:
        return redirect(url_for('login'))


@app.route('/practice', methods=['GET', 'POST'])
def practice():
    output = ''
    code = request.form.get('code', '') if request.method == 'POST' else ''
    try:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exec(code, {})
        output = buffer.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"

        if 'user_id' in session:
            attempt = Attempt(user_id=session['user_id'], code=code, output=output)
            db.session.add(attempt)
            db.session.commit()

    return render_template('practice.html', code=code, output=output)



# User’s code history route
@app.route('/attempts')
def view_attempts():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    attempts = Attempt.query\
        .filter_by(user_id=session['user_id'])\
        .order_by(Attempt.timestamp.desc())\
        .all()

    return render_template('attempts.html', attempts=attempts)

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    attempts = Attempt.query.filter_by(user_id=session['user_id']).order_by(Attempt.timestamp.desc()).all()
    return render_template('history.html', attempts=attempts)



@app.route('/delete_attempt/<int:attempt_id>', methods=['POST'])
def delete_attempt(attempt_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    attempt = Attempt.query.get_or_404(attempt_id)
    if attempt.user_id != session['user_id']:
        flash("Unauthorized access")
        return redirect(url_for('history'))

    db.session.delete(attempt)
    db.session.commit()
    flash("Attempt deleted.")
    return redirect(url_for('history'))


