clean:
	rm -rf dist build *.egg-info
upload: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*
