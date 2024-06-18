from utils import get_session, get_config, get_hugging_face_auth_token
from requests import Session
from typing import Dict

def call_api(session: Session,
             config: Dict,
             auth_token: str,
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
    hugging_face_auth_token = get_hugging_face_auth_token()

    user_input = input("Input: ")
    llm_response = call_api(session=session,
                            config=config,
                            auth_token=hugging_face_auth_token,
                            user_input=user_input)
    print(llm_response)


if __name__ == "__main__":
    main()
