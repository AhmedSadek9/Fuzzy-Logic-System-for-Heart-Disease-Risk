def validate_inputs(inputs):
    """
    Validate input ranges for heart disease risk assessment.
    Returns (is_valid, error_message) tuple.
    """
    age = inputs.get('age')
    sex = inputs.get('sex')
    cp = inputs.get('cp')
    trestbps = inputs.get('trestbps')
    chol = inputs.get('chol')
    fbs = inputs.get('fbs')
    restecg = inputs.get('restecg')
    thalach = inputs.get('thalach')
    exang = inputs.get('exang')
    oldpeak = inputs.get('oldpeak')
    slope = inputs.get('slope')
    ca = inputs.get('ca')
    thal = inputs.get('thal')
    
    if age is None or not (0 <= age <= 120):
        return False, "Age must be between 0 and 120"
    if sex is None or sex not in [0, 1]:
        return False, "Sex must be 0 (female) or 1 (male)"
    if cp is None or not (0 <= cp <= 3):
        return False, "Chest pain type must be between 0 and 3"
    if trestbps is None or not (0 <= trestbps <= 200):
        return False, "Resting blood pressure must be between 0 and 200"
    if chol is None or not (0 <= chol <= 600):
        return False, "Cholesterol level must be between 0 and 600"
    if fbs is None or fbs not in [0, 1]:
        return False, "Fasting blood sugar must be 0 (False) or 1 (True)"
    if restecg is None or not (0 <= restecg <= 2):
        return False, "Resting ECG results must be between 0 and 2"
    if thalach is None or not (0 <= thalach <= 220):
        return False, "Maximum heart rate must be between 0 and 220"
    if exang is None or exang not in [0, 1]:
        return False, "Exercise-induced angina must be 0 (No) or 1 (Yes)"
    if oldpeak is None or not (0 <= oldpeak <= 6.9):
        return False, "Oldpeak must be between 0 and 6.9"
    if slope is None or not (0 <= slope <= 2):
        return False, "Slope must be between 0 and 2"
    if ca is None or not (0 <= ca <= 3):
        return False, "Number of major vessels must be between 0 and 3"
    if thal is None or not (0 <= thal <= 3):
        return False, "Thalassemia type must be between 0 and 3"
    
    return True, "All inputs are valid"

def format_result(risk_level, risk_value):
    """
    Format the result for display.
    """
    return f"Heart Disease Risk Level: {risk_level} (Score: {risk_value:.2f})"