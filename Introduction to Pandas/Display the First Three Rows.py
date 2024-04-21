import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    three_rows = employees.head(3)
    return three_rows
    
