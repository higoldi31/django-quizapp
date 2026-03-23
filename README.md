# 🧠 Django Quiz App

A web-based Quiz Application built using Django that displays one question per page, records user answers, and calculates the final score at the end.

---

## 🚀 Features

- ✅ One question per page
- ✅ Dynamic choices from database
- ✅ Next button navigation
- ✅ Finish button on last question
- ✅ Session-based answer tracking
- ✅ Automatic score calculation
- ✅ Clean and simple UI (Bootstrap)

---

## 🛠️ Tech Stack

- Python
- Django
- HTML
- Bootstrap
- SQLite (default DB)

---

## 📂 Project Structure
quizapp/
│
├── quiz/ # Main app
│ ├── models.py # Question & Choice models
│ ├── views.py # Quiz logic
│ ├── urls.py # Routing
│ └── templates/
│ └── quiz/
│ ├── index.html
│ ├── question_base.html
│ └── results.html
│
├── db.sqlite3
└── manage.py
---

## ⚙️ How It Works

1. User starts quiz from homepage
2. One question is displayed at a time
3. User selects an answer and clicks "Next"
4. Answer is stored using Django sessions
5. Process repeats until last question
6. Final score is calculated and displayed

---

## 🧠 Key Concepts Used

- Django Models (ForeignKey relationships)
- Views & URL Routing
- Templates & Template Tags
- Sessions (for storing answers)
- POST Requests & Form Handling

---
## 🙌 Acknowledgements

Built as a learning project to understand Django fundamentals and backend development.

---
