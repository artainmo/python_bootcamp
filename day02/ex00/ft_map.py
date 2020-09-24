def ft_map(function_to_apply, list_of_inputs):
    list_of_outputs = []
    i = 0
    for items in list_of_inputs:
        list_of_outputs.append(function_to_apply(items))
    return list_of_outputs
