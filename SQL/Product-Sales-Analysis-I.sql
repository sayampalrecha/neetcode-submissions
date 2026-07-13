select 
    p.product_name,
    s.year,
    s.price
from 
    Product p
    
RIGHT JOIN
    Sales s
ON 
    s.product_id = p.product_id;

-- pandas code 
'''
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.merge(product, on='product_id')[['product_name','year','price']]
'''
