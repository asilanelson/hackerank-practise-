#There is a collection of input strings and a collection of query strings. 
#For each query string, determine how many times it occurs in the list of input strings. 
#Return an array of the results
    #example
#strings_list = ['ab', 'ab', 'abc']
#queries = ['ab', 'abc', 'bc']
# ab = 2, abc = 1, bc = 0
def matchingstrings(string_list, queries):
    results = []
    for query in queries:
        count = 0

        for string in string_list:
            if query == string:
               count += 1
        results.append(count)
    return results
        
string_list = ['ab', 'ab', 'a''abc']
queries = ['ab', 'abc', 'a;;''bc']
output = matchingstrings(string_list, queries)
print(output)
            
        