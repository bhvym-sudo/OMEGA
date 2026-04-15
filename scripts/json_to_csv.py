import pandas as pd
from tqdm import tqdm
import csv
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
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            with tqdm(total=len(df) + 1, desc="Writing CSV", unit=" rows", colour="magenta", dynamic_ncols=True) as pbar:
                writer.writerow(df.columns)
                pbar.update(1)
                
                for idx, row in enumerate(df.values):
                    writer.writerow(row)
                    pbar.update(1)
        
        Logger.info(f"Saving CSV file to: {output_path}")
        Logger.warning("DO NOT CLOSE THIS WINDOW - File is being saved...")
        Logger.success(f"Conversion completed! JSON → CSV")
        Logger.info(f"Output file: {output_path}")
        return True
    except Exception as e:
        Logger.error(f"Conversion failed: {str(e)}")
        return False
