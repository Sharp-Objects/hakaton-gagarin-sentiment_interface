import re
import time

import pandas as pd

start_time = time.time()

df_messages = pd.read_excel('test_data.xlsx')
df_tickers = pd.read_excel('issuers.xlsx')

# Создаем словарь для хранения issuerid для каждой строки сообщения
unique_issuer_ids = {}

# Проход по каждой строке в файле сообщений
for index, row_message in df_messages.iterrows():
    message = row_message['MessageText'].lower()  # Приведение сообщения к нижнему регистру
    unique_issuer_ids[index] = set()

    # Проход по каждому тикеру и названию компании в файле с данными
    for index_data, row_data in df_tickers.iterrows():
        ticker = str(row_data['BGTicker'])  # Приведение тикера к нижнему регистру
        company = str(row_data['EMITENT_FULL_NAME'])  # Приведение названия компании к нижнему регистру
        issuerid = row_data['issuerid']

        # Проверка наличия пустых значений в дополнительных столбцах

        # Поиск названия компании в сообщении
        common_messages = [' ', ',', '.', '"']
        if any((company + symbol) in message for symbol in common_messages):
            if company != 'газпром':
                unique_issuer_ids[index].add(issuerid)
            else:
                if 'газпром нефть' not in message:
                    unique_issuer_ids[index].add(issuerid)
                else:
                    if message.index('газпром нефть') > message.index('газпром'):
                        unique_issuer_ids[index].add(issuerid)
                    else:
                        unique_issuer_ids[index].add(issuerid)
                        unique_issuer_ids[index].discard(48)
        col5 = str(row_data['Unnamed: 5']).lower()
        if any((col5 + symbol) in message for symbol in common_messages):
            unique_issuer_ids[index].add(issuerid)

        col6 = str(row_data['Unnamed: 6']).lower()
        if any((col6 + symbol) in message for symbol in common_messages):
            unique_issuer_ids[index].add(issuerid)

        col7 = str(row_data['Unnamed: 7']).lower()
        if any((col7 + symbol) in message for symbol in common_messages):
            unique_issuer_ids[index].add(issuerid)

        col8 = str(row_data['Unnamed: 8']).lower()
        if any((col8 + symbol) in message for symbol in common_messages):
            unique_issuer_ids[index].add(issuerid)

        if re.search(r'\b{}\b'.format(re.escape(ticker)), message):
            unique_issuer_ids[index].add(issuerid)
            if ticker == 'moex' and 'imoex' in message:
                unique_issuer_ids[index].discard(103)

# Вывод уникальных issuerid для каждой строки сообщения
for index in unique_issuer_ids:
    issuer_ids = unique_issuer_ids[index]
    if issuer_ids:
        message = df_messages.loc[index, 'MessageText']
        issuer_ids_str = [str(id) for id in issuer_ids]  # конвертация в строковый формат
        print(f"Issuer IDs {', '.join(issuer_ids_str)} для сообщения '{message}'")

end_time = time.time()
execution_time = end_time - start_time
print(f"Time taken to execute: {execution_time} seconds")
