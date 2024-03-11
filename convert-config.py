#!/usr/bin/env python3

import tomllib; import sys; import json; o=tomllib.load(open(sys.argv[1], "rb"))["rules"]; o=[e for e in o if e["id"] != "generic-api-key"]

print(json.dumps(o, indent=2))
