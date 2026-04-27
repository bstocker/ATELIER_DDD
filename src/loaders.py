from pathlib import Path


def read_text_file(path: str | Path) -> str:
    """Read a UTF-8 text file and return its content."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path.read_text(encoding="utf-8")
