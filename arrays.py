#Array

# ==========================
# Sorting Algorithms
# ==========================   
 
#Bubble Sort
def bubble_sort(arr):
    n = len(arr) #get the length of the array
    for i in range(n): #outer loop - runs n times
        for j in range(0, n-i-1): #inner loop - gets smaller each pass
            if arr[j] > arr[j+1]: #compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j] # swamp if out of order
    return arr

#Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = 1
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

#quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


#O(nlogn)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
    return output

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr


# ==========================
# Searching Algorithms
# ==========================

#Linear Search
#search for a target number in the array one by one
def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


#Search algorithm to find a target value in a sorted array, with each iteration, half the values are eliminated
def binary_search(arr, target):
    left = 0 #initalize left side
    right = len(arr) - 1 #initalize the last element of the array
    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 



# ==========================
# Menus
# ==========================

def sorting_menu(arr):
    print("\n--- Sorting Menu ---")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")
    print("6. Counting Sort")
    print("7. Radix Sort")
    choice = input("Choose sorting algorithm: ")

    if choice == "1":
        print("Bubble Sorted:", bubble_sort(arr[:]))
    elif choice == "2":
        print("Selection Sorted:", selection_sort(arr[:]))
    elif choice == "3":
        print("Insertion Sorted:", insertion_sort(arr[:]))
    elif choice == "4":
        print("Quick Sorted:", quick_sort(arr[:]))
    elif choice == "5":
        print("Merge Sorted:", merge_sort(arr[:]))
    elif choice == "6":
        print("Counting Sorted:", counting_sort(arr[:]))
    elif choice == "7":
        print("Radix Sorted:", radix_sort(arr[:]))
    else:
        print("Invalid choice!")

def searching_menu(arr):
    print("\n--- Searching Menu ---")
    print("1. Linear Search")
    print("2. Binary Search (array must be sorted)")
    choice = input("Choose searching algorithm: ")
    target = int(input("Enter value to search: "))

    if choice == "1":
        result = linear_search(arr, target)
        print("Found at index:" if result != -1 else "Not found", result)
    elif choice == "2":
        sorted_arr = sorted(arr)
        print("Sorted array for binary search:", sorted_arr)
        result = binary_search(sorted_arr, target)
        print("Found at index:" if result != -1 else "Not found", result)
    else:
        print("Invalid choice!")


# ==========================
# Main Menu
# ==========================

def main_menu():
    arr = []  # empty array at start

    while True:
        print("\n=== DSA Project Menu ===")
        print("1. Create Array")
        print("2. Display Array")
        print("3. Sorting Algorithms")
        print("4. Searching Algorithms")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
        elif choice == "2":
            print("Array:", arr)
        elif choice == "3":
            if arr:
                sorting_menu(arr)
            else:
                print("Array is empty! Please create an array first.")
        elif choice == "4":
            if arr:
                searching_menu(arr)
            else:
                print("Array is empty! Please create an array first.")
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main_menu()