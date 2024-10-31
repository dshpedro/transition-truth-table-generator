def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def generate_transitions(arcs):
    """
    This function will take each arc and generate 3 lines
    to make the arc transition from Low -> High -> Low
    you can modify the order by simply re-ordering the lines
    on the code below
    """
    transitions = []

    for arc in arcs:
        low = "".join(char if char.isdigit() else "0" for char in arc)
        transitions.append(low)
        
        high = "".join(char if char.isdigit() else "1" for char in arc)
        transitions.append(high)
        
        low = "".join(char if char.isdigit() else "0" for char in arc)
        transitions.append(low)

    return transitions

def assign_transition_result(transitions, truth_table_map):
    transition_truth_table = []
    for trans_row in transitions:
        row_result = truth_table_map.get(trans_row, "Unknown")
        transition_truth_table.append(trans_row + row_result)

    return transition_truth_table 

def create_truth_table_map(truth_table):
    """
    This function creates a look up table with a dictionary
    the inputs of the truth table are the key, 
    the result from each input is going to the the correspondant value
    """
    truth_table_map = {}
    for row in truth_table:
        input = row[:-1] # everything apart from the last digit
        output = row[-1] # the last digit
        truth_table_map[input] = output
    return truth_table_map


def main():
    arcs = read_file('transition_arcs.txt')
    transitions = generate_transitions(arcs)
    
    truth_table = read_file('truth_table.txt')
    truth_table_map = create_truth_table_map(truth_table)
    
    transition_truth_table = assign_transition_result(transitions, truth_table_map)
    write_file('output.txt', transition_truth_table)

if __name__ == "__main__":
    main()
