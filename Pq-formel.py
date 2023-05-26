from matplotlib import pyplot as plt

integer = 1
floating_point = 1.0
string = "string"
liste = [1, 2, 3.0, "hallo"]
dictionary = {"key": "value", "key2": 1}

def pqformel(a, b, c):
    p = b / a
    q = c / a
    if q > 0:
        raise ValueError("Q cannot be greater than 0")
    t1 = -p/2
    t2 = ((p/2)**2-q)**(1/2)
    return t1 + t2, t1 - t2

loaded_data = []
with open("daten.csv") as file:
    for line in file.readlines():
        if not line.startswith("#") and line.strip():
            entry_list = []
            for entry in line.strip().split(","):
                entry_list.append(float(entry))
            loaded_data.append(entry_list)

print(loaded_data)


def quadrat(a, b, c, x):
    return a*x**2+b*x+c


for a, b, c in loaded_data:
    try:
        x1, x2 = pqformel(a, b, c)
    except ValueError as e:
        x1, x2 = [None, None]

    x = range(-10, 10)
    y = []
    for entry_x in x:
        y.append(quadrat(a, b, c, entry_x))

    if x1 is not None:
        plt.axvline(x1, color='orange')
    if x2 is not None:
        plt.axvline(x2, color='orange')
    plt.plot(x, y)
    plt.title(f"{a=} {b=} {c=}")
    plt.grid()
    plt.show()
    plt.clf()
