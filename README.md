# Language Detection Model

A web-based application that detects the language of a given text using a Naive Bayes algorithm. The project uses a trained machine learning model and a user-friendly web interface powered by Flask.

---

## Features

- Detects the language of input text from a pre-defined dataset.
- Trained using the Naive Bayes algorithm.
- Web interface for users to input text and view results in real-time.
- Easily extendable for additional languages.

---

## Tech Stack

- **Backend**: Python, Flask, Scikit-learn
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for styling)
- **Database**: CSV file for the dataset
- **Environment**: Virtual Environment for dependency management

---

## Installation and Setup

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-URL>
   cd Language-Detection-Model
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
3. **Activate Virtual Environment**:
    ```bash
   venv\Scripts\activate
4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
5. **Run the Application**:
   ```bash
   python app.py

The application will run locally at http://127.0.0.1:5000/.
