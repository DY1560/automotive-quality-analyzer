
from collections import defaultdict

from automotive_quality.quality_types import QualityRecord


# Business thresholds
DEFAULT_DEFECT_THRESHOLD = 20
DEFAULT_SUPPLIER_THRESHOLD = 30


def find_high_defect_records(
    records: list[QualityRecord],
    threshold: int = DEFAULT_DEFECT_THRESHOLD
) -> list[QualityRecord]:
    """
    Return quality records exceeding the defect threshold.

    Args:
        records: Automotive quality records.
        threshold: Maximum permitted defect quantity.

    Returns:
        List of records with quantity greater than threshold.
    """

    high_defect_records = [
        record
        for record in records
        if record["Quantity"] > threshold
    ]

    return high_defect_records


def sort_records_by_quantity(
    records: list[QualityRecord]
) -> list[QualityRecord]:
    """
    Sort quality records by defect quantity in descending order.
    """

    return sorted(
        records,
        key=lambda record: record["Quantity"],
        reverse=True
    )


def calculate_supplier_defects(
    records: list[QualityRecord]
) -> dict[str, int]:
    """
    Calculate total defect quantity for each supplier.
    """

    supplier_defects: dict[str, int] = defaultdict(int)

    for record in records:

        supplier = record["Supplier"]

        quantity = record["Quantity"]

        supplier_defects[supplier] += quantity

    return dict(supplier_defects)


def find_critical_suppliers(
    records: list[QualityRecord],
    threshold: int = DEFAULT_SUPPLIER_THRESHOLD
) -> dict[str, int]:
    """
    Return suppliers exceeding the defect quantity threshold.
    """

    supplier_defects = calculate_supplier_defects(records)

    critical_suppliers = {
        supplier: quantity
        for supplier, quantity in supplier_defects.items()
        if quantity > threshold
    }

    return critical_suppliers
