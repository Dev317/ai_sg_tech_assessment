from utils import get_session, get_config
from requests import Session
from typing import Dict

def call_api(session: Session,
             config: Dict,
             user_input: str) -> str:
    """
    This function invoke the API and returns the response
    Args:
        session: Session object with retry mechanism.
        config: Configuration that contains details about api endpoint.
        user_input: User input to the API.
    Returns:
        response: Response from the API.
    """
    pass

def main() -> None:
    config = get_config(config_path="config.yaml")
    session = get_session(
        max_retry=config["max_retry"],
        retry_status_codes=config["retry_status_codes"],
        backoff_factor=config["retry_backoff_factor"]
    )
    user_input = input("Input: ")
    llm_response = call_api(session=session,
                            config=config,
                            user_input=user_input)
    print(llm_response)


if __name__ == "__main__":
    main()
