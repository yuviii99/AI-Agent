from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
#import chardet


load_dotenv()

ecological_footprint_data_path = os.path.join("data", "ecological_footprint_2023.csv")
ecological_footprint_df = pd.read_csv(ecological_footprint_data_path, encoding='ISO-8859-1')

query_engine = PandasQueryEngine(df=ecological_footprint_df, verbose=True)

print(ecological_footprint_df)