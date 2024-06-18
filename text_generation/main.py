from utils import get_session, get_config, get_hugging_face_auth_token, format_llm_response
from requests import Session
from typing import Dict

def build_url(config: Dict) -> str:
    """
    This function builds the API endpoint.
    Args:
        config: Configuration that contains details how to formulate api endpoint.
    Returns:
        url: API endpoint.

    Reference: https://huggingface.co/docs/api-inference/quicktour#running-inference-with-api-requests
    """
    URL_FORMAT = "{model_endpoint}/{model_id}"

    return URL_FORMAT.format(
        model_endpoint=config["model_endpoint"],
        model_id=config["model_id"]
    )

def build_payload(
        config: Dict,
        user_input: str) -> Dict:
    """
    This function builds the payload for the API.
    Args:
        config: Configuration that contains details about api endpoint.
        user_input: User input to the API.
    Returns:
        payload: Payload for the API.

    Reference: https://huggingface.co/docs/api-inference/detailed_parameters#text-generation-task
    """
    return {
        "inputs": user_input,
        "parameters": config["parameters"]
    }

def build_headers(auth_token: str) -> Dict:
    """
    This function builds the headers for the API.
    Args:
        auth_token: Hugging Face API token.
    Returns:
        headers: Headers for the API.
    """
    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

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

    url_endpoint = build_url(config=config)
    payload = build_payload(config=config, user_input=user_input)
    headers = build_headers(auth_token=auth_token)


    response = session.post(url=url_endpoint, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error: {response.text}")

    json_response = response.json()
    if len(json_response) == 0:
        raise Exception("No text is generated")

    llm_response = format_llm_response(generated_texts=json_response)
    return llm_response


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
    print(f"Generated Text: {llm_response}")


if __name__ == "__main__":
    main()
