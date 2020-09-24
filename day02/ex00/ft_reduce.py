def ft_reduce(function_to_apply, list_of_inputs):
    ret = None
    i = 0
    ret = list_of_inputs[i]
    while i + 1 < len(list_of_inputs):
        ret = function_to_apply(ret, list_of_inputs[i + 1])
        i += 1
    return ret
