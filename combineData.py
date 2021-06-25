import pandas as pd
import csv
df = pd.read_csv('devices.csv')
# df.iloc[2][1]
k=df.loc[df['maso']=='PD']
print(df)

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('outputCombine.csv', 'w') as output:
        writer = csv.writer(output)
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
                writer.writerow(['maso','name','idpic'])
            else:
                
                # print(f'\t{row[0]} works in the {row[1]} department')
                # id=splitString(row[1])
                # print(id)
                # writer.writerow([row[0],id])
                dataRoot=df.loc[df['maso']==row[0]]
                writer.writerow([row[0],dataRoot.iloc[0][1],row[1]])
                line_count += 1
        print(f'Processed {line_count} lines.')
