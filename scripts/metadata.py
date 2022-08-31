import json
from pathlib import Path
from typing import Any, Dict, List, Optional

AuthorInfo = Dict[str, str]

DEFAULT_AUTHOR = {
    "name": "Unknown",
    "orcid": "https://orcid.org/0000-0000-0000-0000",
}
CREATORS_KEY = "creators"


def extract_default_authors(metadata: Path) -> List[AuthorInfo]:
    """Attempts to extract author information from the metadata.json file within
    the repository. If none are found, returns a dummy value.

    Parameters:
        metadata: The path to the metadata file, commonly metadata.json
    """
    with open(metadata) as file:
        data = json.load(file)

    return data.get(CREATORS_KEY, [DEFAULT_AUTHOR])


def extract_notebook_metadata(notebook: Path, keys: Dict[str, Any]) -> Dict[str, Any]:
    """Attempts to extract metadata from the notebook.

    Parameters:
        notebook: The path to the jupyter notebook
        keys: A dictionary of keys to look for in the notebook, and their
            corresponding defaults if the key is not found.

    Returns:
        A dictionary containing the retrieved metadata for each key.
    """
    with open(notebook) as file:
        data = json.load(file)

    metadata = data["metadata"]
    result = {}

    for key, default in keys.items():
        result[key] = metadata.get(key, default)

    return result

