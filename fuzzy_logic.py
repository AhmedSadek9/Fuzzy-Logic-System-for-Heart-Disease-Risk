import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def define_membership_functions():
    # Antecedent/Consequent objects hold universe variables and membership functions
    age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
    sex = ctrl.Antecedent(np.arange(0, 2, 1), 'sex')  # 0 = female, 1 = male
    cp = ctrl.Antecedent(np.arange(0, 4, 1), 'cp')  # chest pain type
    trestbps = ctrl.Antecedent(np.arange(0, 201, 1), 'trestbps')  # resting blood pressure
    chol = ctrl.Antecedent(np.arange(0, 601, 1), 'chol')  # cholesterol level
    fbs = ctrl.Antecedent(np.arange(0, 2, 1), 'fbs')  # fasting blood sugar
    restecg = ctrl.Antecedent(np.arange(0, 3, 1), 'restecg')  # resting ECG results
    thalach = ctrl.Antecedent(np.arange(0, 221, 1), 'thalach')  # max heart rate achieved
    exang = ctrl.Antecedent(np.arange(0, 2, 1), 'exang')  # exercise-induced angina
    oldpeak = ctrl.Antecedent(np.arange(0, 7, 0.1), 'oldpeak')  # ST depression induced by exercise
    slope = ctrl.Antecedent(np.arange(0, 3, 1), 'slope')  # slope of peak exercise ST segment
    ca = ctrl.Antecedent(np.arange(0, 4, 1), 'ca')  # number of major vessels
    thal = ctrl.Antecedent(np.arange(0, 4, 1), 'thal')  # thalassemia type
    
    risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')  # heart disease risk level

    # Auto-membership function population for some variables
    for var in [age, trestbps, chol, thalach, oldpeak]:
        var.automf(3, names=['low', 'medium', 'high'])
    
    # Custom membership functions for other variables
    sex['female'] = fuzz.trimf(sex.universe, [0, 0, 1])
    sex['male'] = fuzz.trimf(sex.universe, [0, 1, 1])
    
    cp['typical'] = fuzz.trimf(cp.universe, [0, 0, 1])
    cp['atypical'] = fuzz.trimf(cp.universe, [0, 1, 2])
    cp['non-anginal'] = fuzz.trimf(cp.universe, [1, 2, 3])
    cp['asymptomatic'] = fuzz.trimf(cp.universe, [2, 3, 3])
    
    fbs['false'] = fuzz.trimf(fbs.universe, [0, 0, 1])
    fbs['true'] = fuzz.trimf(fbs.universe, [0, 1, 1])
    
    restecg['normal'] = fuzz.trimf(restecg.universe, [0, 0, 1])
    restecg['stt'] = fuzz.trimf(restecg.universe, [0, 1, 2])  # ST-T wave abnormality
    restecg['hypertrophy'] = fuzz.trimf(restecg.universe, [1, 2, 2])
    
    exang['no'] = fuzz.trimf(exang.universe, [0, 0, 1])
    exang['yes'] = fuzz.trimf(exang.universe, [0, 1, 1])
    
    slope['upsloping'] = fuzz.trimf(slope.universe, [0, 0, 1])
    slope['flat'] = fuzz.trimf(slope.universe, [0, 1, 2])
    slope['downsloping'] = fuzz.trimf(slope.universe, [1, 2, 2])
    
    ca['none'] = fuzz.trimf(ca.universe, [0, 0, 1])
    ca['one'] = fuzz.trimf(ca.universe, [0, 1, 2])
    ca['two'] = fuzz.trimf(ca.universe, [1, 2, 3])
    ca['three'] = fuzz.trimf(ca.universe, [2, 3, 3])
    
    thal['normal'] = fuzz.trimf(thal.universe, [0, 0, 1])
    thal['fixed'] = fuzz.trimf(thal.universe, [0, 1, 2])  # fixed defect
    thal['reversible'] = fuzz.trimf(thal.universe, [1, 2, 2])  # reversible defect
    
    # Output membership functions
    risk['low'] = fuzz.trimf(risk.universe, [0, 0, 50])
    risk['medium'] = fuzz.trimf(risk.universe, [0, 50, 100])
    risk['high'] = fuzz.trimf(risk.universe, [50, 100, 100])
    
    return {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal,
        'risk': risk
    }

def define_fuzzy_rules(membership_functions):
    age = membership_functions['age']
    sex = membership_functions['sex']
    cp = membership_functions['cp']
    trestbps = membership_functions['trestbps']
    chol = membership_functions['chol']
    fbs = membership_functions['fbs']
    restecg = membership_functions['restecg']
    thalach = membership_functions['thalach']
    exang = membership_functions['exang']
    oldpeak = membership_functions['oldpeak']
    slope = membership_functions['slope']
    ca = membership_functions['ca']
    thal = membership_functions['thal']
    risk = membership_functions['risk']
    
    rules = [
        # High risk rules
        ctrl.Rule(chol['high'] & trestbps['high'], risk['high']),
        ctrl.Rule(cp['asymptomatic'] & thalach['low'], risk['high']),
        ctrl.Rule(oldpeak['high'] & slope['downsloping'], risk['high']),
        ctrl.Rule(ca['three'] | thal['reversible'], risk['high']),
        ctrl.Rule(age['high'] & sex['male'] & exang['yes'], risk['high']),
        
        # Medium risk rules
        ctrl.Rule(chol['medium'] & trestbps['medium'], risk['medium']),
        ctrl.Rule(cp['non-anginal'] & thalach['medium'], risk['medium']),
        ctrl.Rule(oldpeak['medium'] & slope['flat'], risk['medium']),
        ctrl.Rule(ca['one'] | ca['two'], risk['medium']),
        ctrl.Rule(age['medium'] & (sex['male'] | exang['yes']), risk['medium']),
        
        # Low risk rules
        ctrl.Rule(age['low'] & thalach['high'], risk['low']),
        ctrl.Rule(cp['typical'] & restecg['normal'], risk['low']),
        ctrl.Rule(oldpeak['low'] & slope['upsloping'], risk['low']),
        ctrl.Rule(sex['female'] & fbs['false'] & thal['normal'], risk['low']),
        ctrl.Rule(ca['none'] & chol['low'], risk['low'])
    ]
    
    return rules

def compute_risk(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Define membership functions and rules
    membership_functions = define_membership_functions()
    rules = define_fuzzy_rules(membership_functions)
    
    # Create control system
    risk_ctrl = ctrl.ControlSystem(rules)
    risk_simulation = ctrl.ControlSystemSimulation(risk_ctrl)
    
    # Input values
    risk_simulation.input['age'] = age
    risk_simulation.input['sex'] = sex
    risk_simulation.input['cp'] = cp
    risk_simulation.input['trestbps'] = trestbps
    risk_simulation.input['chol'] = chol
    risk_simulation.input['fbs'] = fbs
    risk_simulation.input['restecg'] = restecg
    risk_simulation.input['thalach'] = thalach
    risk_simulation.input['exang'] = exang
    risk_simulation.input['oldpeak'] = oldpeak
    risk_simulation.input['slope'] = slope
    risk_simulation.input['ca'] = ca
    risk_simulation.input['thal'] = thal
    
    # Compute the result
    risk_simulation.compute()
    
    # Get the crisp output value
    risk_value = risk_simulation.output['risk']
    
    # Classify into low, medium, or high
    if risk_value <= 33:
        return 'Low', risk_value
    elif risk_value <= 66:
        return 'Medium', risk_value
    else:
        return 'High', risk_value