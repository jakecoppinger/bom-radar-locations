#!/usr/bin/env python3

import shapefile
import json

# wget ftp://ftp.bom.gov.au/anon/home/adfd/spatial/IDR00007.dbf
# :)
sf = shapefile.Reader("IDR00007.dbf")

# Exclude the first item (deletionFlag)
fields = [d[0] for d in sf.fields][1:]
records = sf.records()

locations = []

for record in records:
    location = {}
    for i in range(len(fields)):
        key = fields[i]
        value = record[i]
        location[key] = value
    locations.append(location)

# Pretty print JSON
s = json.dumps(locations, sort_keys=True, indent=2)
print(s)
