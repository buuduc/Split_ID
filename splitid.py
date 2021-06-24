import csv
def splitString(text):
    header=text.count('https://drive.google.com/file/d/')
    textsub=text.replace('https://drive.google.com/file/d/','')
    textsub=textsub.replace('/view?usp=sharing','')
    return textsub


with open('idpic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('output.csv', 'w') as output:
        writer = csv.writer(output)
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
                writer.writerow(['maso','id'])
            else:
                
                # print(f'\t{row[0]} works in the {row[1]} department')
                id=splitString(row[1])
                print(id)
                writer.writerow([row[0],id])
                line_count += 1
        print(f'Processed {line_count} lines.')

