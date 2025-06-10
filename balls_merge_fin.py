class Node(object):
    counter: int
    color: int
    next: object

    def __init__(self, color, counter, next=None):
        self.color = color
        self.counter = counter
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, color):
        new_node = Node(color, 1, self.top)
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        old_top = self.top
        self.top = self.top.next
        return old_top

    def is_empty(self):
        return not self.top


def main():
    global colors, n
    print("Программа подсчета уничтоженных шариков")
    print("Введите количество шариков и их цвета (через пробел): ")
    while True:
        try:
            input_str = input().strip()
            if not input_str:
                print("Ошибка: пустой ввод. Попробуйте снова.")
                continue

            parts = list(map(int, input_str.split()))
            if len(parts) < 1:
                print("Ошибка: не указано количество шариков. Попробуйте снова.")
                continue

            n = parts[0]
            if n < 0:
                print("Ошибка: количество шариков не может быть отрицательным. Попробуйте снова.")
                continue

            if len(parts) - 1 != n:
                print(f"Ошибка: указано {n} шариков, но введено {len(parts) - 1} цветов. Попробуйте снова.")
                continue

            colors = parts[1:]
            if any(color < 0 or color > 9 for color in colors):
                print("Ошибка: цвета должны быть цифрами от 0 до 9. Попробуйте снова.")
                continue

            break

        except ValueError:
            print("Ошибка: ввод должен содержать только целые числа. Попробуйте снова.")

    destroyed = 0
    stack = Stack()
    stack.push(colors[0])

    for i in range(1, n):
        if stack.top.color == colors[i]:
            stack.top.counter += 1
            continue
        else:
            if stack.top.counter >= 3:
                destroyed += stack.top.counter
                stack.pop()
                if stack.top.color == colors[i]:
                    stack.top.counter += 1
                    continue
            stack.push(colors[i])
    if stack.top.counter >= 3:
        destroyed += stack.top.counter
    print(f'Шариков уничтожено: {destroyed}')


if __name__ == "__main__":
    main()
