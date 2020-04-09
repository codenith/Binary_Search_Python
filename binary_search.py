# Function to implement binary search
def binary_search(list_elements, start, end, item):

    # Check whether the end is larger or equal to the start value
    if end >= start:

        # Find the middle index value to find the middle element in the list
        # This will prevent overflow and also gives value of the middle index
        mid_index_value = start + (end - start) // 2

        # Now we need to  check whether, the middle value ,of the list is the required item or not
        if list_elements[mid_index_value] == item:
            return mid_index_value
        # If the item is smaller than the middle value then no need to check until the end
        elif list_elements[mid_index_value] > item:
            # Here,we use recursion to find out the item in the list
            return binary_search(list_elements, start, mid_index_value-1, item)
        else:
            # the item is present in between the middle value and the end value of the list
            return binary_search(list_elements, mid_index_value+1, end, item)
    else:
        return -1           # Search Unsuccessful, so return -1 to indicate that item was unfound

# main function


def main_function():
    list_elements = []
    number_of_elements = int(
        input("Enter the desired number of elements in the list:  "))
    for index in range(number_of_elements):
        element_value = int(
            input(f"Enter the  desired value of index  {index} :  "))
        list_elements.append(element_value)
    item = int(input("Enter the item to be searched: "))
    list_elements = sorted(list_elements)       #Binary Search will only in a sorted list.
    start_value = list_elements[0]  # value at index 0 stored at start_value
    # value at the last index is stored at the end_value
    end_value = len(list_elements)-1
    # result will obtain the index value of the item ,if search is successful
    result = binary_search(list_elements, start_value, end_value, item)
    if result != -1:  # If search is successful,then
        print(f"Search Succesful\nItem found at the index {result}")
    else:  # If search is unsuccessful,then,the result will obtain -1 as its value
        print("Search Unsuccessful!!\nItem not found")


# calling the main function
main_function()
