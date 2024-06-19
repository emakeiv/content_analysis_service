install:
	pip install --upgrade pip  &&\
		pip install -r requirements.txt 
format:
	black -l 86 $$(find * -name '*.py')
lint:
	# pylint
test:
	# test
build:
	#build
deploy:
	#deploy
all:
	install lint test build deploy
