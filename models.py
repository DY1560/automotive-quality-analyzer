class AutomotiveQualityRecord:

    # Constructor
    def __init__(
        self,
        plant,
        component,
        supplier,
        defect,
        quantity
    ):

        self.plant = plant

        self.component = component

        self.supplier = supplier

        self.defect = defect

        self.quantity = quantity

    # Method
    def display_record(self):

        print("Plant:", self.plant)

        print("Component:", self.component)

        print("Supplier:", self.supplier)

        print("Defect:", self.defect)

        print("Quantity:", self.quantity)