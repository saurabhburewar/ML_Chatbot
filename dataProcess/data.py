import json
import pandas as pd
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

stopwords = stopwords.words("english")


def hasnum(inputString):
    return any(char.isdigit() for char in inputString)


f1 = open("train.json", "r", errors='ignore')
f2 = open("ceosubset.json", "w", errors='ignore')

# df = pd.DataFrame(columns=["id", "Text", "Subject", "Relation", "Object"])
items = []

for item in f1:
    d = json.loads(item)
    i = d["passages"]
    properties = i[0]['exhaustivelyAnnotatedProperties']
    prophere = properties[0]['propertyName']
    passtext = i[0]["passageText"]
    facts = i[0]['facts']
    if len(facts) != 0:
        for fact in facts:
            if fact["subjectText"].lower() not in stopwords and fact["objectText"].lower() not in stopwords and not hasnum(fact["subjectText"].lower()) and not hasnum(fact["objectText"].lower()):
                df_item = {
                    "id": fact["factId"],
                    "Text": passtext,
                    "Subject": fact["subjectText"],
                    "Relation": prophere,
                    "Object": fact["objectText"]
                }

                # if prophere == 'DATE_FOUNDED':
                #     # df = df.append(df_item, ignore_index=True)
                #     items.append(df_item)

                # if prophere == 'HEADQUARTERS':
                #     # df = df.append(df_item, ignore_index=True)
                #     items.append(df_item)

                # if prophere == 'SUBSIDIARY_OF':
                #     # df = df.append(df_item, ignore_index=True)
                #     items.append(df_item)

                # if prophere == 'FOUNDED_BY':
                #     # df = df.append(df_item, ignore_index=True)
                #     items.append(df_item)

                if prophere == 'CEO':
                    # df = df.append(df_item, ignore_index=True)
                    items.append(df_item)

            # break

    if len(items) > 150:
        break

# df.to_csv("subset.csv")
d = {
    "company": items
}

json.dump(d, f2)
