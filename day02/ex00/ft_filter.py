def ft_filter(function_to_apply, list_of_inputs):
    list_of_outputs = []
    i = 0
    for items in list_of_inputs:
        if function_to_apply(items) == True:
            list_of_outputs.append(items)
    return list_of_outputs
