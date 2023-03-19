# python3 Ralfs Dusa


import os


def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def sift_down(data, i, swaps):
    size = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2 
    if left_child < size and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < size and data[right_child] < data[min_index]:
        min_index = right_child
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def main():       
    text = input("Enter 'I' for input or 'F' for file input: ")
    if "I" in text:
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by space: ").split()))
        assert len(data) == n

    elif "F" in text:
        file_name = input("Enter the file name: ")
        path = './tests/'    
        file_path = os.path.join(path, file_name)           
        with open(file_path, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
                  

if __name__ == "__main__":
    main()

