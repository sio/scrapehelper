.PHONY: test
test: venv
	$(VENV)/python -m unittest


.PHONY: test-verbose
test-verbose: venv
	$(VENV)/python -m unittest -v


include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2019.11.06/Makefile.venv"
	echo "93744514780c15f916dd0e26e5827afae23b92cc62704bb2dd8b9e2bb0370a96 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv


.PHONY: test-codestyle
test-codestyle: $(VENV)/pyflakes
	$(VENV)/pyflakes scrapehelper tests
