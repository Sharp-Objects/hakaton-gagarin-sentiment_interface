import json
from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    example_path: Path = Path(Path.cwd().parent, "data", "example.xlsx")
    df = pd.read_excel(example_path.absolute())

    messages = df['MessageText'].tolist()

    texts_path: Path = Path(Path.cwd().parent, "data", "texts.json")
    with open(texts_path.absolute(), 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    with open(texts_path.absolute(), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
