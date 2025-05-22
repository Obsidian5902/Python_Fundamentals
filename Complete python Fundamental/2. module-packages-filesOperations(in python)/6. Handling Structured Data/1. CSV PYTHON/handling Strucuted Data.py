import csv
with open("data.csv", "r+") as f:
    mock_data_reader = csv.reader(f)
    line_count = 1
    users = []

    for row in mock_data_reader:
        if line_count>1:
            name = row[0]
            age = row[1]
            PC =row[2]
            City = row[3]
            users.append({"name":row[0], "age":row[1],"PC": row[2], "city":row[3]})
            # break

        line_count += 1
for user in users:
    print(user)