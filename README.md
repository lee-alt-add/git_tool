Here’s the updated `README.md` file with the inclusion of the `requirements.txt` and instructions for setting it up:

---

# GitHub CLI Tool

This is a command-line tool that allows you to interact with the GitHub API. It provides functionality to retrieve user information, list repositories, search for repositories by keyword, and fetch commit details for a specific repository.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Commands](#commands)
6. [Environment Variables](#environment-variables)
7. [Requirements](#requirements)
8. [Contributing](#contributing)

---

## Features

- Retrieve detailed information about a GitHub user.
- List all public repositories for a given user.
- Search for repositories based on a keyword.
- Fetch commit history for a specific repository and branch.

---

## Prerequisites

Before using this tool, ensure you have the following installed:

- Python 3.6 or higher
- `pip` (Python package manager)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url.git
   cd github-cli-tool
   ```

2. Install the required dependencies using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the following packages:
   - `requests==2.32.3`
   - `python-dotenv==1.0.1`

3. Create a `.env` file in the root directory and add your GitHub API token:

   ```env
   GIT_API_TOKEN=your_github_api_token_here
   ```

   You can generate a personal access token from your GitHub account settings under "Developer Settings" -> "Personal Access Tokens".

---

## Usage

Run the tool from the command line:

```bash
python github_cli.py [command] [arguments]
```

For help:

```bash
python github_cli.py --help
```

---

## Commands

### 1. Get User Information

Retrieve details about a GitHub user.

**Command:**

```bash
python github_cli.py user <username>
```

**Example:**

```bash
python github_cli.py user octocat
```

**Output:**

```
Github user: octocat
Name: The Octocat
Bio: The Octocat is here to help!
Public Repos: 10
```

---

### 2. List Repositories

List all public repositories for a given user.

**Command:**

```bash
python github_cli.py repos <username>
```

**Example:**

```bash
python github_cli.py repos octocat
```

**Output:**

```
Repositories of octocat:
- Hello-World (https://github.com/octocat/Hello-World)
- Spoon-Knife (https://github.com/octocat/Spoon-Knife)
```

---

### 3. Search Repositories by Keyword

Search for repositories owned by a user that match a specific keyword.

**Command:**

```bash
python github_cli.py search <username> <keyword>
```

**Example:**

```bash
python github_cli.py search octocat hello
```

**Output:**

```
Repositories with keyword 'hello':
************
- Hello-World (https://github.com/octocat/Hello-World)
```

---

### 4. Get Commit History

Fetch the commit history for a specific repository and branch.

**Command:**

```bash
python github_cli.py commits <username> <repo> [branch]
```

**Example:**

```bash
python github_cli.py commits octocat Hello-World main
```

**Output:**

```
Hello-World has '5' commits:

1- The Octocat : Initial commit
2- The Octocat : Add README
3- The Octocat : Update README
4- The Octocat : Fix typo
5- The Octocat : Add license
```

*Note: The default branch is `main`. If the repository uses a different branch, specify it as the third argument.*

---

## Environment Variables

The tool requires a GitHub API token to authenticate requests. Add the following variable to your `.env` file:

```env
GIT_API_TOKEN=your_github_api_token_here
```

You can obtain a personal access token from your GitHub account settings.

---

## Requirements

The project depends on the following Python libraries:

- `requests==2.32.3`: For making HTTP requests to the GitHub API.
- `python-dotenv==1.0.1`: For loading environment variables from a `.env` file.

These dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```

---

## Contributing

 Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Please ensure that your code adheres to the existing style and includes appropriate tests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub Issues](https://github.com/your-repo-url/issues) page.
