from fuzzy_logic import compute_risk
from utils import validate_inputs, format_result

def get_user_input():
   
    print("Heart Disease Risk Assessment using Fuzzy Logic")
    print("Please enter Your information:\n")
    
    inputs = {}
    
    inputs['age'] = int(input("Enter age: "))
    inputs['sex'] = int(input("Enter sex (0 = female, 1 = male): "))
    inputs['cp'] = int(input("Enter chest pain type (0-3): "))
    inputs['trestbps'] = int(input("Enter resting blood pressure: "))
    inputs['chol'] = int(input("Enter cholesterol level: "))
    inputs['fbs'] = int(input("Enter fasting blood sugar (0 = False, 1 = True): "))
    inputs['restecg'] = int(input("Enter resting ECG results (0-2): "))
    inputs['thalach'] = int(input("Enter maximum heart rate achieved: "))
    inputs['exang'] = int(input("Enter exercise-induced angina (0 = No, 1 = Yes): "))
    inputs['oldpeak'] = float(input("Enter oldpeak: "))
    inputs['slope'] = int(input("Enter slope (0-2): "))
    inputs['ca'] = int(input("Enter number of major vessels (0-3): "))
    inputs['thal'] = int(input("Enter thalassemia type (0-3): "))
    
    return inputs

def main():
    try:
        # Get user input
        inputs = get_user_input()
        
        is_valid, message = validate_inputs(inputs)
        if not is_valid:
            print(f"Error: {message}")
            return
     
        risk_level, risk_value = compute_risk(
            inputs['age'],
            inputs['sex'],
            inputs['cp'],
            inputs['trestbps'],
            inputs['chol'],
            inputs['fbs'],
            inputs['restecg'],
            inputs['thalach'],
            inputs['exang'],
            inputs['oldpeak'],
            inputs['slope'],
            inputs['ca'],
            inputs['thal']
        )

        print("\n" + format_result(risk_level, risk_value))
        
    except ValueError as e:
        print(f"Error: Invalid input . Please enter required numbers  . {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()