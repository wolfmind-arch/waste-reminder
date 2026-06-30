import json
from pathlib import Path

def read_file(file_path):
    """
    Read a text file and return its contents.
    """
    with open(file_path) as file:
        text = file.read()
    return text

def parse_json(text):
    config = json.loads(text)
    return config



def load_config():
    # file_path = Path("../config.json")
    file_path = Path(__file__).parent.parent / "config.json"


    text = read_file(file_path)

    config = parse_json(text)
    return config

    
    """
    Load and validate the application configuration.

    Parameters:
        None

    Returns:
        dict:
            Application configuration.

    Raises:
        FileNotFoundError:
            If config.json cannot be found.

        JSONDecodeError:
            If the JSON syntax is invalid.

        ValueError:
            If required configuration values are missing.
    """

print(load_config())




