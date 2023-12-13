"""
    --- Day 6: Wait For It ---

    Determine the number of ways you could beat the record in each race. What do you get if you multiply these
    numbers together?

"""
import time

debug1 = True

debug2 = True


def get_answer_1():
    data = ['Time:        55     99     97     93', 'Distance:   401   1485   2274   1405']
    times = [int(k) for k in data[0].split(' ') if k.isnumeric()]
    distances = [int(k) for k in data[1].split(' ') if k.isnumeric()]
    races = [[times[i], distances[i]] for i in range(len(times))]
    margin = 1
    for race in races:
        margin *= get_margin(race)

    return margin


def get_margin(race):
    return len([k * (race[0] - k) for k in range(race[0] + 1) if k * (race[0] - k) > race[1]])


def get_answer_2():
    data = ['Time:        55     99     97     93', 'Distance:   401   1485   2274   1405']

    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 06, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 06, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 06, 1 is
    # The Answer to Advent of Code 2023, 06, 2 is


if __name__ == "__main__":
    main()
