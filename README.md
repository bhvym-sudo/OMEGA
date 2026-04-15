# OMEGA

![OMEGA](OMEGA.png)

A powerful, modular Python CLI-based file conversion tool with real-time progress tracking and a beautiful terminal interface.

## Features

**Supported Conversions**
- CSV ↔ XLSX (bidirectional)
- JSON → CSV

**Real-Time Progress Tracking**
- Live progress bars with row/second throughput
- Detailed logging for each conversion step
- Visual feedback at every stage

**Beautiful Terminal Interface**
- Stylish ASCII art banner
- Colored output (cyan for info, green for success, red for errors, yellow for prompts)
- Professional logging messages with timestamps

**Easy to Extend**
- Clean modular architecture
- Simple conversion routing system
- Add new formats by creating a single script

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd e:\projects\omega
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run in Development Mode
```bash
python app.py
```

### Build Standalone Executable
```bash
pyinstaller build.spec
```

The executable will be created in the `dist/` folder as `FileConverterTool.exe`

## How to Use

1. **Launch the application**
   ```
   python app.py
   ```

2. **Select conversion type**
   - View the list of supported conversions
   - Enter the corresponding number

3. **Provide input file path**
   - Enter the full path to your source file
   - File validation happens automatically

4. **Specify output filename**
   - Enter the desired output filename with extension
   - Output will be saved in the same directory as input

5. **Watch progress**
   - Real-time progress bar shows conversion status
   - Detailed logs for each step

## Project Structure

```
e:\projects\omega\
├── app.py                    # Main entry point
├── requirements.txt          # Project dependencies
├── build.spec               # PyInstaller configuration
├── OMEGA.png                # Application icon
└── scripts/
    ├── __init__.py
    ├── utils.py             # Shared utilities & Logger
    ├── csv_to_xlsx.py       # CSV to Excel converter
    ├── xlsx_to_csv.py       # Excel to CSV converter
    └── json_to_csv.py       # JSON to CSV converter
```

## Dependencies

- **pandas** (2.0.3) - Data manipulation and file I/O
- **openpyxl** (3.1.2) - Excel file handling
- **colorama** (0.4.6) - Colored terminal output
- **tqdm** (4.66.1) - Progress bars
- **pyinstaller** (6.1.0) - Build standalone executables


