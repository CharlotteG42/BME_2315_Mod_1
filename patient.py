class Patient:
    ## The constructor sets up the attributes for each patient object.
    def __init__(self, donor_id, sex, apoe, p_tau, abeta40, abeta42):
        self.donor_id = donor_id
        self.sex = sex
        self.apoe = apoe
        self.p_tau = p_tau
        self.abeta40 = abeta40
        self.abeta42 = abeta42

    ## This representer controls what prints when we print a patient.
    def __repr__(self):
        return f"Patient({self.donor_id}, Sex={self.sex}, APOE={self.apoe})"

    ## Class method to filter patients based on two attributes.
    def filter_patients(patient_list, sex_choice, apoe_choice):
        result = []
        for p in patient_list:
            if p.sex == sex_choice and p.apoe == apoe_choice:
                result.append(p)
        return result
