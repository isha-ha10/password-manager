# 📌 Password Manager (Tkinter GUI)

A simple and functional **Password Manager application** built using Python and Tkinter.  
It allows users to generate secure passwords, store login details, and copy passwords to the clipboard instantly.

---

## 🚀 Features

- 🔐 **Password Generator**
  - Generates strong random passwords using:
    - Letters (uppercase & lowercase)
    - Numbers
    - Symbols
  - Automatically copies password to clipboard (via `pyperclip`)

- 💾 **Save Credentials**
  - Stores:
    - Website
    - Email/Username
    - Password
  - Saves data locally in a `data.txt` file

- ⚠️ **Input Validation**
  - Prevents saving empty fields
  - Confirmation popup before saving data

- 🖥️ **User-Friendly GUI**
  - Built with Tkinter
  - Clean layout with labels, input fields, and buttons

---

## 🛠️ Tech Stack

- Python
- Tkinter (GUI)
- random module
- pyperclip

---

## 📂 Project Structure

```
password-manager/
│── main.py
│── data.txt
│── logo.png
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository:
```
git clone https://github.com/isha-ha10/password-manager.git
```

2. Navigate to the project folder:
```
cd password-manager
```

3. Install dependencies:
```
pip install pyperclip
```

4. Run the app:
```
python main.py
```

---

## 📸 Preview

<img width="1603" height="904" alt="image" src="https://github.com/user-attachments/assets/71fe695c-0475-40ca-9315-31248f4fce5a" />


---

## 💡 Future Improvements

- Save data in JSON instead of text file
- Add search functionality
- Add encryption for better security
- Improve UI (themes / dark mode)

---

## 👤 Author

- Isha

---

## ⚠️ Note

This project is for learning purposes and does not include encryption.  
Do not use it to store highly sensitive real-world passwords.

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
