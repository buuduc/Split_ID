import pandas as pd
import csv
df = pd.read_csv('devices.csv')
# df.iloc[2][1]
# k=df.loc[df['maso']=='PD']
# print(df)
# for index,row in df.iterrows():
#     print(row['maso'])

# with open('output.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
with open('outputCombine.csv', 'w') as output:
    line_count = 0
    readerPic = pd.read_csv('output.csv')
    writer = csv.writer(output)
    for index,row in df.iterrows():
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
            writer.writerow(['maso','name','idpic'])
        else:
            
            # print(f'\t{row[0]} works in the {row[1]} department')
            # id=splitString(row[1])
            # print(id)
            # writer.writerow([row[0],id])
            dataRoot=readerPic.loc[df['maso']==row['maso']]
            if len(dataRoot)==0:
                idPic=''
            else:
                idPic=dataRoot.iloc[0][1]
            writer.writerow([row['maso'],row[1],idPic])
            line_count += 1
    print(f'Processed {line_count} lines.')