python_test: *.py
	@echo "Running Python tests"
	python -m unittest discover -p '*.py' -v

ruby_test: *.rb
	@echo "Running Ruby tests"
	rspec *.rb

test: python_test ruby_test

clean:
	rm *.pyc
