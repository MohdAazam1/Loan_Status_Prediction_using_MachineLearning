from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkey"  # session encryption

# -----------------------------
# Flask-Mail Config (use Gmail SMTP as example)
# -----------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'your_app_password'      # Use App Password, not Gmail password

mail = Mail(app)

# -----------------------------
# Fake DB (in-memory)
# -----------------------------
users = {
    "admin": {"password": "admin123", "role": "admin", "email": "admin@example.com"},
    "john": {"password": "john123", "role": "user", "email": "john@example.com"},
}

loan_applications = []

# -----------------------------
# Routes
# -----------------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/apply-loan', methods=['GET', 'POST'])
def apply_loan():
    if not session.get('username'):
        flash("Please log in to apply for a loan", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = {
            "id": len(loan_applications) + 1,
            "name": session['username'],
            "amount": request.form['amount'],
            "address": request.form['address'],
            "status": "Pending",
            "history": ["Application submitted (Pending)"]
        }
        loan_applications.append(data)
        flash("Loan Application Submitted Successfully!", "success")
        return redirect(url_for('home'))
    return render_template('apply_loan.html')

# -----------------------------
# Login / Logout
# -----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            flash(f"Welcome {username}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "info")
    return redirect(url_for('home'))

# -----------------------------
# Admin Panel
# -----------------------------
@app.route('/admin')
def admin():
    if session.get('role') != 'admin':
        flash("Admin access only!", "danger")
        return redirect(url_for('login'))
    return render_template('admin.html', loans=loan_applications)

@app.route('/update-loan/<int:loan_id>/<string:status>')
def update_loan(loan_id, status):
    if session.get('role') != 'admin':
        flash("Admin access only!", "danger")
        return redirect(url_for('login'))

    for loan in loan_applications:
        if loan["id"] == loan_id:
            loan["status"] = status.capitalize()
            loan["history"].append(f"Loan {status.capitalize()} by Admin")

            # Send email notification
            user_email = users[loan["name"]]["email"]
            subject = f"Loan #{loan_id} {status.capitalize()}"
            body = f"Hello {loan['name']},\n\nYour loan application (Amount: {loan['amount']}) has been {status.capitalize()}.\n\nThank you."
            try:
                msg = Message(subject, recipients=[user_email], body=body, sender=app.config['MAIL_USERNAME'])
                mail.send(msg)
                flash(f"Loan #{loan_id} marked as {status}. Email sent to {user_email}.", "info")
            except Exception as e:
                flash(f"Loan #{loan_id} marked as {status}, but email failed: {e}", "danger")
            break

    return redirect(url_for('admin'))

# -----------------------------
# User Loan History
# -----------------------------
@app.route('/my-loans')
def my_loans():
    if not session.get('username'):
        flash("Login required to view your loans", "warning")
        return redirect(url_for('login'))
    user_loans = [loan for loan in loan_applications if loan['name'] == session['username']]
    return render_template('my_loans.html', loans=user_loans)

# -----------------------------
# Loan Details (with history)
# -----------------------------
@app.route('/loan/<int:loan_id>')
def loan_details(loan_id):
    if not session.get('username'):
        flash("Login required to view loan details", "warning")
        return redirect(url_for('login'))

    loan = next((l for l in loan_applications if l["id"] == loan_id), None)

    if not loan:
        flash("Loan not found!", "danger")
        return redirect(url_for('home'))

    # Users can only view their own loan
    if session.get('role') != 'admin' and loan['name'] != session['username']:
        flash("Access denied!", "danger")
        return redirect(url_for('home'))

    return render_template('loan_details.html', loan=loan)

if __name__ == '__main__':
    app.run(debug=True)
