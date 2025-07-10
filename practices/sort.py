def sortlist(filename):
    try:
        with open(filename, 'r') as file:
            unsorted_list = [int(line.strip()) for line in file if line.strip() != '']
    except Exception as e:
        print(f"Failed to read file '{filename}': {e}")
        return
    
    length = len(unsorted_list)
    sorted_list = []


    for x in range(length):
        new_len = len(unsorted_list)
        min = 999999999
        ind = -1
        for i in range(new_len):
            if unsorted_list[i] < min:
                min = unsorted_list[i]
                ind = i

        sorted_list.append(unsorted_list[ind])
        unsorted_list.remove(min)

    return sorted_list



if __name__ == '__main__':
    print(sortlist('practices/list.txt'))