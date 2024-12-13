# Code Citations

This document provides citations for the code used in the Tableau DataDev 2024-2025 Hackathon project.

## Libraries and Frameworks

1. **Pandas**
    - Citation: McKinney, Wes. "Data Structures for Statistical Computing in Python." Proceedings of the 9th Python in Science Conference. 2010.
    - URL: https://pandas.pydata.org/

2. **NumPy**
    - Citation: Harris, Charles R., et al. "Array programming with NumPy." Nature 585.7825 (2020): 357-362.
    - URL: https://numpy.org/

3. **Matplotlib**
    - Citation: Hunter, J. D. "Matplotlib: A 2D graphics environment." Computing in Science & Engineering 9.3 (2007): 90-95.
    - URL: https://matplotlib.org/

## License: MIT
https://github.com/jazzwang/snippet/tree/b075f3afacb8c0510b7fd7b61919e4d2903c9edb/python/fastapi/MEMO.md

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}