# brainyquote-API
Unofficial API of brainyquote.com for random quotes.

## Requirements

A requirements.txt was provided.
You must have python 3.x with pip.
Then follow the installation process.

## Installation

```
git clone https://github.com/memoriasIT/Brainyquote-API.git

pip install -r requirements.txt
```

## Usage

A demo is provided when the script is executed.
```python
# Demo: Get 40 quotes of the category 'Amazing'
# category() generates a list of categories
print("Category '%s'" % category()[2])

# quotes() gets the quotes given a category name and a number of desired quotes
demoResult = quotes(category()[2], 40)
print("Got %d quotes" % len(demoResult))
print("Example: %s" % demoResult[0])
```

## Disclaimer

This is totally unofficial and not associated with brainyquote.com by any means.
The software was provided for educational purposes only as according to point 5 of brainyquote terms of service:

> You may access and use our Site only for your personal use. Any other access to or use of the Site or its content constitutes a violation of this Agreement and may violate applicable copyright, trademark, or other laws.
>
> You may not access, use, or copy any portion of the Site or its content through the use of bots, spiders, scrapers, web crawlers, indexing agents, or other automated devices or mechanisms.

By downloading this software you agree with this disclaimer and the author does not hold any responsibility for the bad use of this code.