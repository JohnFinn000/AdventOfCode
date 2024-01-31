GTEST = /usr/local/lib/libgtest.a

python_test: *.py
	@echo "Running Python tests"
	python3 -m unittest discover -p '*.py' -v

ruby_test: *.rb
	@echo "Running Ruby tests"
	rspec *.rb

go_test: *.go
	@echo "Running Go tests"
	CGO_ENABLED=0 go test

cpp_test: *.cpp
	g++ -Wall -W -std=c++17 -o cpp day.cpp ${GTEST}
	./cpp
	rm cpp

test: python_test ruby_test

clean:
	rm *.pyc
