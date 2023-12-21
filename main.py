import re
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", ) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

pattern = r"(\+7|8{1})( *)(\(*)(\d{3})(\)*)( |-*)(\d{3})(\ |-*)(\d{2})( |-*)(\d{2})( \(*((доб.) (\d{4}))\)*)*"
subst = r"+7(\4)\7-\9-\11 \14\15"

for id, lists in enumerate(contacts_list[1::]):
    for idx, columns in enumerate(lists[0:3]):
        columns = columns.split()
        while len(columns) != 1 and len(columns) != 0:
            if len(columns) == 2:
                lists[idx + 1] += columns.pop()
                lists[idx] = columns[0]
            if len(columns) == 3:
                lists[idx + 2] += columns.pop()    
        else:
            continue
    lists[5] = (re.sub(pattern, subst, lists[5])).strip()
    for ids, lists_duo in enumerate(contacts_list[1::]):
        if len(set(lists[0:3]) & set(lists_duo[0:3])) >= 2 and lists != lists_duo:
            contacts_list[ids + 1] = list(map(max, zip(lists, lists_duo)))
            contacts_list[id + 1] = list(map(max, zip(lists, lists_duo)))

contacts = []
[contacts.append(x) for x in contacts_list if x not in contacts]
contacts_list = contacts
  
## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)