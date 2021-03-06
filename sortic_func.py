from rra_rrb_rrr import *
from ra_rb_rr import *
from additional_function import ft_find_lst, ft_len, ft_min, ft_slice


def sortic(mass_a):
    mass_b = []
    mass_commands = []

    while mass_a:

        # индекс минимального элмента
        minimal_index = ft_find_lst(mass_a, ft_min(mass_a))

        # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
        if ft_min(mass_a) == mass_a[0]:
            mass_commands.append('pb')
            mass_b.append(mass_a[0])
            mass_a = ft_slice(mass_a, 1, ft_len(mass_a))
        else:
            # находим рассстояние от концов
            # списка до концов списка и находим до куда ближе
            if minimal_index >= ft_len(mass_a) - minimal_index - 1:
                mass_a = rra(mass_a)
                mass_commands.append('rra')
            elif minimal_index <= ft_len(mass_a) - minimal_index - 1:
                mass_a = ra(mass_a)
                mass_commands.append('ra')

    return mass_commands
