import csv
import random
import time
import shutil
import datetime



t_end = time.time() + 30 * 1
while time.time() < t_end:
    time.sleep(10)

    now = datetime.datetime.now() 
    timestamp = str(now.strftime("%Y_%m_%d_%H_%M_%S"))
    csv_file_path = 'sales_data.csv'

    with open(csv_file_path, newline='') as csvfile:
        salesreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in salesreader:
            print(', '.join(row))

    src = "/Users/splank/VS/sales_data.csv"
    dest = "/Users/splank/VS/sales_data_backup"+timestamp 
    shutil.copy(src, dest)

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)

    for row in data_list:
        print(row)

    random.shuffle(data_list)
 
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in data_list:
            csv_writer.writerow(row)
    