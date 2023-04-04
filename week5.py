def freqword(filepath):
    with open(filepath) as file:
        counts=dict()
        for line in file:
            words=line.split()
            for word in words:
                counts[word]=counts.get(word,0)+1

        maxcount=None
        maxword=None
        for word,count in counts.items():
            if maxcount is None or count > maxcount:
                maxword=word
                maxcount=count

    return(f"The most frequent word is: {maxword},and the number of times appeared is :{maxcount}")


import pandas as pd
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
prices= [price for price in prc_date.keys()]
dates= [date for date in prc_date.values()]
series_stk = pd.Series(data=prices, index=dates)
print(series_stk)

dic = {i:i+1 for i in range(10000)}
series_ones = pd.Series(data=[1]*10000, index=range(10000))
print(series_ones)


import pandas as pd
df = pd.DataFrame(
    {
        'col1': range(10),
        'col2': range(10, 20)
    },
    index=list('acgfhibdje')
)

x= df.loc[['b', 'c', 'd', 'e'], 'col1']
print(x)


x2=df.loc[['b', 'd', 'f', 'j'], ['col1']]
print(x2)