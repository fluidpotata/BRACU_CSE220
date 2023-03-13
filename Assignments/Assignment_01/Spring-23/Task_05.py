# Test 05: Remove an element from an array
def remove(source, idx):

    for i in range(idx, len(source) - 1):
        source[i] = source[i + 1]
    source[len(source) - 1] = 0

    return source