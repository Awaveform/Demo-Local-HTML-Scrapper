import pathlib
import re


# TODO:
#   -   Task_1
#   -   Task_2


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# lists, variables, index values
keyword_list = ['src', 'alt', 'href']
keyword_list_2 = ['unwanted_example_1', 'unwanted_example_2', 'unwanted_example_3']
keyword_list_3 = ['tel:', 'mailto:']
keyword_3 = 'doctype'
preheader = '<div>necessary_example_1</div>'
finish_list = []
finish_list_links = []
finish_list_contacts = []
finish_list_contacts_add = []
condition_1 = 'keyword: alt'
condition_2 = 'keyword: src'
condition_3 = 'keyword: href'
condition_4 = 'tel:'
condition_5 = 'mailto:'
list1 = []
list2 = []
list3 = []
list4 = []
list_add = []
list_doctype = []
index = 1
index_2 = 1
index_3 = 1
index_4 = 1
index_5 = 1
index_6 = 1
test_index = 1
index_p = 0

checks = ['check_01', 'check_02', 'check_03', 'check_04', 'check_05', 'check_06', 'check_07', 'check_08']


# open each file in the folder, each string, replenishment of lists with variables depending on conditions
for file in pathlib.Path(r'.').glob('*.html'):  # **/*.html - add subdirs in search // you can add your local absolute path in this part - "r.('HERE')"
    with open(file, encoding='utf-8') as a:
        index_p = 0
        index_d = 0
        for line in a:

            lower_line = line.lower()
            for c in keyword_list:
                if c in lower_line:
                    list1.append(' keyword: ' + c + ' filepath: ' + str(file) + ' line: ' + lower_line.strip())
            for c2 in keyword_list_2:
                if c2 in lower_line:
                    list2.append(c2 + ' --- filepath: ' + str(file))
                    list2.append('')
            for c3 in checks:
                if c3 in lower_line:
                    list_add.append('example_match: ' + c3 + ' --- filepath: ' + str(file))
            for c4 in keyword_list_3:
                if c4 in lower_line:
                    list4.append('filepath: ' + str(file) + ' line: ' + lower_line.strip())
            if preheader in lower_line:
                index_p += 1
            if keyword_3 in lower_line:
                index_d += 1
        print(lower_line)
        if index_p == 0:
            list3.append('--- filepath: ' + str(file))
        if index_d == 0:
            list_doctype.append('--- filepath: ' + str(file))
    list1.append('   ')
    list4.append('   ')

# filter of the text in created lists / re
for elem in list1:
    if condition_1 in elem:
        match = re.search(r'alt="(.*?)"', elem)
        if match:
            elem2 = match.group(0)
            elem3 = ''.join(elem.partition('line: ')[0:1])
            finish_list.append(elem3 + elem2)
    elif condition_2 in elem:
        match = re.search('src=\S+', elem)
        if match:
            elem4 = match.group(0)
            elem5 = ''.join(elem.partition('line: ')[0:1])
            finish_list.append(elem5 + elem4)
    elif condition_3 in elem:
        match = re.search('href="(.*?)"', elem)
        if match:
            elem6 = match.group(0)
            elem7 = ''.join(elem.partition('line: ')[0:1])
            finish_list_links.append(elem7 + elem6)
    else:
        finish_list.append(elem)
        finish_list_links.append(elem)

for elem8 in list4:
    if condition_4 in elem8:
        match = re.search(r'"tel:\S*"', elem8)
        if match:
            elem9 = match.group(0)
            elem10 = ''.join(elem8.partition('line: ')[0:1])
            finish_list_contacts.append((elem10 + elem9).replace('"', ''))
    elif condition_5 in elem8:
        match = re.search('"mailto:\S*"', elem8)
        if match:
            elem11 = match.group(0)
            elem12 = ''.join(elem8.partition('line: ')[0:1])
            finish_list_contacts.append((elem12 + elem11).replace('"', ''))
    else:
        pass

# iterate n in the finish_list and its' print in the string
print("")
print(Color.BOLD + Color.RED + "SRCs & ALTs of each HTML document:" + Color.END)
for el in finish_list:
    if el == '   ':
        print(el)
    elif el != '':
        print(f'{index}' + ' ' + el)
        index += 1
    else:
        print(el)

print("")
print(Color.BOLD + Color.RED + "Href links of each HTML document:" + Color.END)
for el6 in finish_list_links:
    if el6 == '   ':
        print(el6)
    elif el6 != '':
        print(f'{index_6}' + ' ' + el6)
        index_6 += 1
    else:
        print(el6)

# printing the title, unwanted matches and the file path where it was found
print("")
print(Color.BOLD + Color.RED + "Unwanted Match:" + Color.END)
for el2 in list2:
    if '"#"' in el2:
        print(f'{index_2} placeholder match --- ' + el2)
        index_2 += 1
    elif 'unwanted_example_1' in el2:
        print(f'{index_2} unwanted_example_1 match --- ' + el2)
        index_2 += 1
    elif 'unwanted_example_2' in el2:
        print(f'{index_2} unwanted_example_2 match --- ' + el2)
        index_2 += 1
    else:
        print(el2)

if not list2:
    print('- Ok -')

print("")
print(Color.BOLD + Color.RED + "Missed Preheader:" + Color.END)

# iteration the n element in list3 and its' print in a string
for el3 in list3:
    print(str(index_3) + " " + el3)
    index_3 += 1

if not list3:
    print('- Ok -')

list_add = list(dict.fromkeys(list_add))

print("")
print(Color.BOLD + Color.RED + "Warning Match:" + Color.END)

for el4 in list_add:
    print(str(index_4) + " " + el4)
    index_4 += 1

if not list_add:
    print('- Ok -')

print("")
print(Color.BOLD + Color.RED + "Missed Doctype:" + Color.END)

for el5 in list_doctype:
    print(str(index_5) + " " + el5)
    index_5 += 1

if not list_doctype:
    print('- Ok -')

print("")
print(Color.BOLD + Color.RED + "Contact Information:" + Color.END)
for el7 in finish_list_contacts:
    if ('+777' or '+888') in el7.strip():
        finish_list_contacts_add.append(el7 + ' - phone number match: NAME_1')
    elif ('+111' or '+222') in el7.strip():
        finish_list_contacts_add.append(el7 + ' - phone number match: NAME_2')

    elif 'example1@mail.com' in el7.strip():
        finish_list_contacts_add.append(el7 + ' - mail address match: NAME_1')
    elif 'example2@mail.com' in el7.strip():
        finish_list_contacts_add.append(el7 + ' - mail address match: NAME_2')
    else:
        finish_list_contacts_add.append(el7.strip() + ' - contact is UNKNOWN')

for el8 in finish_list_contacts_add:
    if el8 == '   ':
        print('')
    else:
        print(str(test_index) + ' ' + el8)
        test_index += 1

if test_index == 1:
    print('- No contacts were found -')
