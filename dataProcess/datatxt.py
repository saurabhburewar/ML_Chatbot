import json
import pandas as pd


f1 = open("ceosubset.json", errors='ignore')
fw = open("ceonames1.txt", 'w', errors='ignore')
data = json.load(f1)

items = []

for item in data["company"]:
    fw.write("- " + item["Object"] + "\n")
    # fw.write(item["Subject"] + "\n")
    # fw.write(item["Object"] + "\n")

    # i = d["passages"]
    # doctext = d["documentText"]
    # properties = i[0]['exhaustivelyAnnotatedProperties']
    # prophere = properties[0]['propertyName']
    # passage = i[0]["passageText"]
    # facts = i[0]['facts']
    # if len(facts) != 0:
    #     for fact in facts:
    #         df_item = {
    #             "Text": doctext,
    #             "Subject": fact["subjectText"],
    #             "Relation": prophere,
    #             "Object": fact["objectText"]
    #         }

    #         fw.write(fact["subjectText"] + "\n")
    #         fw.write(fact["objectText"] + "\n")
    #         count += 1

    # if count > 120:
    #     break

f1.close()
fw.close()
