class Disease:
    def __init__(self, name, crop, symptoms, severity, treatment, prevention):
        self.name = name
        self.crop = crop
        self.symptoms = symptoms
        self.severity = severity
        self.treatment = treatment
        self.prevention = prevention

    def describe(self):
        print(f"\nDisease: {self.name}")
        print(f"Crop: {self.crop}")
        print(f"Type: {self.disease_type()}")
        print(f"Severity: {self.severity}")
        print("\nSymptoms:")
        for symptom in self.symptoms:
            print(f"- {symptom}")
        print("\nTreatment:")
        print(self.treatment)
        print("\nPrevention:")
        print(self.prevention)

    def get_match_score(self, observed_symptoms):
        known = {s.strip().lower() for s in self.symptoms}
        observed = {s.strip().lower() for s in observed_symptoms}
        return len(known.intersection(observed))

    def disease_type(self):
        return "General"

    def __str__(self):
        return f"{self.name} ({self.crop})"


class FungalDisease(Disease):
    def disease_type(self):
        return "Fungal"


class BacterialDisease(Disease):
    def disease_type(self):
        return "Bacterial"


class ViralDisease(Disease):
    def disease_type(self):
        return "Viral"


class PestDisease(Disease):
    def disease_type(self):
        return "Pest"
