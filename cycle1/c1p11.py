print("NIHAD K - SJC22MCA043")
def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
   swapped = False
   for j in range(n - 1 - i):
    if arr[j] > arr[j + 1]:
      arr[j], arr[j + 1] = arr[j + 1], arr[j]
      swapped = True
   if not swapped:
       break
input_str = input("Enter elements : ")
elements = [int(x) for x in input_str.split()]
print("Original List:", elements)
bubble_sort(elements)
print("Sorted List:", elements)