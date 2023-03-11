operation = lambda x, y: x * y
def print_operation_table(function, num_rows, num_columns):
    for i in range(1,num_columns + 1):
        for j in range(1,num_rows + 1):
            print(function(i,j), end= " ")
        print()
print_operation_table(operation, num_rows=6, num_columns=6)