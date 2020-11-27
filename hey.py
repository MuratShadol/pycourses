# Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно s1, s2, ..., sn рублей в
# год (эти числа вводятся и обрабатываются последовательно).
# Ежегодно в результате износа и морального старения
# (амортизации) все имеющееся оборудование уценивается на р%. Какова общая стоимость накопленного оборудования
# за n лет?

years = 5
price_1 = int(input("Цена 1: "))
price_2 = int(input("Цена 2: "))
price_3 = int(input("Цена 3: "))
price_4 = int(input("Цена 4: "))
price_5 = int(input("Цена 5: "))
depreciation = 0.5
total_price = 5 * depreciation * price_1 + 4 * depreciation * price_2 + 3 * depreciation * price_3 + \
              2 * depreciation * price_4 + depreciation * price_5
print("Итоговая цена: ", total_price)
