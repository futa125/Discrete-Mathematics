import numpy as np


def is_number(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        try:
            float(user_input)
            return True
        except ValueError:
            return False


def is_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def input_number(message):
    user_input = input(message)

    while not is_number(user_input):
        print("Incorrect input")
        user_input = input(message)

    return float(user_input)


def input_int(message):
    user_input = input(message)

    while not is_int(user_input):
        print("Incorrect input")
        user_input = input(message)

    return int(user_input)


def get_data(data_name, data_amount):
    data = []

    for i in range(data_amount):
        data.append(input_number("Enter {}_{}: ".format(data_name, i)))

    return data


def create_equation_array(roots):
    equations = []

    for n in range(len(roots)):
        equations.append([root ** n for root in roots])

    return equations


def solve_equation_array(roots, terms):
    equations = create_equation_array(roots)

    return np.linalg.solve(np.array(equations), np.array(terms))


def find_nth_term_formula(roots, terms, n):
    solution = solve_equation_array(roots, terms)

    term = 0

    for i, j in zip(solution, roots):
        term += i * j ** n

    return term


def find_recurrence_relation(roots):

    # ax^3 + bx^2 + cx + d = 0
    # ax^3 = -(bx^2 + cx + d)
    # x^3 = -(b/a * x^2 + c/a * x + d/a)
    # a_n = -(b/a * a_(n-1) + c/a * a_(n-2) + d/a * a_(n-3))

    # b/a = -(p + q + r)
    # c/a = (p * q) + (q * r) + (r * p)
    # d/a = -(p * q * r)

    # coefficient_1 = 1
    coefficient_2 = -(roots[0] + roots[1] + roots[2])
    coefficient_3 = roots[0]*roots[1] + roots[1]*roots[2] + roots[2]*roots[0]
    coefficient_4 = -(roots[0]*roots[1]*roots[2])

    coefficients = [coefficient_2, coefficient_3, coefficient_4]

    return coefficients


def find_nth_term_recurrence(roots, terms, n):
    coefficients = find_recurrence_relation(roots)

    for i in range(len(terms), int(n) + 1):
        total = 0
        last_term_index = len(terms) - 1

        # -(b/a * a_(n-1) + c/a * a_(n-2) + d/a * a_(n-3))
        for coefficient in coefficients:
            total += coefficient * terms[last_term_index]
            last_term_index -= 1

        terms.append(-total)

    return terms[-1]


def main():
    roots = get_data("x", 3)
    terms = get_data("a", 3)

    n = input_int("Enter the term your want to calculate: ")
    while n <= 2:
        print("n must be larger than 2")
        n = input_int("Enter the term your want to calculate: ")

    print("Formula result: {:0.4f}".format(find_nth_term_formula(roots, terms, n)))
    print("Recurrence result: {:0.4f}".format(find_nth_term_recurrence(roots, terms, n)))


if __name__ == '__main__':
    main()
