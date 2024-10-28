import inflect


p = inflect.engine()


names = []


try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

new_names = p.join(names)

print(f"Adieu, adieu, to {new_names}")

