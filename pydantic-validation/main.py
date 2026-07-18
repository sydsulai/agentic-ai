from pydantic import BaseModel, ValidationError, Field
from typing import Optional

class Employee(BaseModel):
    name: str = Field(min_length=1, description="Name must be a non-empty string")
    age: int = Field(..., gt=0, description="Age must be a positive integer")
    department: Optional[str] = None
    email_id: str = Field(default_factory=lambda: "user@example.com", description="Email ID with a default value")
    salary: float = Field(gt=0, description="Salary must be a positive float")
    reportee: Optional[list[str]] = Field(default_factory=list, description="List of reportees, default is an empty list")

emp1 = Employee(name="John Doe", age=30, department="Engineering", salary=75000.0)
print(emp1)

emp2 = Employee(name="Jane Smith", age=28, department="Marketing", email_id="jane.smith@example.com", salary=68000.0)
print(emp2)

emp3 = Employee(name="Alice Johnson", age=35, department="HR", salary=80000.0, reportee=["Bob Brown", "Charlie Davis"])
print(emp3)

emp4 = Employee(name="Bob Brown", age=40, department="Finance", salary=-1, reportee=["David Evans"])
print(emp4)