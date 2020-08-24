'''複数回入力した値を記録してcsvで出力'''
def list_output_csv(list,folder_name,file_name):
    import csv

    if folder_name=="":
        save_name="{}.csv".format(file_name)
    else:
        save_name = "{0}/{1}.csv".format(folder_name, file_name)
    csv_name = open(save_name, 'w', newline='')
    csvWriter = csv.writer(csv_name)
    csvWriter.writerows(list)
    csv_name.close()

output_val=[]
while(True):
    input_val=input("input words")
    output_val.append([input_val])
    if input_val=="":
        break

list_output_csv(output_val, "", "test")  # input_list, folder_name,file_name
