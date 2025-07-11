import csv


def remove_duplicates_csv(file1, file2, output_file='result_hlushko.csv'):
    data = set()

    for file in [file1, file2]:
        with open(file, newline='', encoding='utf-8') as file_exampl:
            reader = csv.reader(file_exampl)
            for row in reader:
                data.add(tuple(row))

    with open(output_file, 'w', newline='', encoding='utf-8') as file_exampl:
        writer = csv.writer(file_exampl)
        for row in sorted(data):
            writer.writerow(row)


remove_duplicates_csv(
    'dir_csv/random.csv',
    'dir_csv/random-michaels.csv'
)