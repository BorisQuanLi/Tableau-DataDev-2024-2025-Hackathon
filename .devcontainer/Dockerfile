FROM python:3.9-slim

# Set the working directory
WORKDIR /workspace

# Copy the requirements file
COPY backend/requirements.txt /workspace/backend/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r /workspace/backend/requirements.txt

# Copy the rest of the application code
COPY backend /workspace/backend
