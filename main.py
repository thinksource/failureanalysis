from FailureCount import FailureCollection

if __name__ == '__main__':
    filename = "log-data.json"
    example = FailureCollection(filename)
    print("There are {} errors".format(example.get_error_count()))
    print("Details:")
    example.print_error_detail()