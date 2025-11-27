from pathlib import Path
import json
import pickle


class File:
    @staticmethod
    def _get_path(path: str) -> Path:
        """Validate path and return a Path object."""
        if not path:
            raise ValueError("Empty file path", path)

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError("File not found:", path)

        return file_path

    @staticmethod
    def load_json(path: str) -> dict:
        file_path = File._get_path(path)

        with file_path.open() as f:
            return json.load(f)

    @staticmethod
    def load_txt(path: str) -> str:
        file_path = File._get_path(path)

        with file_path.open() as f:
            return f.read()

    @staticmethod
    def load_pickle(path: str) -> str:
        file_path = File._get_path(path)

        with file_path.open("rb") as f:
            return pickle.load(f)

    @staticmethod
    def _prepare_path(path: str) -> Path:
        """Create parent folder if needed and return a Path object."""
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        return file_path

    @staticmethod
    def dump_json(path: str, data: dict):
        file_path = File._prepare_path(path)
        with file_path.open("w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def dump_pickle(path: str, data):
        file_path = File._prepare_path(path)
        with file_path.open("wb") as f:
            pickle.dump(data, f)
