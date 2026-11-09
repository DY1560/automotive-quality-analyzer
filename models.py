from dataclasses import dataclass


@dataclass
class AutomotiveQualityRecord:

    plant: str

    component: str

    supplier: str

    defect: str

    quantity: int

    def validate(self):

        errors = []

        # -----------------------------------------
        # Mandatory field validation
        # -----------------------------------------

        if not self.plant.strip():

            errors.append("Plant is mandatory")

        if not self.component.strip():

            errors.append("Component is mandatory")

        if not self.supplier.strip():

            errors.append("Supplier is mandatory")

        if not self.defect.strip():

            errors.append("Defect is mandatory")

        # -----------------------------------------
        # Quantity validation
        # -----------------------------------------

        if not isinstance(self.quantity, int):

            errors.append("Quantity must be an integer")

        elif self.quantity < 0:

            errors.append("Quantity cannot be negative")

        return errors

    def calculate_defect_cost(self, cost_per_defect):

        return self.quantity * cost_per_defect

    def display_record(self):

        print(self)