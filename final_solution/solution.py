import pickle
import typing as tp
from pathlib import Path

EntityScoreType = tp.Tuple[int, float]  # (entity_id, entity_score)
MessageResultType = tp.List[EntityScoreType]


def get_issuerid(string: str, data_dict: dict) -> int:
    """
    Ищет соответствие 'titles' в строке и возвращает 'issuerid'

    :param string: Строка, в которой ищем соответствие
    :param data_dict: Подготовленный словарь данных с 'titles' и 'issuerid'
    :return: 'issuerid', если найдено соответствие, в противном случае `-1`
    """
    return next(
        (record['issuerid'] for record in data_dict
         if any(title in string for title in record['titles'])
         ), -1)


def score_texts(
        messages: tp.Iterable[str], *args, **kwargs
) -> tp.Iterable[MessageResultType]:
    """
    Main function (see tests for more clarifications)
    Args:
        messages (tp.Iterable[str]):
         any iterable of strings (utf-8 encoded text messages)

    Returns:
        tp.Iterable[tp.Tuple[int, float]]:
         for any messages returns MessageResultType object
    -------
    Clarifications:
    # all messages are shorter than 2048 characters
    >>> assert all([len(m) < 10 ** 11 for m in messages])
    """

    messages = list(messages) \
        if hasattr(messages, "__iter__") else [messages]  # type: ignore

    if not messages:
        return []

    if len(messages) == 1 and messages[0] == "":
        return [[tuple()]]  # type: ignore

    issuer_path: Path = Path(Path.cwd(), "data", "issuer.pickle")
    with open(issuer_path.absolute(), 'rb') as f:
        issuer_pickle = pickle.load(f)

    VALUE = 3.0  # TODO: fix me

    scores: list = []

    print(issuer_pickle[108])

    for message in messages:
        message = message.lower()
        result = get_issuerid(message, issuer_pickle)
        print(f"DEBUG | {message}")
        scores.append([(result, VALUE)])

    return scores
