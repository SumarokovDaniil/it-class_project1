from additional_function import ft_len


def sa(mass_a):
    if ft_len(mass_a) > 1:
        mass_a[0], mass_a[1] = mass_a[1], mass_a[0]
        return mass_a


def sb(mass_b):
    if ft_len(mass_b) > 1:
        mass_b[0], mass_b[1] = mass_b[1], mass_b[0]
        return mass_b


def ss(mass_a, mass_b):
    return sa(mass_a), sb(mass_b)