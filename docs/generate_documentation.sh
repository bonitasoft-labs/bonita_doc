#!/bin/sh

# parcourir bonita.json
python generate_doc.py bonita 7.5
python generate_doc.py bonita 7.6
python generate_doc.py bonita 7.7
python generate_doc.py bonita 7.8

# parcourir bcd.json
python generate_doc.py bcd 1.0
python generate_doc.py bcd 2.0
python generate_doc.py bcd 3.0

# parcourir bici.json
python generate_doc.py ici 1.0
python generate_doc.py ici 1.1
