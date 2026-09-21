class DiagnosisEngine:
    def __init__(self, diseases):
        self.diseases = diseases

    def diagnose(self, crop, symptoms):
        candidates = [
            disease for disease in self.diseases
            if disease.crop.lower() == crop.lower()
        ]

        observed = {s.strip().lower() for s in symptoms if s.strip()}
        results = []

        for disease in candidates:
            score = disease.get_match_score(observed)
            total = len(disease.symptoms)
            percentage = (score / total * 100) if total else 0

            results.append({
                "disease": disease,
                "score": score,
                "percentage": percentage,
            })

        return sorted(
            results,
            key=lambda item: (item["percentage"], item["score"]),
            reverse=True,
        )

    def display_results(self, results):
        print("\n===== DIAGNOSIS RESULTS =====")

        if not results:
            print("No matching diseases found.")
            return

        for index, result in enumerate(results[:5], start=1):
            disease = result["disease"]
            print(
                f"{index}. {disease.name} | "
                f"match: {result['percentage']:.1f}% | "
                f"severity: {disease.severity} | "
                f"type: {disease.disease_type()}"
            )
