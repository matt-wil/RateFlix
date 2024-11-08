import os


def determine_storage_type(file_path: str) -> str:
    """determine the storage type based on the file extension"""
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == ".json":
        return "json"
    elif extension == ".csv":
        return "csv"
    else:
        raise ValueError("Unsupported file type. At this time we only support .json and .csv files.")


def determine_ui_type():
    pass
