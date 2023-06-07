def matching_strings(string_list, queries):
    results = []
    for query in queries:
        count = 0
        for string in string_list:
            if query == string:
                count += 1
        results.append(count)
    return results

strings_list = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
output = matching_strings(strings_list, queries)
print(output)
