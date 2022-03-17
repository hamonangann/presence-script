
# import pandas
import pandas as pd
import numpy as np

def fill1(r):
    return '1'

def fill0(r):
    return '0'

column_tanggal = input()
   
# read csv data
df1 = pd.read_csv('daftar-mhs_vLive.csv', sep=';')
df2 = pd.read_csv('meetingAttendanceReport.csv', sep=';')
df2 = df2.drop_duplicates(subset=['Nama'], keep='last')


   
Left_join = pd.merge(df1, 
                     df2, 
                     on ='Nama', 
                     how ='left')

Left_join[column_tanggal] = np.where(Left_join['Duration'].isnull(),'0','1')

Left_join.to_csv('res_data.csv', index=False)

