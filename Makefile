VENV = venv
VBIN = $(VENV)/bin


all: test


$(VBIN)/%:
	python3 -m venv venv

	chmod +x $(VBIN)/activate
	./$(VBIN)/activate

	$(VBIN)/pip install -r requirements.txt
	$(VBIN)/pip install -e lib


test: $(VBIN)/pytest
	$(VBIN)/pytest tests

coverage.xml: $(VBIN)/pytest
	$(VBIN)/pytest tests --cov src
	coverage xml -o coverage.xml

htmlcov: $(VBIN)/coverage coverage.xml
	$(VBIN)/coverage html


clean:
	rm -rf htmlcov
	rm -f .coverage coverage.xml
	rm -rf */.pytest_cache
	rm -rf */__pycache__


fclean: clean
	rm -rf venv
	rm -rf lib/*.egg-info


.PHONY: all clean fclean test
