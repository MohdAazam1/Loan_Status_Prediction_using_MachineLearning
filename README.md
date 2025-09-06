# Loan Approval Prediction App

## 📌 Project Overview
This project is a **Loan Approval Prediction Web Application** built with **Flask** and a trained **Machine Learning model**.  
It allows users to apply for loans, view their loan details, and get predictions on loan approval status.  
Admins can also log in to manage loan applications.  

---

## 🚀 Features
- User Registration & Login  
- Apply for a Loan  
- Loan Approval Prediction using ML model (`loan_approval_model.pkl`)  
- View My Loans section  
- Admin Dashboard for managing applications  
- Responsive UI with Flask Jinja templates  

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS (Jinja2 templates)  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Database:** (if included, SQLite/MySQL)  
- **Model Training:** Jupyter Notebook (`model.ipynb`)  

---

## 📂 Project Structure
```
Loan_app/
│── app.py                  # Flask application
│── loan_approval_model.pkl # Trained ML model
│── LoanApprovalPrediction.csv # Dataset
│── model.ipynb             # Jupyter Notebook for training
│── static/
│   └── style.css           # CSS styling
│── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── apply_loan.html
│   ├── my_loans.html
│   ├── loan_details.html
│   └── admin.html
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Loan_app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Access the app**  
   Open browser → `http://127.0.0.1:5000/`

---

## 📊 Model Training
- The ML model was trained using **LoanApprovalPrediction.csv** dataset.  
- Training steps are available in **model.ipynb**.  
- Final model is saved as `loan_approval_model.pkl`.  

---

## 🔐 Authentication
- Users can **register/login** to apply for loans.  
- Admin has a separate login for managing applications.  

---

## 📸 Screenshots
*(Add relevant screenshots of the app UI here)*  

---

## 👨‍💻 Author
Developed by **[Your Name]**  
