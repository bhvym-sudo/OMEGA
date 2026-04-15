import pandas as pd
from tqdm import tqdm
from .utils import Logger

def convert(input_path, output_path):
    try:
        Logger.info(f"Reading JSON file: {input_path}")
        
        with tqdm(total=100, desc="Reading JSON", unit="%", colour="cyan", dynamic_ncols=True) as pbar:
            pbar.update(40)
            df = pd.read_json(input_path)
            pbar.update(60)
        
        Logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
        
        Logger.info(f"Converting to CSV format...")
        with tqdm(total=100, desc="Converting", unit="%", colour="magenta", dynamic_ncols=True) as pbar:
            pbar.update(50)
            df.to_csv(output_path, index=False)
            pbar.update(50)
        
        Logger.info(f"Writing CSV file to: {output_path}")
        Logger.success(f"Conversion completed! JSON → CSV")
        Logger.info(f"Output file: {output_path}")
        return True
    except Exception as e:
        Logger.error(f"Conversion failed: {str(e)}")
        return False
