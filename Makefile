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
	echo "d32b54ae7cb0e99ec75cff9c4ef78c7050bc0c351f834464674fe4aa328ca370 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv


.PHONY: test-codestyle
test-codestyle: $(VENV)/pyflakes
	$(VENV)/pyflakes scrapehelper tests
