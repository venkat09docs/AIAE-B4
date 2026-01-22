# READING CSV FILES IN PYTHON

import csv

with open('./modal_logs1.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header row
    print(f'Header: {header}')

    # for row in csv_reader:
    #     # print(row[1])
    #     pass

    # find the day where the tokens are used max

    day_wise_tokens = {row[0]: int(row[3]) for row in csv_reader}
    print(day_wise_tokens)

    max_tokens_day = max(day_wise_tokens, key=day_wise_tokens.get)
    print(f'Day with maximum tokens used: {max_tokens_day} with {day_wise_tokens[max_tokens_day]} tokens')

# WRITING TO A CSV FILE IN PYTHON

with open('./modal_logs_summary.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)

    # Writing the header
    csv_writer.writerow(['Day', 'Tokens Used'])

    # Writing data
    for day, tokens in day_wise_tokens.items():
        csv_writer.writerow([day, tokens])

with open('model_performance.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile)

    write.writerow(['Model', 'Accuracy', 'Response Time (ms)', 'Tokens'])

    # write.writerow(['gpt-3.5-turbo', 0.92, 150, 1200])
    # write.writerow(['gpt-4', 0.96, 300, 2500])
    # write.writerow(['gpt-4-turbo', 0.94, 200, 1800])

    models = [
        ['gpt-3.5-turbo', 0.92, 150, 1200],
        ['gpt-4', 0.96, 300, 2500],
        ['gpt-4-turbo', 0.94, 200, 1800]
    ]

    write.writerows(models)




