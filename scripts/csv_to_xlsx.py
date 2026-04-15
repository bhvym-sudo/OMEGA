import pandas as pd
from tqdm import tqdm
from openpyxl import Workbook
from .utils import Logger

def convert(input_path, output_path):
    try:
        Logger.info(f"Reading CSV file: {input_path}")
        
        chunks = []
        total_rows = 0
        
        with tqdm(desc="Reading CSV", unit=" rows", colour="cyan", dynamic_ncols=True) as pbar:
            for chunk in pd.read_csv(input_path, chunksize=10000):
                chunks.append(chunk)
                pbar.update(len(chunk))
                total_rows += len(chunk)
        
        Logger.info(f"Loaded {total_rows} rows and {chunks[0].shape[1]} columns")
        df = pd.concat(chunks, ignore_index=True)
        
        Logger.info(f"Converting to Excel format...")
        
        wb = Workbook()
        ws = wb.active
        
        with tqdm(total=len(df) + 1, desc="Writing Excel", unit=" rows", colour="magenta", dynamic_ncols=True) as pbar:
            ws.append(list(df.columns))
            pbar.update(1)
            
            for row in df.itertuples(index=False, name=None):
                ws.append(row)
                pbar.update(1)
        
        Logger.info(f"Saving Excel file to: {output_path}")
        wb.save(output_path)
        
        Logger.success(f"Conversion completed! CSV → XLSX")
        Logger.info(f"Output file: {output_path}")
        return True
    except Exception as e:
        Logger.error(f"Conversion failed: {str(e)}")
        return False
