"""transpose of a matrix"""
import numpy
import csv
import pandas
dir_input=r'C:/Users/user/Desktop/input_data.csv'
dir_output=r'C:/Users/user/Desktop/output_data.csv'
df = pandas.read_csv(f'{dir_input}',encoding='UTF-8', header=None) #No index
df = df.values #'numpy.ndarray'      #[1:,1:,]#index
df = df[1:3,1:3]#snip
df = numpy.where(df > 3, 1, -1)#if
df = pandas.DataFrame(df)
df.to_csv(f'{dir_output}',index=False,header=None)


"""transpose of a matrix"""
def matrix_transposed():
    print(__doc__)
    import numpy as np
    import csv
    A=[1,2,3]
    B=[4,5,6]
    C=[7,8,9]
    D=[A,B,C]
    print(D) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    DT= np.array(D).T.tolist()
    print(DT)#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    with open('data.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(DT)