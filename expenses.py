
from typing import Self
from unicodedata import category


class Expense:
    class amount:
     def __init__(Self,__name__,category,amount) -None:# type: ignore
      Self.name= __name__
      Self.category= category
      Self.amount=amount

    def __repr__(self) -> str:
        return f"<Expense: {self.name},{self.category},${self.amount:.2f}>"



    

