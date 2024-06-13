# номер посылки: 115227367
def min_platforms(weights: list[int], limit: int) -> int:
    # Создаем копию списка и сортируем её
    sorted_weights: list[int] = sorted(weights)
    left: int = 0
    right: int = len(sorted_weights) - 1  # Индекс первого и последнего роботов
    platforms: int = 0  # Количество платформ

    while left <= right:
        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1
        right -= 1  # В любом случае один робот отправится на платформу
        platforms += 1

    return platforms


if __name__ == '__main__':
    weights: list[int] = list(map(int, input().split()))  # Ввод весов роботов
    limit: int = int(input())  # Ввод грузоподъемности платформы

    print(min_platforms(weights, limit))
