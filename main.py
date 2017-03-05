import csv, sys

emails = []
with open('Master_DHR_03_03_2017.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    with open('output.csv', 'w', newline='') as outfile:
        fieldnames = ('Name', 'From Email Address')
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for row in reader:
            row = {k: row[k] for k in ('Name', 'From Email Address')}
            if row['From Email Address'] not in emails:
                writer.writerow(row)
                emails.append(row['From Email Address']
    outfile.close()
csvfile.close()
