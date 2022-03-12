import glob
import json

file_names = glob.glob("*[0-9].json")


while True:
    url_key = input("Enter key name. Press enter for default (img_url): ")

    if url_key == "":
        url_key = "img_url"

    url_pref = input("Enter url prefix. Press enter for default (http://localhost:3000/) ")

    if url_pref == "":
        url_pref = "http://localhost:3000/"

    url_suff = input("Enter url suffix. Press enter for default (.png) ")

    if url_suff == "":
        url_suff = ".png"

    print(f"Current format (example 5.json): \"{url_key}\": \"{url_pref}5{url_suff}\"")
    ok = input("Ok? (y to continue, anything else to restart) ")

    if ok == "y" or ok == "Y":
        break


for file_name in file_names:
    with open(file_name, "r+") as f:
        content = json.load(f)

        content[url_key] = url_pref + file_name[:-5] + url_suff
        f.seek(0)
        json.dump(content, f)
        f.truncate()



