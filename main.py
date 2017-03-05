import csv, sys

emails = []
with open('test.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    with open('output.csv', 'w', newline='') as outfile:
        fieldnames = ('Name', 'From Email Address')
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for row in reader:
            # print(', '.join(row))
            # print(row['From Email Address'])
            row = {k: row[k] for k in ('Name', 'From Email Address')}
            # print(row)
            if row['From Email Address'] not in emails:
                writer.writerow(row)
                emails.append(row['From Email Address'])
