def get_user_choice(q_string: str = None,
                    parse_string: bool = False,
                    var_count: int = 0) -> str:
    if parse_string:
        var_count = max([int(i) for i in q_string if i.isdigit()])
    variants = [str(i) for i in range(1, var_count + 1)]
    user_input = input(">> ")
    while user_input not in variants:
        print("Потрібно ", end='')
        print(*variants, sep=' або ', end='!')
        print()
        user_input = input(">> ")
    return user_input
