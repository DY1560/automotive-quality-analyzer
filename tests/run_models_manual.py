import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from models import AutomotiveQualityRecord


# -----------------------------------------
# Create a quality record
# -----------------------------------------

record = AutomotiveQualityRecord(
    plant="Plant_A",
    component="Brake_Disc",
    supplier="Supplier_01",
    defect="Crack",
    quantity=15
)


# -----------------------------------------
# Display record
# -----------------------------------------

record.display_record()


# -----------------------------------------
# Validate record
# -----------------------------------------

errors = record.validate()

print("\nValidation Errors:", errors)


# -----------------------------------------
# Calculate defect cost
# -----------------------------------------

cost = record.calculate_defect_cost(
    cost_per_defect=250
)

print("\nEstimated Defect Cost:", cost)