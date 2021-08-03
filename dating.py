import csv

# with open('ACSST1Y2019.S1201_data_with_overlays_2021-07-24T221503.csv') as dating_data:
# 	c = csv.reader(dating_data, delimiter=',')
# 	i = 0
# 	j = 0
# 	for row in c:
# 		if i == 1:
# 			for column in row:
# 				if 'Now married (except separated)' in column:
# 					print(column)
# 		i += 1
# 		if i == 2:
# 			break

class Row:
	pass



col_married_20_34_male = 'S1201_C02_004E'
col_married_20_34_female = 'S1201_C02_011E'
col_married_35_44_male = 'S1201_C02_005E'
col_married_35_44_female = 'S1201_C02_012E'
col_name = 'NAME'
with open('ACSST1Y2019.S1201_data_with_overlays_2021-07-24T221503.csv') as dating_data:
	c = csv.DictReader(dating_data)
	i = 0
	rows = []
	for row in c:
		i += 1
		# first row is just some metadata so we skip it
		if i == 1:
			continue
		r = Row()
		x = row[col_married_20_34_male]
		if x != 'N':
			unmarried_20_34_male_perc = 1 - float(x)
			unmarried_20_34_female_perc = 1 - float(row[col_married_20_34_female])
			unmarried_35_44_male_perc = 1 - float(row[col_married_35_44_male])
			unmarried_35_44_female_perc = 1 - float(row[col_married_35_44_female])
			n = row[col_name]
			n = n.replace(' city,', ',')
			n = n.replace(' zona urbana,', ',')
			n = n.replace(' metropolitan government (balance),', ',')
			n = n.replace(' CDP,', ',')
			n = n.replace(' metro government (balance),', ',')
			n = n.replace(' urban county,', ',')
			n = n.replace(' city (balance),', ',')
			n = n.replace(' consolidated government (balance),', ',')
			n = n.replace(' municipality,', ',')
			r.name = n
			rows.append(r)

			r.unmarried_woman_per_man_20_34 = unmarried_20_34_female_perc / unmarried_20_34_male_perc
			r.unmarried_woman_per_man_35_44 = unmarried_35_44_female_perc / unmarried_35_44_male_perc
			r.unmarried_woman_20_34_per_man_35_44 = unmarried_20_34_female_perc / unmarried_35_44_male_perc
	# rows_20_34 = sorted(rows, key=lambda row: row.unmarried_woman_per_man_20_34)
	# for row in rows_20_34:
	# 	print(row.name, row.unmarried_woman_per_man_20_34)
	# rows_35_44 = sorted(rows, key=lambda row: row.unmarried_woman_per_man_35_44)
	# for row in rows_35_44:
	# 	print(row.name, row.unmarried_woman_per_man_35_44)
	rows_35_44_to_20_34 = sorted(rows, key=lambda row: row.unmarried_woman_20_34_per_man_35_44)
	for row in rows_35_44_to_20_34:
		print(row.name, row.unmarried_woman_20_34_per_man_35_44)