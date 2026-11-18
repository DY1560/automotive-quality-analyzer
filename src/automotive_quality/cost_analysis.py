
"""
Automotive quality defect cost calculations.
"""


def calculate_total_defect_cost(
    quantity: int,
    cost_per_defect: float
) -> float:
    """
    Calculate estimated defect cost.

    Args:
        quantity: Number of defective components.
        cost_per_defect: Estimated cost per defective component.

    Returns:
        Estimated total defect cost.
    """

    return quantity * cost_per_defect


def calculate_supplier_quality_cost(
    defect_quantity: int,
    rejection_cost: float,
    inspection_cost: float
) -> float:
    """
    Calculate total supplier quality cost.

    Includes rejection and inspection costs.
    """

    total_cost = (
        defect_quantity * rejection_cost
        + inspection_cost
    )

    return total_cost
