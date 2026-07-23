# File Organizer

A command-line tool to scan, categorize, and organize files within a directory.

## Status

🚧 Early development — Month 1 of a structured backend engineering syllabus.

## Current Features

- `scan_directory(path: str) -> list` — scans a given directory and returns all files (excluding subdirectories) using `pathlib`.

## Planned Features

- Categorize files by extension/type
- Move files into organized subfolders
- Support dry-run mode (preview changes before applying them)
- CLI interface with argument parsing

## Requirements

- Python 3.9+

## Usage

```python
from main import scan_directory

files = scan_directory("/path/to/folder")
print(files)
```

## Project Log

Daily development notes and design decisions are documented as I build this out.

---
Part of a self-directed transition into backend software engineering.