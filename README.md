# FastAPI Template

This sample repo contains the recommended structure for a Python FastAPI project. In this sample, we use `fastapi` to build a web application and `pytest` to run tests.

For a more in-depth tutorial, see our [FastAPI tutorial](https://code.visualstudio.com/docs/python/tutorial-fastapi).

The code in this repo aims to follow Python style guidelines as outlined in [PEP 8](https://peps.python.org/pep-0008/).

## Set up instructions

This sample makes use of Dev Containers. To leverage this setup, make sure you have [Docker installed](https://www.docker.com/products/docker-desktop).

### Prerequisites

- Python 3.10.12

### Create and activate virtual environment

```bash
python3 -m venv tableau-fastapi-venv
source tableau-fastapi-venv/bin/activate  # On Windows use `tableau-fastapi-venv\Scripts\activate`
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the sample

- Open the project folder in your preferred IDE or text editor.
- If using Dev Containers, open the project in a Dev Container.
- Run the app using the following command:
  ```bash
  python3 main.py
  ```
- Open your web browser and navigate to `http://127.0.0.1:8000` to see the running application.
- Test the API functionality by navigating to `/docs` URL to view the Swagger UI.
- Configure and run tests using your preferred testing framework or IDE.

## Recommended VS Code Extensions

If you are using VS Code, the following extensions are recommended:

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

In addition to these extensions, there are a few settings that are also useful to enable. You can enable the following settings by opening the Settings editor (`Ctrl+,`) and searching for the following settings:

- Python > Analysis > **Type Checking Mode** : `basic`
- Python > Analysis > Inlay Hints: **Function Return Types** : `enable`
- Python > Analysis > Inlay Hints: **Variable Types** : `enable`

# Tableau DataDev 2024-2025 Hackathon

## Requirements

- Python 3.10.12
- FastAPI
- Uvicorn
- python-dotenv
- tableauserverclient
- tableauhyperapi

## Setup

1. Create a virtual environment with Python 3.10:
   ```sh
   python3.10 -m venv venv
   ```

2. Activate the virtual environment:
   ```sh
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Tableau Cloud credentials:
   ```
   TABLEAU_SERVER_URL=https://10ax.online.tableau.com
   TABLEAU_USERNAME=your-username
   TABLEAU_PASSWORD=your-password
   TABLEAU_SITE_ID=your-site-id
   ```

5. Run the application:
   ```sh
   uvicorn main:app --reload
   ```

## Usage

- Access the API at `http://127.0.0.1:8000`
