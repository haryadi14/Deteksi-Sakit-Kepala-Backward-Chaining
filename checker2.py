symptoms = {"headache": False, "nausea": False, "dizziness": False, "fever": False, }

diseases = {"migraine": {"headache": True, "nausea": True}, "flu": {"fever": True},
    "ear infection": {"ear pain": True}, }


# Define the rules
def rule_migraine(symptoms):
    if symptoms["headache"] and symptoms["nausea"]:
        return True
    return False


def rule_flu(symptoms):
    if symptoms["fever"]:
        return True
    return False


def rule_ear_infection(symptoms):
    if symptoms["ear pain"]:
        return True
    return False


# Define the backward chaining algorithm
def diagnose(symptom, diseases, symptoms):
    if symptom in diseases:
        for cause in diseases[symptom]:
            if not symptoms[cause]:
                diagnose(cause, diseases, symptoms)
        if not rule_migraine(symptoms):
            return
        print("You have migraine.")
    else:
        print("Unknown symptom.")


# Test the diagnosis
symptoms["headache"] = True
symptoms["nausea"] = True
diagnose("headache", diseases, symptoms)
