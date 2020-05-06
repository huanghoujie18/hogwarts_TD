import yaml
def test_yaml():
    y = yaml.load("""
    ... - Hesperiidae
    ... - Papilionidae
    ... - Apatelodidae
    ... - Epiplemidae
    ... """)
    print(y)

def test_set():
    my_set = {2,3,34,33}
    print(dir(my_set))
