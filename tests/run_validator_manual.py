import sys
from pathlib import Path

# Add project source directory to Python path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from validator import validate_record


# -----------------------------------------
# Test 1: Valid record
# -----------------------------------------

valid_record = {
    "Plant": "Plant_A",
    "Component": "Brake_Disc",
    "Defect": "Crack",
    "Supplier": "Supplier_01",
    "Quantity": 2015
}

errors = validate_record(valid_record)

print("Valid Record Errors:", errors)


# -----------------------------------------
# Test 2: Negative quantity
# -----------------------------------------

invalid_record = {
    "Plant": "Plant_B",
    "Component": "Steering_Rack",
    "Defect": "Leakage",
    "Supplier": "Supplier_02",
    "Quantity": -10
}

errors = validate_record(invalid_record)

print("Invalid Record Errors:", errors)


# -----------------------------------------
# Test 3: Missing supplier
# -----------------------------------------

missing_supplier_record = {
    "Plant": "Plant_C",
    "Component": "Suspension",
    "Defect": "Dimension_Error",
    "Supplier": "",
    "Quantity": 20
}

errors = validate_record(missing_supplier_record)

print("Missing Supplier Errors:", errors)