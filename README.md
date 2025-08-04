# 🚗 Car Calculator

**Car Calculator** is an interactive web application that helps you choose the right type of car based on your financial capacity, lifestyle, and professional profile. The app calculates an estimated car budget and suggests the most suitable car category for you.

---

## ✅ Features
✔ Calculate the maximum car value based on your yearly income  
✔ Adjust calculations if you already own a car  
✔ Select personal and professional details to get the ideal car category  
✔ See recommendations for popular car types  
✔ User-friendly **Streamlit interface**  

---

## 🛠 Tech Stack
- **Python 3.10+**
- [Streamlit](https://streamlit.io/) for the web UI
- [Pandas](https://pandas.pydata.org/) for data handling (optional)

---

## 📂 Project Structure
Car-Calculator/
│
├── front_end_Car_calculator.py # Main Streamlit application
├── requirements.txt # Project dependencies
└── README.md # Documentation

yaml
Copy
Edit

---

## ✅ Installation & Usage

1. Clone the repository
```bash
git clone https://github.com/LyubomirKrasenov/Car-calculator.git
cd Car-calculator

2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Run the Streamlit app
bash
Copy
Edit
streamlit run front_end_Car_calculator.py
