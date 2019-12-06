# zbmath-api
API wrapper for zbMATH

## How to Run

```bash
$ pip3 install -r requirements.txt
$ FLASK_APP=app.py flask run
```

You can also use virtual environments, as long as you install all required packages.

## API Documentation

### GET `/search`

Search for a list of documents within zhMATH system.

Query parameters

* query: The search term, plain-text, do not URL encode.

Response Example

```json
[
    {
        "authors": [
            "Mielke, Eckehard W."
        ],
        "link": "https://zbmath.org/?q=an%3A1365.81006",
        "title": "Geometrodynamics of gauge fields. On the geometry of Yang-Mills and gravitational gauge theories. 2nd edition."
    },
    {
        "authors": [
            "Deriglazov, Alexei A.",
            "Pupasov-Maksimov, Andrey M."
        ],
        "link": "https://zbmath.org/?q=an%3A1368.81103",
        "title": "Relativistic corrections to the algebra of position variables and spin-orbital interaction."
    },
    {
        "authors": [
            "Jellal, Ahmed"
        ],
        "link": "https://zbmath.org/?q=an%3A1364.82074",
        "title": "Integer quantum Hall effect in graphene."
    }
]
```