test:
	nosetests --with-coverage --cover-html --cover-html-dir=tests/reports --no-byte-compile --cover-package=pypeup -w . --cover-erase

install:
	python setup.py install
	make clean

clean:
	rm -rf dist build *.egg-info