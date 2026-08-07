from pathlib import Path
from utils import scan_directory, move_file,classify_file

def organize_directory(source:Path):
    """
    Organizes the files in the given source directory into subdirectories based on their file extensions.

    Args:
        source (Path): path obj for the directory to organize

    Returns:
        None
    """

    files = scan_directory(source)

    if not files:
        print(f"No files exist in the directory '{source.name}' to organize")

    for file in files:
        category = classify_file(file)
        
        category_folder = source / category

        # move file by design already implicitly creates the category folder if it does not exist

        try:
            move_file(file,category_folder)
        except (PermissionError, FileExistsError, FileNotFoundError) as e:
            print(f'Error occured in file "{file.name}" : {e}')

if __name__ == "__main__":
    organize_directory(Path.home() / "projects" / "file-organizer" / "scratch_test")



