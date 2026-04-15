import pandas as pd
from tqdm import tqdm
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
        with tqdm(total=100, desc="Converting", unit="%", colour="magenta", dynamic_ncols=True) as pbar:
            pbar.update(50)
            df.to_excel(output_path, index=False)
            pbar.update(50)
        
        Logger.info(f"Writing Excel file to: {output_path}")
        Logger.success(f"Conversion completed! CSV → XLSX")
        Logger.info(f"Output file: {output_path}")
        return True
    except Exception as e:
        Logger.error(f"Conversion failed: {str(e)}")
        return False
