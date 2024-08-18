# code-genie-server

server for code genie

# folder structure for the project

    code-genie-server/
    │
    ├── server.py            # Entry point for the FastAPI server
    ├── routes/              # API routes # Define API endpoints
    ├── db/                  # Database-related files, Database models, CRUD operations, Database connection management
    ├── services/            # Business logic and services, Interactions with OpenAI API
    ├── utils/               # Utility functions
    ├── tests/               # Unit and integration tests, test_services.py
    ├── .env                 # Environment variables
    ├── requirements.txt     # Python dependencies
    └── README.md            # Project documentation

---

# Environment Variables (Explanation)

The following environment variables are stored in `.env`. Loading and usage of these variables is explained in [Usage](#environment-variables-usage)

- `MONGODB_USERNAME`: The username for MongoDB. Example: **root**
- `MONGODB_PASSWORD`: The password for MongoDB. Example: **1234**
- `MONGODB_HOST`: The host for MongoDB. Example: **localhost**
- `OPENAI_API_KEY`: The API Key used to make requests to the OpenAI API. Example: **sk-abcdefghijklmnopqrstuvwxyz1234567890abcd**
- `SERVER_URL`: The online server url. Example: **https://online-server-url.onrender.com/**

# Environment Variables (Usage)

To load environment variables from a `.env` file in Python, you can use the `python-dotenv` package. Here’s how you can do it:

1. Save an `.env` file in your project. **WARNING**: make sure it is found in `.gitignore`. Save the above [Variables](#environment-variables-explanation) in the `.env` file using the exact provided names.

2. **Install the `python-dotenv` package** (if you haven’t already):

   ```sh
   pip install python-dotenv

   ```

3. A brief example on how to load a specific environment variable:

   ```python
   from dotenv import load_dotenv
   from globals import globals


   # Load the appropriate .env file
   if globals.env_status == "dev":
      load_dotenv('.env.dev')
   else:
      load_dotenv('.env.prod')

   mongodb_host = os.getenv('MONGODB_HOST')
   ```

## Command-Line Arguments

- `--env`: Specifies the environment to run the server in. Valid options are `dev` and `prod`. The default is `dev`.

## Running the Server

### Running in Development Environment

To run the server in the `dev` environment (default), use the following command:

```bash
python server.py
```

Or explicitly specify the environment:

```bash
python server.py --env dev
```

This will start the server on `127.0.0.1` (localhost) at port `8002`.

### Running in Production Environment

To run the server in the `prod` environment, use the following command:

```bash
python server.py --env prod
```

This will start the server on `127.0.0.1` (localhost) at port `8001`.

# Running the tests

In order to run the tests you have to run the following commands:

```shell
cd path/to/your/project # Replace with the path to your project (root)
pytest
```

# Mongodb setup collections
# Users Database

An example of how a user and its details is stored in the database:

```json
{
  "_id": {
    "$oid": "66b8c62485b638ba5da0f934"
  },
  "user_id": "636459",
  "questions": [
    {
      "question_text": "How to list all of your services in Docker swarm?",
      "score": 9,
      "answer": "docker service ls",
      "topic": "Docker",
      "is_correct": true
    },
    {
      "question_text": "How to list all of your services in Docker swarm?",
      "score": 0,
      "answer": "my answer",
      "topic": "Docker",
      "is_correct": false
    },
    {
      "question_text": "Docker can build images automatically by reading the instructions from",
      "score": 9,
      "answer": "Dockerfile",
      "topic": "Docker",
      "is_correct": true
    },
    {
      "question_text":  "What is the key difference between React.js functional components and class components regarding state management?",
      "score": 2,
      "answer": "my answer",
      "topic": "Docker",
      "is_correct": false
    }
  ],
  "topics": {
    "Docker": {
      "hard": {
        "questions_answered": 1,
        "questions_answered_correctly": 1
      },
      "easy": {
        "questions_answered": 2,
        "questions_answered_correctly": 1
      }
    },
    "Linux": {
      "hard": {
        "questions_answered": 1,
        "questions_answered_correctly": 0
      }
    }
  }
}
```  

# Questions Database

An example of how a question and its details is stored in the database:

```json
{
  "_id": {
    "$oid": "66b89fea6b1e15e0af25ffce"
  },
  "question": "How are you?",
  "answers": {
    "636459": "Bad",
    "944113": "Good"
  },
  "explanations": {
    "636459": "I lost the last FIFA match",
    "944113": "I won the last FIFA match"
  },
  "difficulty": "easy",
  "users_details": {
    "636459": "mohamad",
    "944113": "shaheen"
  }
}
```

As shown in the above example, one question can be answered by many users and each user is represented by his ID

