import matplotlib.pyplot as plt

cardsPerDayList = [179,220,191,264,241,197,219,245,325,230,310,303,253,228,217,250,201,301,214,211,231,208,225,210,231,224,221,176,200,197,231,224,239,217,248,213,217,235,318,260,236,231,293,237,223,283,245,204,216,214,231,211,270,265,212,295,273,178,223,246,207,180,193,189,188,250,273,215,220,206,198,220,234,294,173,194,237,208,213,220,456,286,241,207,270,228,279,281,205,190,190,392,244,214,338,191,202,217,248,214,221,266,226,279,187,320,218,190,262,257,224,234,268,228,256,220,187,270,195,177,185,183,226,234,171,199,153,185,196,244,168,173,196,174,172,166,176,145,179,171,159,152,164,166,145,148,139,142,149,133,168,141,114,140,124,142,96,120,144,128,129,102,124,100,90,120,310,112,147,124,207]

joursList = [k for k in range(len(cardsPerDayList))]

totCardsPerDayList = [cardsPerDayList[0]]

for i in range(1, len(cardsPerDayList)):
    totCardsPerDayList.append(totCardsPerDayList[-1] + cardsPerDayList[i])

plt.plot(joursList, cardsPerDayList, label="Cartes crées chaque jour")
#plt.plot(joursList, totCardsPerDayList, label="Cartes crées au total")
plt.xlabel("Jours depuis l'ouverture")
plt.ylabel("Nb de cartes crées")
plt.legend()
plt.show()