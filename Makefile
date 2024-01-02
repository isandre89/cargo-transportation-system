run:
	@python -B main.py

tests:
	@python -B tests.py

clean-pycache:
	@find . -name \*.pyc -delete
	@find . -name \*__pycache__ -delete 
