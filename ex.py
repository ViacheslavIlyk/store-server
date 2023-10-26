import pandas as pd
import os

file = os.path.join(os.getcwd(), 'store/products/fixtures/categories.json')
# /content/data/file.txt

df = pd.read_json(file, encoding='unicode_escape')