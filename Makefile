
ACTIVATE := source venv/bin/activate

install: venv
	$(ACTIVATE) && pip install --upgrade pip && pip install -r requirements.txt

act:
	$(ACTIVATE)

run: 
	uvicorn main:app --host 0.0.0.0 --port 8080 --reload


clean:
	rm -rf venv
