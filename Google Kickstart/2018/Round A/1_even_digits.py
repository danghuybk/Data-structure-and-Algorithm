def get_next_num(digits, idx):
    if digits[idx] != 9:
        next_digits = digits[:idx] + [digits[idx] + 1] + [0] * (len(digits) - idx - 1)
    else:
        next_digits = digits[:idx] + [0] + [0] * (len(digits) - idx - 1)
        if idx == 0:
            next_digits = [2] + next_digits
        for idx in range(idx - 1, -1, -1):
            if next_digits[idx] != 8:
                next_digits[idx] += 2
                break
            else:
                next_digits[idx] = 0
            if idx == 0:
                next_digits = [2] + next_digits
    output = 0
    for digit in next_digits:
        output = output * 10 + digit
    return output

def get_prev_num(digits, idx):
    output = 0
    prev_digits = digits[:idx] + [digits[idx] - 1] + [8] * (len(digits) - idx - 1)
    for digit in prev_digits:
        output = output * 10 + digit
    return output

def solve(N):
    digits = [int(digit) for digit in N]
    first_odd_idx = -1
    for i, digit in enumerate(digits):
        if digit % 2 == 1:
            first_odd_idx = i
            break
    if first_odd_idx == -1:
        return 0
    next_num = get_next_num(digits, first_odd_idx)
    prev_num = get_prev_num(digits, first_odd_idx)
    return min(next_num - int(N), int(N) - prev_num)

T = int(input())
for test_idx in range (1, T + 1):
    # input
    N = input()

    # processing
    output = solve(N)

    # output 
    print('Case #{}: {}'.format(test_idx, output))
