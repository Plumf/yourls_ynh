import json

with open("/etc/ssowat/conf.json.persistent", "r", encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)
    data["protected_urls"].remove("__DOMAIN__/__PATH__/admin")

with open("/etc/ssowat/conf.json.persistent", "w", encoding='utf-8') as jsonFile:
	jsonFile.write(json.dumps(data, indent=4, sort_keys=True))
