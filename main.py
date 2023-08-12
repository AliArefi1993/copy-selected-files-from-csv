import csv
import os

def eliminate_short_question(in_path, out_path):
    lines = list()

    with open(in_path, 'r') as readFile:
        reader = csv.reader(readFile)
        not_first = False
        for row in reader:
            lines.append(row)
            if len(row[3].split()) < 7 and not_first:
                lines.remove(row)
            not_first = True

    with open(out_path, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

def bring_out_specified_number_of_data(n, in_path, out_path):
    lines = list()
    with open(in_path, 'r') as readFile:

        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)

    total_line_number = len(lines)
    print(total_line_number//n)
    print("total_line_number", total_line_number)
    selected_lines = list()
    line_counter = 0
    for i in range(0,total_line_number, total_line_number//n):
        print(i)
        selected_lines.append(lines[i])
        if line_counter == n:
            break
        line_counter += 1
    with open(out_path, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(selected_lines)

def list_selected_wav_path(in_path):
    lines = list()
    with open(in_path, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(os.path.join("/home/emdad/test/hooshtel-emdad-khodro/logs", "bot" + row[7],row[6]))
    return lines

outfile = eliminate_short_question("after-sales.csv", "first_edit.csv")
outfile = bring_out_specified_number_of_data(97, "first_edit.csv", "after_sales_second_edit.csv")
list_of_selected_wav_path = list_selected_wav_path("after_sales_second_edit.csv")
print(list_of_selected_wav_path)
for i, j in enumerate(list_of_selected_wav_path):
    print("i:", i)
    print("j:", j)
    destination_path = os.path.join("./integrated", str(i)+j[-4:])
    cmd = f"cp {j} {destination_path}"
    print(cmd)
    # os.system(cmd)
