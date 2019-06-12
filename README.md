# Helpful library for scraping information from web

## Project status

New project, used by one person. The API changes should be backwards
compatible most of the time.


## Overview

This library provides helper tools for efficient and polite web scraping:

- Thread safe `RateLimiter` object
- Nice `BaseDataFetcher` class for creating custom data fetchers


## Installation

1. As a standalone Python package:
`pip install "https://github.com/sio/scrapehelper/tarball/master"`

2. As a dependency in your setup.py:
```python
    install_requires=[
        'scrapehelper @ https://github.com/sio/scrapehelper/tarball/master',
        # other dependencies
    ],
```


## Usage

API docs are yet to be written. The primary objects provided by this library
are `scrapehelper.fetch.BaseDataFetcher` and `scrapehelper.limit.RateLimiter`.

Check the code of the corresponding modules for more information. Submitting
documentation improvements via pull requests is very welcome!


## Support and contributing

If you need help with including this library into your Python project, please
create **[an issue](https://github.com/sio/scrapehelper/issues)**. Issues are
also the primary venue for reporting bugs and posting feature requests.
General discussion related to this project is also acceptable and very
welcome!

In case you wish to contribute code or documentation, feel free to open **[a
pull request](https://github.com/sio/scrapehelper/pulls)**. That would certainly
make my day!

I'm open to dialog and I promise to behave responsibly and treat all
contributors with respect. Please try to do the same, and treat others the way
you want to be treated.

If for some reason you'd rather not use the issue tracker, contacting me via
email is OK too. Please use a descriptive subject line to enhance visibility
of your message. Also please keep in mind that public discussion channels are
preferable because that way many other people may benefit from reading past
conversations. My email is visible under the GitHub profile and in the commit
log.



## License and copyright

Copyright 2019 Vitaly Potyarkin

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
