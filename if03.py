def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a<c or a<b and a>c:
        return a
    if b>a and b<c or b<a and b>c:
        return b
    if c>b and c<a or c<b and c>a:
        return c
    
print(main(7,5,3))