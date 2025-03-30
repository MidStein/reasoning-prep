all: anki moodle

organise:
	python organise.py

anki: organise
	python anki.py

moodle: organise
	python moodle.py
