arr = [31, 41, 59, 26, 41, 58]

def insertion_sort(arr):
    for i in range(1, len(arr)): # i는 1부터 시
        key = arr[i]
        j = i - 1 # 정렬된 부분의 마지막 index
        while j >= 0 and arr[j] > key:
            arr[j + 1]  = arr[j] # 값을 오른쪽으로 이동
            j -= 1
        arr[j + 1] = key

        print(f"step {i}: {arr}")

print("initial arr: ", arr)
insertion_sort(arr)
print("sorted arr: ", arr)