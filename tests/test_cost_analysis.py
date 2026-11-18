
from automotive_quality.cost_analysis import (
    calculate_total_defect_cost,
    calculate_supplier_quality_cost
)


def test_calculate_total_defect_cost():

    actual_cost = calculate_total_defect_cost(
        quantity=15,
        cost_per_defect=250
    )

    assert actual_cost == 3750


def test_calculate_supplier_quality_cost():

    actual_cost = calculate_supplier_quality_cost(
        defect_quantity=10,
        rejection_cost=200,
        inspection_cost=500
    )

    assert actual_cost == 2500


def test_zero_defect_cost():

    actual_cost = calculate_total_defect_cost(
        quantity=0,
        cost_per_defect=250
    )

    assert actual_cost == 0
