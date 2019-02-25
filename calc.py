def inp_ut(x):
    while True:
        try:
            text = '{}'.format(x)
            a = float(input(text))
            return a
        except ValueError:
            print("Please enter only numbers")


unit_hp = inp_ut("Units hp: \n")  # stands for units hp
unit_quantity = inp_ut("Units quantity: \n")  # stands for units quantity
pit_lords_quantity = inp_ut("pit lords quantity: \n")  # stands for pit lords quantity


def formula(unit_hp, unit_quantity, pit_lords_quantity):
    pl_can: int = pit_lords_quantity * 50 // 35
    stack_max: int = int(unit_hp) * int(unit_quantity) // 35
    if pl_can <= stack_max:
        return pl_can
    else:
        return stack_max


print(
    'The quantity of summoned demons is: \n{0}'.format(str(formula(unit_hp, unit_quantity, pit_lords_quantity)))
)
