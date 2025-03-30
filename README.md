# 🫀 Heart Disease Risk Assessment using Fuzzy Logic


## 📌 Overview
This project implements a **Fuzzy Logic System** to assess the risk of heart disease based on various health parameters. Using **SciKit-Fuzzy**, the system takes user inputs such as age, cholesterol levels, and ECG results, and predicts the likelihood of heart disease.

## 🚀 Features
✅ User-friendly input system for health data collection  
✅ Implements **Fuzzy Logic** for decision-making  
✅ Uses **SkFuzzy** for defining membership functions  
✅ Validates user inputs for consistency  
✅ Provides a **risk level (Low, Medium, High)** based on computed scores  
✅ Fully modular with separate logic for **validation, computation, and formatting**  
✅ Easy to extend with additional features in the future  

## 📂 Project Structure
```
📁 HeartDiseaseRiskAssessment
 ├── fuzzy_logic.py         # Fuzzy logic implementation
 ├── utils.py               # Validation and formatting functions
 ├── main.py                # User input handling & execution
 ├── requirements.txt       # Required dependencies
 ├── README.md              # Project documentation
```

## 📥 Installation
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/heart-disease-fuzzy.git
cd heart-disease-fuzzy
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

## ▶️ Usage
Run the script and enter the required health information:
```bash
python main.py
```
Follow the prompts to enter health parameters. The system will output the computed risk level.

## 🛠️ Technologies Used
- **Python** 🐍
- **Scikit-Fuzzy** 🤖
- **NumPy** 🔢

## 📊 How it Works
1️⃣ **User enters health parameters** (e.g., Age, Cholesterol, ECG, etc.)  
2️⃣ **Validation module** ensures inputs are within a valid range  
3️⃣ **Fuzzy logic system** applies rules and membership functions  
4️⃣ **Risk level is computed** (Low, Medium, High)  
5️⃣ **Formatted output** is displayed to the user  

## 🎯 Future Enhancements
🔹 Web-based UI for easier input and visualization  
🔹 Integration with **Machine Learning models** for hybrid decision-making  
🔹 Database storage for patient history tracking  

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests and improve this system.

## 📜 License
This project is licensed under the MIT License.

---
💡 **"Prevention is better than cure. Detect risks early!"**

