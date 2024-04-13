import json
from pathlib import Path

if __name__ == '__main__':
    texts_path: Path = Path(Path.cwd().parent, "data", "texts.json")
    with open(texts_path.absolute(), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    print(data[12])
