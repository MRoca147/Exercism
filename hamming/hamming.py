def distance(strand_a, strand_b):
    try:
        if len(strand_a) != len(strand_b):
            int("string")
    except ValueError:
        raise ValueError("ValueError exception thrown")
    count = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            count += 1
    return count
