import sqlite3
from sqlite3 import Error
from PIL import Image
import cv2

print("\nRunning retrieve.py")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

database = "C:/Users/Dell/Desktop/final_proj/Django/myproject/db.sqlite3"
conn = create_connection(database)

with conn:
    cur =  conn.cursor()
    #retrieve patient info
    cur.execute("SELECT * FROM mapp_Patient AS p WHERE p.analysis == 'NODONE'")
    all_info = cur.fetchall()
    cur.execute("UPDATE mapp_Patient SET analysis = 'DONE'")

    #retrieve clinic info
    clinic_id = all_info[0][5]
    #print(clinic_id)
    cur.execute("SELECT * FROM mapp_Clinic AS c WHERE c.cid == "+clinic_id)
    clinic_info = cur.fetchall()

#print(all_info)
#print(clinic_info)

id = all_info[0][0]
gender = all_info[0][1]
c_name = all_info[0][2]
stage = all_info[0][3]
c_type = all_info[0][4]
name = all_info[0][6]+" "+all_info[0][7]
age = all_info[0][8]
patient_email = all_info[0][9]
phone = all_info[0][10]
address = all_info[0][11]+" "+all_info[0][12]
img_name = all_info[0][14]
clinic_mail = clinic_info[0][1]

img = cv2.imread('C:/Users/Dell/Desktop/final_proj/Django/myproject/'+img_name)

print("Successfully Retrieved...")