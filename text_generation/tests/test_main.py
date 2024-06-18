import os
from unittest import TestCase, mock
from main import build_url, build_payload, build_headers, call_api, main

class TestMain(TestCase):

    def test_build_url(self):
        mock_config = {
            "model_id": "gpt3",
            "model_endpoint": "https://api-inference.huggingface.co/model",
        }
        self.assertEqual(build_url(mock_config), "https://api-inference.huggingface.co/model/gpt3")

    def test_build_payload(self):
        mock_config = {
            "parameters": {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8}
        }
        mock_user_input = "Hello World."
        self.assertEqual(build_payload(mock_config, mock_user_input), {"inputs": "Hello World.", "parameters": {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8}})

    def test_build_headers(self):
        mock_auth_token = "test-token"
        self.assertEqual(build_headers(mock_auth_token), {"Authorization": f"Bearer test-token", "Content-Type": "application/json"})

    def test_fail_to_call_api_non_200_status(self):
        mock_session = mock.MagicMock()
        mock_session.post.return_value.status_code = 500
        mock_config = {
            "model_endpoint": "https://api-inference.huggingface.co/model",
            "parameters": {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8}
        }
        mock_auth_token = "test-token"
        mock_user_input = "Hello World."
        with self.assertRaises(Exception):
            call_api(mock_session, mock_config, mock_auth_token, mock_user_input)

    def test_fail_to_call_api_empty_response(self):
        mock_session = mock.MagicMock()
        mock_session.post.return_value.status_code = 200
        mock_session.post.return_value.json.return_value = []
        mock_config = {
            "model_endpoint": "https://api-inference.huggingface.co/model",
            "parameters": {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8}
        }
        mock_auth_token = "test-token"
        mock_user_input = "Hello World."
        with self.assertRaises(Exception):
            call_api(mock_session, mock_config, mock_auth_token, mock_user_input)

    def test_call_api(self):
        mock_session = mock.MagicMock()
        mock_session.post.return_value.status_code = 200
        mock_session.post.return_value.json.return_value = [{"generated_text": "Hello World."}]
        mock_config = {
            "model_endpoint": "https://api-inference.huggingface.co/model",
            "model_id": "gpt3",
            "parameters": {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8}
        }
        mock_auth_token = "test-token"
        mock_user_input = "Hello World."
        self.assertEqual(call_api(mock_session, mock_config, mock_auth_token, mock_user_input), "Hello World.")
