import os
import pandas as pd

from services.disease_factory import DiseaseFactory


class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.DataFrame()
        self.diseases = []
        self.load_data()

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            self.diseases = [
                DiseaseFactory.create_disease(row)
                for _, row in self.data.iterrows()
            ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset not found: {self.file_path}")
        except Exception as exc:
            raise RuntimeError(f"Could not load dataset: {exc}") from exc

    def get_crops(self):
        return sorted({disease.crop for disease in self.diseases})

    def get_diseases_by_crop(self, crop):
        return [
            disease for disease in self.diseases
            if disease.crop.lower() == crop.lower()
        ]

    def search_disease(self, name):
        for disease in self.diseases:
            if disease.name.lower() == name.lower():
                return disease
        return None

    def generate_report(self):
        print("\n===== DATASET REPORT =====")
        print(f"Total disease records: {len(self.diseases)}")
        print(f"Total crops: {len(self.get_crops())}")
        print("Crops:")
        for crop in self.get_crops():
            print(f"- {crop}")


class HistoryManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_record(self, crop, symptoms, diagnosis):
        record = pd.DataFrame([{
            "crop": crop,
            "symptoms": ", ".join(symptoms),
            "diagnosis": diagnosis,
        }])

        exists = os.path.exists(self.file_path)
        record.to_csv(
            self.file_path,
            mode="a" if exists else "w",
            header=not exists,
            index=False,
        )

    def show_history(self):
        if not os.path.exists(self.file_path):
            print("\nNo diagnosis history yet.")
            return

        history = pd.read_csv(self.file_path)
        if history.empty:
            print("\nNo diagnosis history yet.")
            return

        print("\n===== DIAGNOSIS HISTORY =====")
        print(history.to_string(index=False))
