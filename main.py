from pathlib import Path
import argparse
from utils import scan_directory, move_file,classify_file

def organize_directory(source:Path, dry_run : bool = False):
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

    if dry_run:
        print()

    for file in files:
        category = classify_file(file)

        if dry_run:
            print(f"[DRY RUN] {file.name} -> {category}/")

        else:       
            category_folder = source / category

            # move file by design already implicitly creates the category folder if it does not exist

            try:
                move_file(file,category_folder)
            except (PermissionError, FileExistsError, FileNotFoundError) as e:
                print(f'Error occured in file "{file.name}" : {e}')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files by type.")

    parser.add_argument("--source", required=True, help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")

    args = parser.parse_args()
    
    organize_directory(source=Path(args.source), dry_run=args.dry_run)



