import random

# mas = random.sample(range(20), 20)
mas = [1, 5, 7, 8, 4, 5, 8,9]
# mas = [1]
bufmas = []

print("Excisting array: ")


def merge_sort(mas, bufmas, left, right):
    mid = left + (right - left) // 2
    if left == mid:
        bufmas.append(mas[left])
        return bufmas;
    leftcur = left
    rightcur = mid
    leftA = merge_sort(mas, bufmas, left, mid)
    rightA = merge_sort(mas, bufmas, mid, right)

    while leftcur < mid and rightcur < right:
        if mas[leftcur] > mas[rightcur]:
            bufmas.append(mas[rightcur])
            rightcur += 1
        else:
            bufmas.append(mas[leftcur])
            leftcur += 1
    while leftcur < mid:
        bufmas.append([leftcur])
        leftcur += 1
    while rightcur < right:
        bufmas.append(mas[rightcur])
        rightcur += 1
    return bufmas


merge_sort(mas, bufmas, 0, len(mas))
