def convert_input(input_data):
    result_dict = {}
    for state, transitions in input_data.items():
        state_dict = {}
        for symbol, next_states in transitions.items():
            symbol_dict = {}
            for next_state, stack_operations in next_states.items():
                symbol_dict[next_state] = stack_operations
            state_dict[symbol] = symbol_dict
        result_dict[state] = state_dict
    return result_dict


input_data = "{
    "q0": {
        "": {
            "Z": {("qf", "")},
            "B": {("q1", ("B"))},
        },
        "a": {
            "Z": {("q0", ("A", "Z"))},
            "B": {("q0", ("A", "B"))},
        },
        "b": {
            "A": {("q0", ("B", "A"))},
        },
    },
    "q1": {
        "": {
            "Z": {("qf", "")},
        },
        "a": {
            "A": {("q1", "")},
            "B": {("q1", "")},
        },
    },
}

converted_dict = convert_input(input_data)
print(converted_dict)
print(type(converted_dict))
