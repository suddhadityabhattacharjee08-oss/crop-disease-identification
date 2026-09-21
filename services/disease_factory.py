from models.disease import (
    BacterialDisease,
    FungalDisease,
    PestDisease,
    ViralDisease,
)


class DiseaseFactory:
    @staticmethod
    def create_disease(row):
        disease_type = str(row["type"]).strip().lower()
        symptoms = [s.strip() for s in str(row["symptoms"]).split(";") if s.strip()]

        classes = {
            "fungal": FungalDisease,
            "bacterial": BacterialDisease,
            "viral": ViralDisease,
            "pest": PestDisease,
        }

        if disease_type not in classes:
            raise ValueError(f"Unknown disease type: {row['type']}")

        return classes[disease_type](
            str(row["name"]),
            str(row["crop"]),
            symptoms,
            str(row["severity"]),
            str(row["treatment"]),
            str(row["prevention"]),
        )
