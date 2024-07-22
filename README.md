# code-genie-server
server for code genie

# Environment Variables (Explanation)

The following environment variables are stored in `.env`. Loading and usage of these variables is explained in [Usage](#environment-variables-usage)

- `MONGODB_USERNAME`: The username for MongoDB. Example: **root**
- `MONGODB_PASSWORD`: The password for MongoDB. Example: **1234**
- `MONGODB_HOST`: The host for MongoDB. Example: **localhost**
- `MONGODB_PORT`: The port for MongoDB: Example: **27017**
- `OPENAI_API_KEY`: The API Key used to make requests to the OpenAI API. Example: **sk-abcdefghijklmnopqrstuvwxyz1234567890abcd**


# Environment Variables (Usage)

To load environment variables from a `.env` file in Python, you can use the `python-dotenv` package. Here’s how you can do it:

1. Save an `.env` file in your project. **WARNING**: make sure it is found in `.gitignore`. Save the above [Variables](#environment-variables-explanation) in the `.env` file using the exact provided names.

2. **Install the `python-dotenv` package** (if you haven’t already):
   ```sh
   pip install python-dotenv
   
3. A brief example on how to load a specific environment variable:
    ```python
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    mongodb_host = os.getenv('MONGODB_HOST')
    ```
# mongodb collections
## users 
user_id \
username \
chat_id \
created_at \
last_active \
status 
## Questions
question_id \
topic \
difficulty \
question_text \ 
correct_answer \
wrong_answers \
explanation \
created_at 
## UserAnswers
user_id \
question_id \
selected_answer \
is_correct \
answered_at 