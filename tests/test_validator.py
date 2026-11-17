import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from validator import validate_record


def test_valid_quality_record():

    record = {
        "Plant": "Plant_A",
        "Component": "Brake_Disc",
        "Defect": "Crack",
        "Supplier": "Supplier_01",
        "Quantity": 15
    }

    errors = validate_record(record)

    assert errors == []


def test_negative_quantity():

    record = {
        "Plant": "Plant_A",
        "Component": "Brake_Disc",
        "Defect": "Crack",
        "Supplier": "Supplier_01",
        "Quantity": -5
    }

    errors = validate_record(record)

    assert "Quantity cannot be negative" in errors


def test_missing_supplier():

    record = {
        "Plant": "Plant_A",
        "Component": "Brake_Disc",
        "Defect": "Crack",
        "Quantity": 15
    }

    errors = validate_record(record)

    assert "Missing field: Supplier" in errors


def test_invalid_quantity():

    record = {
        "Plant": "Plant_A",
        "Component": "Brake_Disc",
        "Defect": "Crack",
        "Supplier": "Supplier_01",
        "Quantity": "ABC"
    }

    errors = validate_record(record)

    assert "Quantity must be a valid integer" in errors