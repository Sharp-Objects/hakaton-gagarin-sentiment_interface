import re
from pathlib import Path
from typing import Dict, Set

import pandas as pd

data_path: Path = Path(Path.cwd().parent, 'data', 'test_data.xlsx')
df_messages = pd.read_excel(data_path.absolute())
issuers_path: Path = Path(Path.cwd().parent, 'data', 'issuers.xlsx')
df_tickers = pd.read_excel(issuers_path.absolute())

# Creating a dictionary to store issuerid for each message row
unique_issuer_ids: Dict[int, Set[int]] = {i: set() for i in df_messages.index}

# Converting all messages to lower case for efficient comparison
df_messages['MessageText'] = df_messages['MessageText'].str.lower()

# Converting to string and lower case for efficient comparison
df_tickers[
    [
        'BGTicker',
        'EMITENT_FULL_NAME',
        'Unnamed: 5',
        'Unnamed: 6',
        'Unnamed: 7',
        'Unnamed: 8'
    ]
] = df_tickers[
    [
        'BGTicker',
        'EMITENT_FULL_NAME',
        'Unnamed: 5',
        'Unnamed: 6',
        'Unnamed: 7',
        'Unnamed: 8'
    ]
].apply(lambda x: x.astype(str).str.lower())

common_messages = [' ', ',', '.', '"']

# Unpacking the dataframe to series for more efficient computation
issuer_ids = df_tickers['issuerid']
tickers = df_tickers['BGTicker']
companies = df_tickers['EMITENT_FULL_NAME']
unnamed_cols = [df_tickers[f'Unnamed: {i}'] for i in range(5, 9)]

for message_index, message in df_messages['MessageText'].items():
    assert isinstance(message_index, int)
    for ticker, company, issuerid, *unnamed_cols_values in (
            zip(tickers, companies, issuer_ids, *unnamed_cols)
    ):
        if any(
                (company + symbol) in message for symbol in common_messages
        ) and company != 'газпром':
            if (
                    'газпром нефть' in message
                    and message.index('газпром нефть')
                    > message.index('газпром')
            ):
                unique_issuer_ids[message_index].add(issuerid)
            unique_issuer_ids[message_index].add(issuerid)
        if 'газпром' in company:
            unique_issuer_ids[message_index].discard(48)
        if (
                any((col + symbol) in message
                    for symbol in common_messages
                    for col in unnamed_cols_values)
        ):
            unique_issuer_ids[message_index].add(issuerid)
        if re.search(r'\b{}\b'.format(re.escape(ticker)), message):
            unique_issuer_ids[message_index].add(issuerid)
        if ticker == 'moex' and 'imoex' in message:
            unique_issuer_ids[message_index].discard(103)

result = []

for index, issuer_ids in unique_issuer_ids.items():  # type: ignore
    if issuer_ids:
        message = df_messages.loc[index, 'MessageText']
        result.append([list(issuer_ids), message])

print(result[3])
