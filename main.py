from services.data_manager import DataManager, HistoryManager
from services.diagnosis import DiagnosisEngine
from services.image_analyzer import LeafImageAnalyzer, load_image
from utils.helpers import choose_from_list, pause


DATA_FILE = "data/diseases.csv"
HISTORY_FILE = "data/diagnosis_history.csv"


def symptom_diagnosis(data_manager, engine, history_manager):
    crop = choose_from_list(data_manager.get_crops(), "Available crops")
    diseases = data_manager.get_diseases_by_crop(crop)

    known_symptoms = sorted({
        symptom
        for disease in diseases
        for symptom in disease.symptoms
    })

    print("\nSymptoms available in the dataset:")
    for symptom in known_symptoms:
        print(f"- {symptom}")

    raw = input("\nEnter observed symptoms separated by commas: ")
    symptoms = [item.strip() for item in raw.split(",") if item.strip()]

    if not symptoms:
        print("No symptoms entered.")
        return

    results = engine.diagnose(crop, symptoms)
    engine.display_results(results)

    if results and results[0]["score"] > 0:
        best = results[0]["disease"]
        print("\n===== TOP RESULT DETAILS =====")
        best.describe()
        history_manager.save_record(crop, symptoms, best.name)
    else:
        print("\nNo disease matched the supplied symptoms.")


def image_diagnosis(data_manager, engine):
    path = input("\nEnter image path: ").strip()
    image = load_image(path)
    if image is None:
        return

    try:
        analyzer = LeafImageAnalyzer(image)
        analysis = analyzer.analyze()

        print("\n===== IMAGE ANALYSIS =====")
        for key, value in analysis.items():
            if key.endswith("percentage"):
                print(f"{key}: {value:.2f}%")

        symptoms = analyzer.generate_symptoms()
        print("\nDetected symptoms:")
        if symptoms:
            for symptom in symptoms:
                print(f"- {symptom}")
        else:
            print("- No rule-defined symptoms detected.")
            return

        crop = choose_from_list(data_manager.get_crops(), "Select crop")
        results = engine.diagnose(crop, symptoms)
        engine.display_results(results)

    except ValueError as exc:
        print(f"Image analysis error: {exc}")


def disease_information(data_manager):
    name = input("\nEnter disease name: ").strip()
    disease = data_manager.search_disease(name)
    if disease:
        disease.describe()
    else:
        print("Disease not found.")


def main():
    try:
        data_manager = DataManager(DATA_FILE)
    except RuntimeError as exc:
        print(exc)
        return

    engine = DiagnosisEngine(data_manager.diseases)
    history_manager = HistoryManager(HISTORY_FILE)

    print("\n======================================")
    print("   CROP DISEASE IDENTIFICATION SYSTEM")
    print("======================================")

    while True:
        print("""
1. Symptom-based diagnosis
2. Image-based diagnosis
3. Disease information
4. Dataset report
5. Diagnosis history
6. Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            symptom_diagnosis(data_manager, engine, history_manager)
            pause()
        elif choice == "2":
            image_diagnosis(data_manager, engine)
            pause()
        elif choice == "3":
            disease_information(data_manager)
            pause()
        elif choice == "4":
            data_manager.generate_report()
            pause()
        elif choice == "5":
            history_manager.show_history()
            pause()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()
