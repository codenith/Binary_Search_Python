# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  

list_elements = []
number_of_elements = int(
        input("Enter the desired number of elements in the list:  "))
for index in range(number_of_elements):
        element_value = int(
            input(f"Enter the  desired value of index  {index} :  "))
        list_elements.append(element_value)
list_elements = sorted(list_elements)
item = int(input("Enter the item:"))
result = binary_search(list_elements, 0, len(list_elements)-1, item) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
