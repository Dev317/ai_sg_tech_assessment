import os
from unittest import TestCase, mock
from utils import get_hugging_face_auth_token, get_config, format_llm_response

class TestUtils(TestCase):

    @mock.patch('os.getenv', return_value=None)
    def test_fail_to_get_hugging_face_auth_token(self, mock_getenv):
        with self.assertRaises(ValueError):
            get_hugging_face_auth_token()

    def test_succeed_to_get_hugging_face_auth_token(self):
        os.environ["HUGGING_FACE_API_KEY"] = "test"
        self.assertEqual(get_hugging_face_auth_token(), "test")

    def test_fail_to_get_config(self):
        with self.assertRaises(FileNotFoundError):
            get_config("test_config.yaml")

    def test_succeed_to_get_config(self):
        config = get_config("config.yaml")
        self.assertEqual(config["model_id"], "gpt2")
        self.assertEqual(config["model_endpoint"], "https://api-inference.huggingface.co/models")
        self.assertEqual(config["parameters"], {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8})
        self.assertEqual(config["max_retry"], 3)

    def test_format_llm_response(self):
        generated_texts = [
            { "generated_text": "Hello World.\n\n" },
            { "generated_text": "This is a test." }
        ]
        self.assertEqual(format_llm_response(generated_texts), "Hello World. This is a test.")
