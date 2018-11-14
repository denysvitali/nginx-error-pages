import requests

r = requests.get('http://webconcepts.info/concepts/http-status-code.json')
json = r.json()

for i in json["values"]:
    template = "templates/" + i["value"][0:1] + "xx.html"
    with open(template) as f:
        content = f.read()
        new_content = content
        error_code = int(i["value"])

        print("Error Code: %d" % (error_code))

        if error_code == 418 or error_code < 400 or error_code > 599:
            continue
        new_content = new_content.replace("$ERROR_CODE", i["value"])
        new_content = new_content.replace("$ERROR_NAME", i["description"])
        new_content = new_content.replace("$ERROR_DESC", i["details"][0]["description"])
        with open(i["value"] + ".html", "w") as output_file:
            output_file.write(new_content)

with open("snippets/error_pages_content.conf", "w") as epc:
    for i in json["values"]:
        v = int(i["value"])
        if v < 400 or v > 599:
            continue
        print("error_page %d /%d.html;" % (v,v), file=epc)
