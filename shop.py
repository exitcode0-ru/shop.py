purchases = []
running = True
total = 0
total_quantity = 0
best = None
worst = None
while running:
    purchase = {}

    purchase["name"] = input("Название товара: ")
    if purchase["name"] == "":
        print("Неверное значение")
        continue
    try:
        purchase["quantity"] = int(input("Количество товара: "))
    except:
        print("Количество должно быть числом")
        continue
    if purchase["quantity"] <= 0:
        print("Количество должно быть больше 0")
        continue
    elif purchase["quantity"] > 100:
        print("Слишком большое количество")
        continue

    try:
        purchase["price"] = float(input("Цена товара: "))
    except ValueError:
        print("Цена должна быть числом")
        continue
    if purchase["price"] <= 0:
        print("Цена должна быть больше 0")
        continue
    elif purchase["price"] > 10000:
        print("Слишком высокая цена")
        continue

    cost = purchase["quantity"] * purchase["price"]
    total = total + cost
    total_quantity = total_quantity + purchase["quantity"]
    
    purchases.append(purchase)

    while running:
        answer = input("Хотите ввести ещё одну покупку? (да/нет) ")
        answer = answer.lower()
        if answer == "да":
            break
        elif answer == "нет":
            running = False
            print("Программа завершена")
        else:
             print("Неизвестный ответ")
            

for purchase in purchases:
    cost = purchase["quantity"] * purchase["price"]
    if best is None or cost > best_cost:
        best = purchase
        best_cost = cost

for purchase in purchases:
    cost = purchase["quantity"] * purchase["price"]
    if worst is None or cost < worst_cost:
        worst = purchase
        worst_cost = cost

if total_quantity <= 0:
    print("Неверная запись")
else:
    average_price = total / total_quantity
    print(f"Средняя цена одного товара: {average_price:.2f}")

if len(purchases) > 0:
    average = total / len(purchases)
    print(f"Средняя стоимость: {average:.2f}")

if len(purchases) > 0:
    print("Самая дорогая покупка:", best["name"], "-", best_cost)
    print("Самая дешевая покупка:", worst["name"], "-", worst_cost)
else:
    print("Покупок нет")

for purchase in purchases:
    print(f"{purchase['name']} - {purchase['quantity']} шт. по {purchase['price']:.2f}")

print("Всего покупок:", len(purchases))
print(f"Общее количество товаров: {total_quantity}")
print(f"Общая сумма {total:.2f}")

search_name = input("Введите название товара для поиска: ")
search_name = search_name.lower()

if search_name == "":
    print("Название не введено, поиск пропущен")
else:
    found_count = 0
    found_total = 0
    for purchase in purchases:
        if search_name in purchase["name"].lower():
            found_count = found_count + 1
            cost = purchase["quantity"] * purchase["price"]
            found_total = found_total + cost
            print(f"{purchase['name']} - {purchase['quantity']} шт. по {purchase['price']:.2f}")
    if found_count == 0:
        print("Товар не найден")
    else:
        print(f"Найдено покупок: {found_count}")
        print(f"Общая стоимость найденных товаров: {found_total:.2f}")
