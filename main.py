import csv
from pathlib import Path
from collections import Counter
from logger_config import logger
from models import AutomotiveQualityRecord

# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "raw" / "quality_data.csv"


# --------------------------------------------------
# 2. Create synthetic automotive quality data
# --------------------------------------------------

def create_sample_data():

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    quality_records = [
        ["Plant", "Component", "Defect", "Supplier", "Quantity"],
        ["Plant_A", "Brake_Disc", "Crack", "Supplier_01", 15],
        ["Plant_A", "Brake_Disc", "Surface_Defect", "Supplier_01", 10],
        ["Plant_B", "Steering_Rack", "Leakage", "Supplier_02", 25],
        ["Plant_B", "Steering_Rack", "Leakage", "Supplier_02", 10],
        ["Plant_C", "Brake_Disc", "Crack", "Supplier_03", 20],
        ["Plant_A", "Suspension", "Dimension_Error", "Supplier_01", 12],
        ["Plant_C", "Suspension", "Dimension_Error", "Supplier_03", 8],
        ["Plant_B", "Brake_Disc", "Surface_Defect", "Supplier_02", 18],
    ]

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerows(quality_records)

    print("Sample quality data created successfully!")

def demonstrate_quality_model():

    record = AutomotiveQualityRecord(
        plant="Plant_A",
        component="Brake_Disc",
        supplier="Supplier_01",
        defect="Crack",
        quantity=15
    )

    errors = record.validate()

    if errors:

        logger.warning(
            "Invalid quality record: %s",
            errors
        )

    else:

        logger.info("Quality record validated successfully")

        record.display_record()

        cost = record.calculate_defect_cost(250)

        print("Estimated defect cost:", cost)

# --------------------------------------------------
# 3. Load quality data
# --------------------------------------------------

def load_quality_data():

    with open(DATA_FILE, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        records = []

        for row in reader:

            row["Quantity"] = int(row["Quantity"])

            records.append(row)

    return records


# --------------------------------------------------
# 4. Analyze quality data
# --------------------------------------------------

def analyze_quality(records):

    plant_defects = Counter()

    component_defects = Counter()

    defect_categories = Counter()

    supplier_defects = Counter()

    total_defects = 0

    for record in records:

        plant = record["Plant"]

        component = record["Component"]

        defect = record["Defect"]

        supplier = record["Supplier"]

        quantity = record["Quantity"]

        plant_defects[plant] += quantity

        component_defects[component] += quantity

        defect_categories[defect] += quantity

        supplier_defects[supplier] += quantity

        total_defects += quantity

    return {
        "total_defects": total_defects,
        "plant_defects": plant_defects,
        "component_defects": component_defects,
        "defect_categories": defect_categories,
        "supplier_defects": supplier_defects
    }


# --------------------------------------------------
# 5. Display quality report
# --------------------------------------------------

def display_report(results):

    print("\n" + "=" * 50)

    print("AUTOMOTIVE QUALITY ANALYZER")

    print("=" * 50)

    print("\nTotal Defects:", results["total_defects"])

    print("\nDefects by Plant:")

    for plant, quantity in results["plant_defects"].most_common():

        print(f"{plant}: {quantity}")

    print("\nDefects by Component:")

    for component, quantity in results["component_defects"].most_common():

        print(f"{component}: {quantity}")

    print("\nDefect Categories:")

    for defect, quantity in results["defect_categories"].most_common():

        print(f"{defect}: {quantity}")

    print("\nSupplier Defects:")

    for supplier, quantity in results["supplier_defects"].most_common():

        print(f"{supplier}: {quantity}")

    highest_defect_plant = results["plant_defects"].most_common(1)

    print("\nHighest Defect Plant:")

    print(
        highest_defect_plant[0][0],
        "with",
        highest_defect_plant[0][1],
        "defects"
    )

# --------------------------------------------------
# 6. Main application
# --------------------------------------------------

def main():

    logger.info("Automotive Quality Analyzer Started")

    create_sample_data()

    records = load_quality_data()

    logger.info("Quality data loaded successfully")

    results = analyze_quality(records)

    display_report(results)

    logger.info("Quality analysis completed")

    demonstrate_quality_model()


if __name__ == "__main__":

    main()