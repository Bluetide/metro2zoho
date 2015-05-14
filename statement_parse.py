import csv

with open('data/000101027265_0415_20150514164017.csv', newline='') as csvfile:
  with open('metrozoho.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    cs = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date-dd/MM/YYY', 'Withdrawals', 'Deposits', 'Payee', 'Description', 'Reference Number']) # write new header
    for line in cs:
        print (line)
        writer.writerow((line[4],line[8],line[7],'',line[5],line[6]))


# with open('MovimientoEst.txt', newline='',encoding='latin-1' ) as f:
#     reader = csv.reader(f,delimiter=';')
#     fecha = ''
#     for row in reader:
#         fecha= fecha + row[0]+","
#         # print(row[1])
#         # print(row[2])
#         # print(row[3])
#         # print(row[4])
#         # print(row[5])  balance
#
# print (type (fecha))
#
# with open("output.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(fecha)
