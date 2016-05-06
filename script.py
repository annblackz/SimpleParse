import csv

with open('GJB2.markers.tsv', 'r') as file:
	with open('results.tsv', 'w') as out:
		writer = csv.writer(out, delimiter="\t")
		reader = csv.reader(file, delimiter="\t")
		results = []
		headers = reader.next()
		results.append(headers)
		for row in reader:
			try:
				if (float(row[4]) > 0.01):
					results.append(row)
			except:
				# skip the header
				continue
		writer.writerows(results)
