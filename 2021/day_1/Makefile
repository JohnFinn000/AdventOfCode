python_test: *.py
	@echo "Running Python tests"
	python -m unittest discover -p '*_test.py' -v

ruby_test: *.rb
	@echo "Running Ruby tests"
	rspec *_spec.rb

go_test: *.go
	@echo "Running Go tests"
	go test

clean:
	rm *.pyc

test: python_test ruby_test
