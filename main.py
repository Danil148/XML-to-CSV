import os
import pandas as pd
        
        

path = input("Введите путь к папке к примеру скрипт лежит в папке main и в ней есть папка content с xml файлами вы должны указать вот так content/ :   ")
col = int(input("В числовом формате укажите сколько будет колонок максимум колнок 6 минимум 3 колонки:   "))    

try:  
    if col == 3:
        df = pd.DataFrame(columns=['col1', 'col2', 'col3'])

        # Перебираем все файлы в папке
        for filename in os.listdir(f'{path}'):
            if filename.endswith('.xml'):
                # Открываем файл и считываем нужные строки
                with open(os.path.join(f'{path}', filename), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    col1 = lines[0].strip()
                    col2 = lines[1].strip()
                    col3 = ''.join(lines[2:]).strip()
                    # Добавляем строки в датафрейм
                    df = pd.concat([df, pd.DataFrame({'col1': [col1], 'col2': [col2], 'col3': [col3]})])
        df.to_csv('article_all.csv', index=False)
        # Сохраняем датафрейм в CSV файл
        with open('article_all.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open('article_all.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines[1:])
    elif col == 4:
        df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4'])

        # Перебираем все файлы в папке
        for filename in os.listdir(f'{path}'):
            if filename.endswith('.xml'):
                # Открываем файл и считываем нужные строки
                with open(os.path.join(f'{path}', filename), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    col1 = lines[0].strip()
                    col2 = lines[1].strip()
                    col3 = lines[2].strip()
                    col4 = ''.join(lines[3:]).strip()
                    
                    # Добавляем строки в датафрейм
                    df = pd.concat([df, pd.DataFrame({'col1': [col1], 'col2': [col2], 'col3': [col3], 'col4': [col4]})])

        # Сохраняем датафрейм в CSV файл
        df.to_csv('article_all.csv', index=False)
        # Сохраняем датафрейм в CSV файл
        with open('article_all.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open('article_all.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines[1:])
    elif col == 5:
        df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4', 'col5'])

        # Перебираем все файлы в папке
        for filename in os.listdir(f'{path}'):
            if filename.endswith('.xml'):
                # Открываем файл и считываем нужные строки
                with open(os.path.join(f'{path}', filename), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    col1 = lines[0].strip()
                    col2 = lines[1].strip()
                    col3 = lines[2].strip()
                    col4 = lines[3].strip()
                    col5 = ''.join(lines[4:]).strip()
                    
                    # Добавляем строки в датафрейм
                    df = pd.concat([df, pd.DataFrame({'col1': [col1], 'col2': [col2], 'col3': [col3], 'col4': [col4], 'col5': [col5]})])

        # Сохраняем датафрейм в CSV файл
        df.to_csv('article_all.csv', index=False)
        # Сохраняем датафрейм в CSV файл
        with open('article_all.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open('article_all.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines[1:])
    elif col == 6:
        df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

        # Перебираем все файлы в папке
        for filename in os.listdir(f'{path}'):
            if filename.endswith('.xml'):
                # Открываем файл и считываем нужные строки
                with open(os.path.join(f'{path}', filename), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    col1 = lines[0].strip()
                    col2 = lines[1].strip()
                    col3 = lines[2].strip()
                    col4 = lines[3].strip()
                    col5 = lines[4].strip()
                    col6 = ''.join(lines[5:]).strip()
                    
                    # Добавляем строки в датафрейм
                    df = pd.concat([df, pd.DataFrame({'col1': [col1], 'col2': [col2], 'col3': [col3], 'col4': [col4], 'col5': [col5], 'col6': [col6]})])

            # Сохраняем датафрейм в CSV файл
        df.to_csv('article_all.csv', index=False)
        # Сохраняем датафрейм в CSV файл
        with open('article_all.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open('article_all.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines[1:])

    elif col < 3 or col > 6:
        print("Не допустимое количевство колонок")
 
except FileNotFoundError:
    print("Не найден путь")    

input("Чтобы выйти из скрипта нажмите Enter")
