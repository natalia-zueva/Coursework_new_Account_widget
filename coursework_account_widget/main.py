from utils import load_data, sorted_by_state, sorted_by_date, format_data

PATH_TO_OPERATIONS = 'operations.json'

def main():

    operations_data = load_data(PATH_TO_OPERATIONS)
    operations_executed = sorted_by_state(operations_data)
    sorted_list = sorted_by_date(operations_executed)
    result_data = format_data(sorted_list)
    for operation in result_data:
        print(operation)

main()
