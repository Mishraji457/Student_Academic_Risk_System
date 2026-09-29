def find_risk(score):
    if score >= 75:
        return "Low Risk"
    elif score >= 50:
        return "Medium Risk"
    else:
        return "High Risk"