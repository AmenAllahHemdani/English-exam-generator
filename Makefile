install:
	pip install --upgrade pip && pip install -r requirements.txt

run: 
	uvicorn main:app --host 0.0.0.0 --port 8080 --reload

clean:
	rm -rf venv
