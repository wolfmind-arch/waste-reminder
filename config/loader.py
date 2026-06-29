def read_file(file_path):
    """
    Read a text file and return its contents.
    """
    with open(file_path) as file:
        text = file.read()
    return text


def load_config():
    # file_path = "../config.json"
    text = read_file("../config.json")
    print(text)
    print("hej")
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

load_config()



