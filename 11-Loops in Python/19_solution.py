s = "ramlalarmnababcdcd"
for ch in s:
    print(ch)
    if s.count(ch) == 1:
        print("non-repeatd character:", ch)
        break
        