all:
	python generate.py
clean:
	find . -maxdepth 1 -iname '[0-9][0-9][0-9].html' -not -iname '418.html' -exec rm \{\} \;
