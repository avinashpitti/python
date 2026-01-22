import csv
with open('emp.csv', 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row[1])
        print(row[2])

# Moving data frp, source(emp.csv) to destination(data.csv) file

import csv

with open('emp.csv', 'r') as src_file:
    reader = csv.reader(src_file)

    with open('data.csv', 'w', newline='') as dest_file:
        writer = csv.writer(dest_file)

        for row in reader:
            writer.writerow(row)

print("Data successfully moved from emp.csv to data.csv")


# new csv file user.csv created
import csv 
employees=[
            (101,'rahul','Male'),
            (102,'Sonia','Female'),
            (103,'Priya','Female')
           ]
fp=open('user.csv','w',newline="")

csv_writer=csv.writer(fp)
csv_writer.writerow(['uid','uname','gender'])#csv header
csv_writer.writerows(employees)              #csv data
# print(csv_writer)

print('New CSV File Created successfully')

fp.close()

# write a python script to read employee.csv and write male users into
# male.csv  female users into female.csv

import csv

# open source file
with open('employee.csv', 'r', newline='') as src:
    reader = csv.DictReader(src)

    # open destination files
    with open('male.csv', 'w', newline='') as male_file, \
         open('female.csv', 'w', newline='') as female_file:

        fieldnames = reader.fieldnames

        male_writer = csv.DictWriter(male_file, fieldnames=fieldnames)
        female_writer = csv.DictWriter(female_file, fieldnames=fieldnames)

        # write headers
        male_writer.writeheader()
        female_writer.writeheader()

        # process rows
        for row in reader:
            gender = row['gender'].lower()

            if gender == 'male':
                male_writer.writerow(row)
            elif gender == 'female':
                female_writer.writerow(row)
