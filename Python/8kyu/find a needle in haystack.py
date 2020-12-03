def find_needle(haystack):
    for index, junk in enumerate(haystack):
        if junk == "needle":
            return "found the needle at position " + str(index)
