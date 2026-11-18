from typing import TypedDict


class QualityRecord(TypedDict):

    Plant: str

    Component: str

    Supplier: str

    Defect: str

    Quantity: int