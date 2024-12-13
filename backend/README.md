# FastAPI Hackathon Project

This is a FastAPI project for the Tableau-DataDev-2024-2025-Hackathon.

## Setup

### Local Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Dev Container Setup

1. Open the project in VS Code.
2. Press `F1` and select `Remote-Containers: Open Folder in Container...`.
3. Select the project folder.
4. The container will build and start automatically.