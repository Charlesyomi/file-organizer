from pathlib import Path

def scan_directory(path:str) -> list :
    """scans a directory for files

    Args:
        path: string, the path to the directory

    Returns:
        a list containing just files in a directory
    """
    path_obj = Path(path)  #generate path object to work with
    return [file for file in path_obj.iterdir() if file.is_file()]

EXTENSION_CATEGORIES = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".md": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".tiff": "Images",
    ".webp": "Images",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".h": "Code",
    ".html": "Code",
    ".css": "Code",
    ".sh": "Code",
    ".ipynb": "Code",

    # Data
    ".csv": "Data",
    ".json": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".xlsx": "Data",
    ".xls": "Data",
    ".sql": "Data",
    ".parquet": "Data",

    # Archives
    ".zip": "Archives",
    ".gz": "Archives",
    ".tar": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
}

def classify_file(path:Path) -> str:
    """classifies file by extension

    Args:
        path: path object for the file to classify

    Returns:
        class for file based on its extension or "Other"
    """

    ext = path.suffix.casefold()
    category = EXTENSION_CATEGORIES.get(ext, "Other")

    print(category)
    return category

classify_file(Path("Readme"))