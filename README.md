# PdfParamExtractor
1. Create a Python virtual environment:
	```
    python -m venv .venv
	```

2. Activate the virtual environment:
	```
	.\venv\Scripts\activate
	```

3. Upgrade pip (recommended):
	```
	python -m pip install --upgrade pip
	```

4. Install dependencies:
	```
	pip install -r requirements.txt
	```
    You are now ready to use the project!

5. To run :
   ```
    fastapi dev main.py
   ```
    Local server can be accessed at  http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs

6. To deactivate venv:
   ```
   deactivate
   ```

7. Mongo Db details: 
   ```
   URL: mongodb+srv://PDFParamInformation:6uLnknAjIcBCPz8K@cluster0.dh6bh6p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   Cluster: Cluster0
   Schema: PDFParamInformation
   Password: 6uLnknAjIcBCPz8K
   DB: parametrix
   Collection: part_info
   ```
