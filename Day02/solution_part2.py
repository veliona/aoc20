import re

with open('data.csv.txt') as data:
    passwords = [line.strip() for line in data]

    result_valid_passwords = 0

    for password in passwords:
        min_number = int(re.findall(r"^.*?(?=-)", password)[0])
        max_number = int(re.findall(r"(?<=\-)(.*?)(?=\ )", password)[0])
        letter = re.findall(r"(?<=\ )(.*?)(?=\:)", password)[0]
        password_value_list = list(re.findall(r"(?<=: ).*$", password)[0])
        password_value = re.findall(r"(?<=: ).*$", password)[0]
        if (password_value_list[min_number - 1] == letter) & (password_value_list[max_number - 1] != letter):
            result_valid_passwords += 1
        elif (password_value_list[min_number - 1] != letter) & (password_value_list[max_number - 1] == letter):
            result_valid_passwords += 1
    print(result_valid_passwords)
