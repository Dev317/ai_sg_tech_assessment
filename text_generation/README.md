### Overview


https://github.com/Dev317/ai_sg_tech_assessment/assets/70529335/a8b6a5c6-e20f-4d06-acee-f99576b0b7c8


This is overall a simple program that does sentence auto completion by invoking Hugging Face Inference API using gpt2.
It will take in a single user input and returns response that are pre-configured in the api call params. The program heavily depends on the `config.yaml` that acts as a contract on how to invoke the api endpoint (e.g what endpoint to call, which model to use, what params to put in). Additionally, the program also has a retry mechanism to ensure that users will always get a response or be notified of any errors!

### How to run the program
- Pre-requisite: python3.8 version and above
- Setup:
    1. Set up the python virtual environment
    ````
        cd text_generation
        python3 venv venv
        source venv/bin/activate
        pip3 install -r requirements.txt
    ````
    2. Get Hugging Face API Token. Reference: https://huggingface.co/docs/hub/en/security-tokens
    3. Create a `.env` file that stores Hugging Face API Token
    ```
        HUGGING_FACE_API_KEY=hf_******
    ```
    4. Run the program with the following command
    ```
        python3 main.py
    ```
    5. If you want to add more parameters, do make the necessary changes under `parameters` in the `config.yaml`

### Testing
1. A simple CI workflow `text_generation_ci.yaml` is being set up
2. Any pull request needs to pass the CI before being merged to `main` branch
3. At the moment, the CI only does basic unit testing
