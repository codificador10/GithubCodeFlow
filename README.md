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

For detailed documentation and examples, refer to the API documentation or interact with the endpoints using an API client.

## Contribution Guidelines

Contributions to GitHubCodeFlow are welcome! If you'd like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or fix.
- Make your changes, ensuring adherence to coding standards and documentation guidelines.
- Test your changes thoroughly.
- Submit a pull request, providing a clear description of the changes made and any relevant information.

## License

GitHubCodeFlow is licensed under the [MIT License](https://github.com/codificador10/GithubCodeFlow/blob/main/LICENSE).
