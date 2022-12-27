from console_app_for_big_data.sell import sell


def get_sell():
    file_name = 'michelin_data'

    while True:
        regions = {1: 'Georgia', 2: 'Russia', 3: 'Germany', 4: 'Spain', 5: 'USA', 6: 'India', 7: 'China'}
        [print(x, regions[x]) for x in regions]

        region_id = input('Выберете регион введя его порядковый номер:\n')
        try:
            if int(region_id) in range(1, 8):
                region_id = regions[int(region_id)]
                break
            else:
                print('Такого региона нет\n')
        except:
            print('Некорректный ввод\n')

    while True:
        cai = input('Артикул товара, например "16777225":\n')
        if not cai.isdigit():
            print('Артикул может быть только целым числом\n')
        else:
            cai = int(cai)
            break

    while True:
        amount = input('Сумма продажи:\n')
        try:
            float(amount)
            break
        except ValueError:
            print('Принимаются только цифры\n')

    sell(cai, region_id, float(amount), file_name)
