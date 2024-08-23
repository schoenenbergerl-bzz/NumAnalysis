def calculate_mean(data):
    total = 0
    count = 0

    for num in data:
        total += num
        count += 1

    mean = total / count if count != 0 else 0
    return mean


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n == 0:
        return None

    midpoint = n // 2

    if n % 2 == 1:
        return sorted_data[midpoint]
    else:
        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2


def calculate_mode(data):
    frequency = {}

    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values(), default=0)
    modes = [key for key, value in frequency.items() if value == max_count]

    if len(modes) == len(data):
        return None
    else:
        return modes[0]


def calculate_standard_deviation(data):
    if len(data) == 0:
        return 0

    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)
    standard_deviation = variance ** 0.5

    return standard_deviation


def calculate_variance(data):
    if len(data) == 0:
        return 0

    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)

    return variance


if __name__ == "__main__":
    user_input = input("Bitte geben Sie eine Liste von Zahlen ein, getrennt durch Leerzeichen: ")

    # Die Eingabe in eine Liste von Zahlen umwandeln
    data = list(map(float, user_input.split()))

    print(f"Mittelwert: {calculate_mean(data)}")
    print(f"Median: {calculate_median(data)}")
    print(f"Modus: {calculate_mode(data)}")
    print(f"Standardabweichung: {calculate_standard_deviation(data)}")
    print(f"Varianz: {calculate_variance(data)}")
