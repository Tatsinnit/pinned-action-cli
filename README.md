# Pinned Actions CLI

Pinned Actions CLI is a tool to automatically pin GitHub Actions dependencies in your workflow files. It replaces unpinned actions with their corresponding SHA values to ensure reproducibility and security.

## Features

- Fetches the SHA for a given GitHub Action version.
- Replaces unpinned actions in workflow files with pinned SHAs.
- Simple command-line interface.

## Installation

You can install the Pinned Actions CLI using local build:

```sh
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install requests pyyaml click
```

## Usage

To pin GitHub Actions dependencies in your workflow files, run the following command:

```sh
pip install -e .
pin-actions <directory>
```

Replace `<directory>` with the path to your repository.

## Example

```sh
pin-actions /path/to/your/repo
```

This command will look for workflow files in the `.github/workflows` directory of your repository and replace unpinned actions with their corresponding SHAs.

## Requirements

- Python 3.6+
- `requests`
- `pyyaml`
- `click`

## Development

To contribute to the development of this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pinned-actions-cli.git
    ```
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the tests:
    ```sh
    python -m unittest discover tests
    ```

## License

This project is licensed under the MIT License.
