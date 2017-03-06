# task-python-products

### Show Columns
 ```
 print(df.columns)
Index([u'code', u'piece', u'description', u'quantity', u'price'], dtype='object')
 ```

### Show All Products
 ```
 print(df.to_string())
    code      piece                   description  quantity   price
0      1  vestuario   camisa polo marca propria P       100    32.0
1      2  vestuario   camisa polo marca propria M       150    32.0
2      3  vestuario   camisa polo marca propria G       130    32.0
3      4  vestuario  camisa polo marca propria GG       130    32.0
4      5  vestuario                 camisa polo P        33    43.0
5      6  vestuario                 camisa polo M        83    43.0
6      7  vestuario                 camisa polo G        63    43.0
7      8  vestuario                camisa polo GG        93    43.0
8      9  vestuario           camisa polo tommy P        20    85.0
9     10  vestuario          camisa polo tommy M         70    85.0
10    11  vestuario           camisa polo tommy G        30    85.0
11    12  vestuario          camisa polo tommy GG        40    85.0
12    13  vestuario         camisa polo lacoste P        20    99.0
13    14  vestuario         camisa polo lacoste M        30    99.0
14    15  vestuario         camisa polo lacoste G        60    99.0
15    16  vestuario        camisa polo lacoste GG        12    99.0
16    17  vestuario          camisa polo beagle P        12    87.0
17    18  vestuario          camisa polo beagle M        66    87.0
18    19  vestuario          camisa polo beagle G        70    87.0
19    20  vestuario         camisa polo beagle GG        32    87.0
20    22  vestuario                calça social P        33    96.5
21    23  vestuario                calça social M        63    96.5
22    24  vestuario                calça social G        54    96.5
23    25  vestuario               calça social GG        19    96.5
24    26  vestuario               camisa social P         6    56.0
25    27  vestuario               camisa social M        56    56.0
26    28  vestuario               camisa social G        30    56.0
27    29  vestuario              camisa social GG        20    56.0
28    30  vestuario                       gravata       300    16.0
29    31  vestuario                          meia       400    16.0
30    32  vestuario                         boina       100    60.0
31    33  vestuario                        chapeu        89    56.0
32    34  vestuario                boina feminina        90    56.0
33    35  vestuario               chapeu feminino        89    76.0
34    36  vestuario               bermuda tommy P        20    36.0
35    37  vestuario               bermuda tommy M        40    36.0
36    38  vestuario               bermuda tommy G        10    36.0
37    39  vestuario              bermuda tommy GG        12    36.0
38    40  vestuario                       short P        29    46.0
39    41  vestuario                       short M        39    46.0
40    42  vestuario                       short G        20    46.0
41    43  vestuario                      short GG        30    46.0
42    44  vestuario                 relogio apple        10  4600.0
 ```


### Products by position 0 to 3
 ```
    code      piece                  description  quantity  price
0     1  vestuario  camisa polo marca propria P       100   32.0
1     2  vestuario  camisa polo marca propria M       150   32.0
2     3  vestuario  camisa polo marca propria G       130   32.0

 ```
 
### Find by name
 ```
 print(df[df['description'] == 'bermuda tommy GG'])
 37    39  vestuario  bermuda tommy GG        12   36.0

 ```
 
### Find by code
```
df[df['code'] == 6]
   code      piece    description  quantity  price
5     6  vestuario  camisa polo M        83   43.0
```
 
### Find by Price Greater Than 90.00
```
print(df[df['price'] > 90.00])
    code      piece             description  quantity   price
12    13  vestuario   camisa polo lacoste P        20    99.0
13    14  vestuario   camisa polo lacoste M        30    99.0
14    15  vestuario   camisa polo lacoste G        60    99.0
15    16  vestuario  camisa polo lacoste GG        12    99.0
20    22  vestuario          calça social P        33    96.5
21    23  vestuario          calça social M        63    96.5
22    24  vestuario          calça social G        54    96.5
23    25  vestuario         calça social GG        19    96.5
42    44  vestuario           relogio apple        10  4600.0

```

### Find by Price Less Than 20.00
```
print(df[df['price'] < 20.00])
28    30  vestuario     gravata       300   16.0
29    31  vestuario        meia       400   16.0
```

### Sum all quantity products
```
print(df['quantity'].sum())
2803
```

### Mean quantity products
```
print(df['quantity'].mean())
65.1860465116
```

### Product with max quantity
```
print( df.iloc[[int(df['quantity'].idxmax())]])
    code      piece description  quantity  price
29    31  vestuario        meia       400   16.0
```

### Product with smaller quantity
```
print( df.iloc[[int(df['quantity'].idxmin())]])
    code      piece      description  quantity  price
24    26  vestuario  camisa social P         6   56.0
```

### Product with max price
```
print( df.iloc[[int(df['price'].idxmax())]])
    code      piece    description  quantity   price
42    44  vestuario  relogio apple        10  4600.0
```

### Product with smaller price
```
print( df.iloc[[int(df['price'].idxmin())]])
Product with smaller price
    code      piece description  quantity  price
28    30  vestuario     gravata       300   16.0
```
