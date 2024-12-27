def append_middle(s1, s2):
    print("Original Strings are:", s1, s2)
    min = int(len(s1)/2)
    x = s1[:min:]
    x = x + s2
    x = x + s1[min:]
    print("After appending:", x)
append_middle("abb", "ccc")