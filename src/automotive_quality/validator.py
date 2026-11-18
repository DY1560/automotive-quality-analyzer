# validator.py

REQUIRED_FIELDS = [
    "Plant",
    "Component",
    "Defect",
    "Supplier",
    "Quantity"
]


def validate_record(record):

    errors = []

    # -----------------------------------------
    # 1. Check mandatory fields
    # -----------------------------------------

    for field in REQUIRED_FIELDS:

        if field not in record:

            errors.append(f"Missing field: {field}")

        elif record[field] is None or str(record[field]).strip() == "":

            errors.append(f"Empty value: {field}")

    # -----------------------------------------
    # 2. Validate quantity
    # -----------------------------------------

    if "Quantity" in record:

        try:

            quantity = int(record["Quantity"])

            if quantity < 0:

                errors.append("Quantity cannot be negative")
            
            if quantity >1000:
                
                errors.append("Unusually High Defect Quantity Detected")

        except (ValueError, TypeError):

            errors.append("Quantity must be a valid integer")

    # -----------------------------------------
    # 3. Return validation result
    # -----------------------------------------

    return errors