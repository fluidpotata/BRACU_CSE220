def flattenList(given_list, output_list):
    if len(given_list)==0:
        return
    elif type(given_list[0])==list:
        flattenList(given_list[0], output_list)
        flattenList(given_list[1:], output_list)
    else:
        output_list.append(given_list[0])
        flattenList(given_list[1:], output_list)
    return output_list


given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flattenList(given_list, []) # Initial empty list is sent for update
print(output_list)
