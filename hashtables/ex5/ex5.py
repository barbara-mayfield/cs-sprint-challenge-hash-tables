# Your code here

# U P E R

# U - Understand
# Input:
# We are given:
#   - list of full paths to files
#   - list of filenames to query
# Output:
# We need to return:
#   - List of strings of full paths that match the filename.

# Plan
# Dict for file names
# List of results
# For the path in our files
# We will want to split the path at it's /'s
# Set file_name to the end of the split path
# If the file name isn't in the dict,
# Set the default file name to the file name and path
# Otherwise, append the path to the file name's index.

# As for queries append the path if the query is in the dict

# Execute


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_names = {}
    result = []

    for path in files:
        split_path = path.split("/")
        file_name = split_path[-1]
        if file_name not in file_names:
            file_names.setdefault(file_name, [path])
        else:
            file_names[file_name].append(path)

    for query in queries:
        if query in file_names:
            for path in file_names[query]:
                result.append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))


# Reflect
