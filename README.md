# GitHubCodeFlow

GitHubCodeFlow is a project aimed at facilitating efficient interaction with GitHub repositories, focusing on extracting metadata and managing code-related tasks. It leverages FastAPI for API handling, Firebase for authentication, and various tools for parsing codebases and managing metadata.

## Features

- **FastAPI Integration**: Utilizes FastAPI, a modern Python web framework, for handling HTTP requests and responses efficiently.
- **Firebase Authentication**: Implements Firebase Bearer Token authentication to ensure secure access to the APIs, allowing only authenticated users.
- **GitHub Repository Interaction**: Provides endpoints to perform operations on GitHub repositories, including metadata extraction and code management.
- **Database Schema**: Designs a database schema to store metadata about functions within a codebase, ensuring efficient data management.
- **Tree-sitter Parsing**: Utilizes the Tree-sitter library to parse codebases and extract metadata about functions, enhancing code analysis capabilities.
- **Function Code Retrieval API**: Designs an API endpoint to retrieve function code based on identifiers stored in the database, facilitating code access.

## Getting Started

To get started with GitHubCodeFlow, follow these steps:

1. **Clone the Repository**: Clone the GitHubCodeFlow repository to your local machine using the following command:

   ```
   git clone https://github.com/codificador10/GithubCodeFlow.git
   ```

2. **Install Dependencies**: Navigate to the cloned directory and install the project dependencies using pip:

   ```
   cd GithubCodeFlow
   pip install -r requirements.txt
   ```

3. **Configure Firebase Credentials**: Obtain Firebase credentials and configure them in the project for authentication purposes.

4. **Run the Application**: Start the FastAPI application using uvicorn:

   ```
   uvicorn main:app --reload
   ```

5. **Access the APIs**: Once the application is running, access the APIs using a suitable API client, providing necessary authentication tokens for authorized access.

## API Documentation

The API endpoints provided by GitHubCodeFlow are documented below:

- **Endpoint 1**: `/functions` - Retrieves all functions' metadata from the database.
- **Endpoint 2**: `/functions/{id}` - Retrieves metadata for a specific function based on its identifier.
- **Endpoint 3**: `/functions/findByName` - Retrieves functions' metadata by their function name.
- **Endpoint 4**: `/functions/findByFunctionAndFileName` - Retrieves functions' metadata by their function name and file name.
- **Endpoint 5**: `/functions/{id}/fileName` - Retrieves the file name for a specific function based on its identifier.
- **Endpoint 6**: `/functions/{id}/functionName` - Retrieves the function name for a specific function based on its identifier.
- **Endpoint 7**: `/functions/{id}/functionBody` - Retrieves the function body for a specific function based on its identifier.
- **Endpoint 8**: `/functions/{id}/fileClass` - Retrieves the class to which a specific function belongs based on its identifier.
- **Endpoint 9**: `/functions` (POST) - Adds a new function's metadata to the database.
- **Endpoint 10**: `/functions/{id}` (PUT) - Updates the metadata of a specific function in the database.
- **Endpoint 11**: `/functions/{id}/functionBody` (PATCH) - Updates the function body of a specific function in the database.
- **Endpoint 12**: `/parseRepo` (POST) - Parses the repository provided in the request body and adds function metadata to the database.


For detailed documentation and examples, refer to the API documentation or interact with the endpoints using an API client.

## Picture Walkthrough

- **HomePage**: Initial state, no GitHub Repo parsed so far
  ![HomePage](https://github.com/codificador10/GithubCodeFlow/assets/82313146/ab593bd4-4eb3-4a10-aed9-c58b1e6cb77e)

- **Parsing a file with repo link as a parameter**: All Functions Added to Database
  ![Parsing a file with repo link as a parameter](https://github.com/codificador10/GithubCodeFlow/assets/82313146/fa5b60d1-ef17-461a-8ae7-f6efd4f9c590)

- **Find by Function Name**: Find by Function Name
  ![Find by Function Name](https://github.com/codificador10/GithubCodeFlow/assets/82313146/005840b8-2aef-43dc-bf57-1aece8ae37f0)

- **Find by Function ID**: Find by Function ID
  ![Find by Function ID](https://github.com/codificador10/GithubCodeFlow/assets/82313146/36010101-d0b5-49a1-b6ae-44b1224081ab)

- **Update the Function Body**: Update the Function Body
  ![Update the Function Body](https://github.com/codificador10/GithubCodeFlow/assets/82313146/8013f26f-b82e-4100-a80f-dd4bfcfa30b1)

- **Updated Function Body**: Updated Function Body
  ![Updated Function Body](https://github.com/codificador10/GithubCodeFlow/assets/82313146/8e9452a9-01d5-4792-acda-bcd701d71719)

## Contribution Guidelines

Contributions to GitHubCodeFlow are welcome!

**Note:** Currently, the project only supports parsing Python files.


## License

GitHubCodeFlow is licensed under the [MIT License](https://github.com/codificador10/GithubCodeFlow/blob/main/LICENSE).
