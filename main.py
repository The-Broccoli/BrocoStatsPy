fobj = open("Daylio-export.csv")
da_list = []
for line in fobj:
    splitLine = line.split(',')
    # Super Gut Ok Schlecht Lausig
    if splitLine[4] == 'Super':
        da_list.append(5)
    if splitLine[4] == 'Gut':
        da_list.append(4)
    if splitLine[4] == 'Ok':
        da_list.append(3)
    if splitLine[4] == 'Schlecht':
        da_list.append(2)
    if splitLine[4] == 'Lausig':
        da_list.append(1)
print(da_list)
fobj.close()

import matplotlib.pyplot as plt
plt.xlabel('Tage')
plt.ylabel('Stimmung')
#plt.plot (X, Y, color='blue', alpha=1.00)
plt.plot(da_list, color='green')
plt.show()