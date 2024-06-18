import os
import requests
from requests.adapters import HTTPAdapter, Retry
import yaml
from dotenv import load_dotenv
from typing import Dict, List

def get_session(
    max_retry: int,
    retry_status_codes: List[int],
    backoff_factor: float = 0.1
) -> requests.Session:
    """
    This function creates a session object with retry mechanism.
    Args:
        max_retry: Maximum number of retries.
        retry_status_codes: List of status codes to retry.
        backoff_factor: A backoff factor to apply between attempts after the second try.
    Returns:
        sess: A session object with retry mechanism.
    """
    sess = requests.Session()
    retries = Retry(total=max_retry,
                    backoff_factor=backoff_factor,
                    status_forcelist=retry_status_codes)
    sess.mount('http://', HTTPAdapter(max_retries=retries))
    return sess

def get_config(config_path: str) -> Dict:
    """
    This function reads the yaml configuration file.
    Args:
        config_path: Path to the configuration file.
    Returns:
        config: Configuration that contains details about api endpoint.
    """

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file {config_path} not found")

    with open(file=config_path, mode="r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise Exception(f"Error reading the config file: {exc}")

    return config

def get_hugging_face_auth_token() -> str:
    """
    This function reads the Hugging Face API token from the environment variable.
    Returns:
        token: Hugging Face API token.
    """
    load_dotenv()
    token = os.getenv("HUGGING_FACE_API_KEY", None)
    if token is None:
        raise ValueError("Hugging Face API token not found in the environment variable.")
    return token
