# code-genie-server
server for code genie

# folder structure for the project
    code-genie-server/
    │
    ├── server.py            # Entry point for the FastAPI server
    ├── routes/              # API routes
    │   ├── endpoints.py     # Define API endpoints
    ├── db/                  # Database-related files
    │   ├── models.py        # Database models
    │   ├── crud.py          # CRUD operations
    │   └── connection.py    # Database connection management
    ├── services/            # Business logic and services
    │   └── openai_service.py# Interactions with OpenAI API
    ├── utils/               # Utility functions
    │   └── helpers.py
    ├── tests/               # Unit and integration tests
    │   ├── test_endpoints.py
    │   └── test_services.py
    ├── .env                 # Environment variables
    ├── requirements.txt     # Python dependencies
    └── README.md            # Project documentation
