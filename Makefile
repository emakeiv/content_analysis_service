install:
	pip install --upgrade pip  &&\
		pip install -r requirements.txt 
format:
	#black
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
