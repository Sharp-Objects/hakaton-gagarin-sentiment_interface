from typing import List


def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    @param y_true: Список с истинными значениями классификации.
    @param y_pred: Список с предсказанными значениями классификации.
    @return: Значение точности прогноза.
    """
    correct: int = sum(y_t == y_p for y_t, y_p in zip(y_true, y_pred))
    return correct / len(y_true) if y_true else 0


def macro_f1_score(
        y_true: List[int], y_pred: List[int], n_classes: int
) -> float:
    """
    @param y_true: Список с истинными значениями классификации.
    @param y_pred: Список с предсказанными значениями классификации.
    @param n_classes: Количество классов.
    @return: Значение макросредней F-меры.
    """
    tp: list[int] = [0] * n_classes
    fp: list[int] = [0] * n_classes
    fn: list[int] = [0] * n_classes

    for y_t, y_p in zip(y_true, y_pred):
        if y_t == y_p:
            tp[y_t] += 1
        else:
            fp[y_p] += 1
            fn[y_t] += 1

    scores: list = []
    for i in range(n_classes):
        if tp[i] + fp[i] == 0 or tp[i] + fn[i] == 0:
            continue
        precision = tp[i] / (tp[i] + fp[i])
        recall = tp[i] / (tp[i] + fn[i])
        if precision + recall == 0:
            continue
        f1 = 2 * precision * recall / (precision + recall)
        scores.append(f1)

    return sum(scores) / len(scores) if scores else 0


def team_score(y_true: List[int], y_pred: List[int], n_classes: int) -> float:
    """
    @param y_true: Список с истинными значениями классификации.
    @param y_pred: Список с предсказанными значениями классификации.
    @param n_classes: Количество классов.
    @return: Значение общего показателя (Team Score).
    """
    accuracy: float = accuracy_score(y_true, y_pred)
    f1_score: float = macro_f1_score(y_true, y_pred, n_classes)

    return 100 * ((0.5 * f1_score) + (0.5 * accuracy))
