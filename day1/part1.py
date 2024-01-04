filename = "input.txt"

def collect_num(str):
    num_list = list(filter(lambda ch: ch.isdigit(), [*str]))
    if len(num_list) > 0:
        return int(num_list[0] + num_list[-1])
    else:
        return 0


def main():
    numbers = []
    with open(filename) as file:
        input_lines = file.read().splitlines()

    numbers = sum(list(map(collect_num, input_lines)))
    print(numbers)

if __name__ == "__main__":
    main()