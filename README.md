# Legal MD: Markdown for Legal Documents

[![Build Status](https://travis-ci.org/openlegaldata/legal-md.svg?branch=master)](https://travis-ci.org/openlegaldata/legal-md) [![Coverage Status](https://coveralls.io/repos/github/openlegaldata/legal-md/badge.svg?branch=master)](https://coveralls.io/github/openlegaldata/legal-md?branch=master)

*!!! THIS EXTENSION IS STILL WORK-IN-PROGRESS !!!*

Extension for [Python-Markdown](https://python-markdown.github.io/). Supported features:

- Line numbers: Convert paragraph numbers into HTML tables
- Special links: Semantic annotation and citation markers


## Install

```
pip install git+https://github.com/openlegaldata/legal-md.git#egg=legal-md

# Install locally (dev purpose)
pip install -e /var/www/apps/oldp/app/
```

## Usage

```python
import markdown

md_str = '# Title\n'
md_str += '1| Paragraph with line number\n'

html = markdown.markdown(md_str, extensions=[
    'legal_md.extensions.line_numbers',
])

```

## License

not licensed yet
