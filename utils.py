from pathlib import Path
import shutil

def scan_directory(path:Path) -> list :
    """scans a directory for files

    Args:
        path: Path obj, the path to the directory

    Returns:
        a list containing just files in a directory
    """
    return [file for file in path.iterdir() if file.is_file()]

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

    # print(category)
    return category

# classify_file(Path("pandas.JPG"))

def move_file(src:Path, dest_folder:Path) -> Path :
    """moves a given file to a given destination even if has to create destination folders

    Args:
        src: Path Object of the file to be moved
        dest_folder: Path Object for the move endpoint
    
    Returns:
        Path Object of the new file location

    Raises:
        FileExistsError: if file already exists in new location
        FileNotFoundError: if destination folder DNE--slim chance from a TOCTOU window
        PermissionError: if user does not have move to/ create permission for dest folder
    """

    dest_path = dest_folder / src.name

    if dest_path.exists():
        raise FileExistsError(f"{src.name} already exists at {dest_path}")

    dest_folder.mkdir(exist_ok=True, parents=True)

    shutil.move(src, dest_path)

    return dest_path

