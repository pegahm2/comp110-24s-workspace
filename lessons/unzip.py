"""Splitting a dictionary into two lists.""" 

__author__ = "730553436" 


def get_keys(inputs: dict[str,]) -> list[str]:
    """List all of they keys."""
    input_list = []
    for key in inputs:
        # return keys in dictionary 
        input_list.append(key)
    return (input_list) 


def get_values(inputs: dict[str, int]) -> list[int]:
    """List all of the values."""
    inputs_list = []
    for key in inputs:
        # return values in dictionary 
        inputs_list.append(inputs[key])
    return (inputs_list) 


    
    
