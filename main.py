import csv
import os
import datetime
from openpyxl import Workbook

input_file="Input/sales.csv"
output_folder="Output"
logs_file="Logs/errors.txt"


def log_error(error_file,row,error):
    time_stamp=datetime.datetime.now().strftime("%Y/%m/%d,%H:%M:%S")
    error_file.write(f"{time_stamp} | Invalid Row: {row} | error: {error}\n")

def data_processing(input_file,log_file):
    sales={}

    with open(log_file,"a") as error_file:
        with open(input_file,"r") as file:
            reader=csv.reader(file)
            next(reader)

            for row in reader:
                try:
                    product=row[2].strip()
                    quantity=int(row[8].strip())
                    price=float(row[9].strip())

                    total=quantity*price

                    if product in sales:
                        sales[product]+=total

                    else:
                        sales[product]=total
                except(ValueError,IndexError) as e:
                    log_error(error_file,row,str(e))
                    continue
    return sales

def generate_report(sales,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    report_name=f"report_{datetime.date.today()}.txt"
    report_path=os.path.join(output_folder,report_name)

    with open(report_path,"w") as report:
        report.write("---Summary of sales---\n")
        report.write(f"Date: {datetime.date.today()}\n")

        for product, total in sales.items():
            report.write(f"product: {product} | Total sales: {total:.2f}\n")
    print("Report Generated successfully!")

def excel_report(sales,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    report_name="Summary Report.xlsx"
    report_path=os.path.join(output_folder,report_name)

    wb = Workbook()
    sheet=wb.active
    sheet.title="Sales Summary"
    sheet.append(["product","Total sales"])
    for product, total in sales.items():
        sheet.append([product,total])
    
    wb.save(report_path)
    


def main():
    sales_data=data_processing(input_file,logs_file)
    generate_report(sales_data,output_folder)
    excel_report(sales_data,output_folder)

if __name__ == "__main__":
    main()