import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from analysis import (
    find_high_defect_records,
    sort_records_by_quantity,
    calculate_supplier_defects,
    find_critical_suppliers
)


def sample_records():

    return [
        {
            "Plant": "Plant_A",
            "Component": "Brake_Disc",
            "Supplier": "Supplier_01",
            "Defect": "Crack",
            "Quantity": 15
        },
        {
            "Plant": "Plant_A",
            "Component": "Brake_Disc",
            "Supplier": "Supplier_01",
            "Defect": "Surface_Defect",
            "Quantity": 10
        },
        {
            "Plant": "Plant_B",
            "Component": "Steering_Rack",
            "Supplier": "Supplier_02",
            "Defect": "Leakage",
            "Quantity": 25
        },
        {
            "Plant": "Plant_B",
            "Component": "Steering_Rack",
            "Supplier": "Supplier_02",
            "Defect": "Leakage",
            "Quantity": 10
        }
    ]


def test_high_defect_filter():

    records = sample_records()

    result = find_high_defect_records(
        records,
        threshold=20
    )

    assert len(result) == 1

    assert result[0]["Quantity"] == 25


def test_sort_records():

    records = sample_records()

    result = sort_records_by_quantity(records)

    assert result[0]["Quantity"] == 25

    assert result[-1]["Quantity"] == 10


def test_supplier_aggregation():

    records = sample_records()

    result = calculate_supplier_defects(records)

    assert result["Supplier_01"] == 25

    assert result["Supplier_02"] == 35


def test_critical_suppliers():

    records = sample_records()

    result = find_critical_suppliers(
        records,
        threshold=30
    )

    assert result == {
        "Supplier_02": 35
    }