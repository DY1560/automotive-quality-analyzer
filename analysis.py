from collections import defaultdict


def find_high_defect_records(records, threshold=20):

    high_defects = [
        record
        for record in records
        if record["Quantity"] > threshold
    ]

    return high_defects


def sort_records_by_quantity(records):

    sorted_records = sorted(
        records,
        key=lambda record: record["Quantity"],
        reverse=True
    )

    return sorted_records


def calculate_supplier_defects(records):

    supplier_defects = defaultdict(int)

    for record in records:

        supplier = record["Supplier"]

        quantity = record["Quantity"]

        supplier_defects[supplier] += quantity

    return dict(supplier_defects)


def find_critical_suppliers(records, threshold=30):

    supplier_defects = calculate_supplier_defects(records)

    critical_suppliers = {
        supplier: quantity
        for supplier, quantity in supplier_defects.items()
        if quantity > threshold
    }

    return critical_suppliers