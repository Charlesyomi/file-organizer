from pathlib import Path

def scan_directory(path:str) -> list :
    path_obj = Path(path)  #generate path object to work with
    return [file for file in path_obj.iterdir() if file.is_file()]
  