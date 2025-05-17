
# AWS EC2 Automation with Flask API 🚀

This project automates the process of launching an EC2 instance, executing a simple bash script, optionally fetching results, and safely terminating the instance — all exposed via a Flask API and testable through Postman.

---

## ✅ Features

- 🔹 Launch an EC2 (Amazon Linux 2) instance with a simple bash script
- 🔹 Script performs basic `echo` and `sleep` operations
- 🔹 (WIP) Fetch output using AWS SSM
- 🔹 Terminate instance safely
- 🔹 REST APIs built using Flask
- 🔹 Tested using Postman — **No frontend required**

---

## 📦 Technologies Used

- Python 3.8+
- Flask
- Boto3 (AWS SDK for Python)
- AWS EC2
- Postman (for testing)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RohithMarrapu/Scientiflow.git
cd Scientiflow
````

### 2. Set Up Environment

Make sure Python is installed:

```bash
python3 --version
```

Install required packages:

```bash
pip install boto3 flask
```

---

## 🔐 AWS Setup

Make sure you have:

* AWS credentials set via `~/.aws/credentials` or environment variables.
* An **existing EC2 key pair** (e.g., `cli-key.pem`) — *do not upload this to GitHub!*
* The `.pem` key is already `.gitignore`-ed to keep it secure.
* Optionally attach an IAM role to your instance to support SSM (for output fetching).

---

## 🚀 Running the App

```bash
python app.py
```

Server will run locally at `http://127.0.0.1:5000`

---

## 🧪 API Usage (Postman)

### ▶️ Launch Instance

* **Method**: `POST`
* **URL**: `http://127.0.0.1:5000/launch`

**Response**:

```json
{
  "message": "Instance launched",
  "id": "i-xxxxxxxxxxxxxxxxx"
}
```

---

### ⏹ Terminate Instance

* **Method**: `POST`
* **URL**: `http://127.0.0.1:5000/terminate`

**Response**:

```json
{
  "message": "Instance terminated"
}
```

---

## 📂 Project Structure

```
.
├── app.py                # Flask app exposing launch & terminate APIs
├── ec2_manager.py        # Core EC2 logic using boto3
├── .gitignore            # Ignores keys, environments, etc.
└── README.md             # You're reading it :)
```

---

## 🛡️ Security

* `.pem` and AWS credential files are ignored using `.gitignore`
* Make sure **you never upload your key files or credentials**

---

## 📸 Screenshots

### ✅ Launching an Instance via API (Postman)

![Launch Screenshot](screenshots/launch.png)

---

### ✅ Terminating the Instance via API

![Terminate Screenshot](screenshots/terminate.png)

---

## 💡 Future Work

* ✅ Add output fetching from instance via AWS SSM
* ⏳ Add input parameters for instance type, region, etc.
* 🧪 Add test cases and validations

---

## 🙋‍♂️ Contributor

**Rohith Marrapu**

---

## 📜 License

This project is open-sourced for educational and personal use.

```

---

### ✅ Final Checklist:
- Add two screenshots in a folder like `screenshots/launch.png` and `screenshots/terminate.png`
- Push everything (except `.pem` and `.env`) to GitHub

Let me know if you'd like the screenshots section preformatted for markdown drag-and-drop or if you'd like help building the output-fetching part using SSM.
```
