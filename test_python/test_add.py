def add(i):
    sum = 0
    for n in range(1, i+1): #[1,n+1)
        sum += n
    return sum

def test_add():
    result=add(100)
    print(result)

