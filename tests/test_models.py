import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from models import AutomotiveQualityRecord


def test_calculate_defect_cost():

    record = AutomotiveQualityRecord(
        plant="Plant_A",
        component="Brake_Disc",
        supplier="Supplier_01",
        defect="Crack",
        quantity=15
    )

    actual_cost = record.calculate_defect_cost(250)

    expected_cost = 3750

    assert actual_cost == expected_cost