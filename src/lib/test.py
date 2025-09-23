def run(function, *args):
    *data, expected_result = args
    try:
        result = function(*data)
    except Exception as err:
        if (
            isinstance(expected_result, type) and
            issubclass(expected_result, Exception) and
            isinstance(err, expected_result)):
            print(f'[GOOD] {function.__name__}{data} -> {err}')
        else:
            print(f'[FAIL] {function.__name__}{data} -> {err}, expected {expected_result}')
            raise
    else:
        if result == expected_result:
            print(f'[GOOD] {function.__name__}{data} -> {result}')
        else:
            print(f'[FAIL] {function.__name__}{data} -> {result}, expected {expected_result}')
