invoice = ('0.....6.................................40.......52....55........\n'
            '1909  Pimoroni PiBrella                 $17.50    3    $52.50\n'
            '1489  Tactile Switch x20                $4.95     2    $9.90\n'
            '1510 Panavise Jr. - PV-201              $28.00    1    $28.00\n')
#name for the slice
SKU = slice(0,6)
DESC = slice(6, 40)
PRICE = slice(40, 52)
QUANTITY = slice(52,55)
TOTAL = slice(55, None)
line_items = invoice.split('\n')
for item in line_items:
    print(item[PRICE], item[DESC])

l = list(range(10))
print(l)

l[2:5] = [20,30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

#如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代
#对象。即便只有单独一个值，也要把它转换成可迭代的序列。
#l[2:5] = 100
#print(l)


l[2:5] = [100]
print(l)

#多维切片和省略
#[]运算符里还可以使用以逗号分开的多个索引或者切片，外部库Numpy里就有用到这个特性
#二维的numpy.ndarray, 就可以用a[i.j], 来取值，用a[m:n, k:l]的方式来取得二维切片。
#http://wiki.scipy.org/Tentative_NumPy_Tutorial