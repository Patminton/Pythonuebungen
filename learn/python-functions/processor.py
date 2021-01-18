def process_numbers(unprocessed_list):
    numbers=[]
    if not isinstance(unprocessed_list, list):
        return numbers
    
    for item in unprocessed_list:
        if isinstance(item, int):
            numbers.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                numbers.append(int(item))
    number = numbers.sort()
    return(numbers)

def process_names(unprocessed_list):
    names=[]
    
    if not isinstance(unprocessed_list, list):
        return names

    for item in unprocessed_list:
        if isinstance(item, str):
            if not item.isnumeric():
                names.append(item)
    names.sort()
    return(names)