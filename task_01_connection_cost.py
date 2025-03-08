import heapq

def min_connection_cost(cables):
    if not cables:
        return 0

    heapq.heapify(cables)  # Перетворюємо список у мінімальну купу
    total_cost = 0

    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second  # Вартість їх з'єднання
        total_cost += cost  # Додаємо до загальних витрат
        print(f"З'єднуємо кабелі {first} та {second} за ціною {cost}. Всього: {total_cost}")

        heapq.heappush(cables, cost)  # Додаємо новий об'єднаний кабель назад у купу

    return total_cost

# Приклад використання
cables = [15, 2, 5, 1, 10]
print("Мінімальні витрати на з'єднання:", min_connection_cost(cables))
