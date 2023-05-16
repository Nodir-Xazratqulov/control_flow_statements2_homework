def main(a):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x = a%10
    y = a//10
    z = y%10
    e = y//10
    b = e%10
    d = e//10
    f = d%10
    g = d//10

    #  x,z,b,f,g ??????

    if x>z and x>b and x>f and x>g:
        return 4
    if z>x and z>b and z>f and z>g:
        return 3
    if b>z and b>x and b>f and b>g:
        return 2
    if f>z and f>b and f>x and f>g:
        return 1
    if g>z and g>b and g>f and g>x:
        return 0

print(main(23475))
