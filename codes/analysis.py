import telo_predict as t

print("\nRunning analysis.py")

#Accessing all the form input variables 
c_name = t.r.c_name 
c_type = t.r.c_type
stage = t.r.stage
age = int(t.r.age)

#input from model
predicted_length = t.predicted_length

#analysis variables
rad_range = '0'
rad_fract = '0'
rad_dose = '0'
add_treatment = 'NA'
add_suggest = 'NA'
flag = 0
tel_cond = 'NA'

#analysis definations
def blood():
    global rad_range, rad_fract, rad_dose, add_treatment
    if c_type == 'Hodgkin lymphoma':
        if stage == 'Early':
            rad_range = '20 to 30 Gy'
            rad_fract = '10 to 15 times in total'
            rad_dose = '2Gy per time'
        elif stage == 'Advanced':
            rad_range = '30 to 36 Gy'
            rad_fract = '18 to 20 times in total'
            rad_dose = '1.7Gy per time'
            add_treatment = 'Radiation Therapy can be delivered after chemotherapy.'
    elif c_type == 'Non-Hodgkin lymphoma':
        rad_range = '30 to 36 Gy'
        rad_fract = '18 to 20 times in total'
        rad_dose = '1.7Gy per time'
        if stage == 'Early':
            add_treatment = 'Radiation Therapy can be delivered after chemotherapy.'
        if stage == 'Advanced':
            add_treatment = 'Radiation therapy used to treat bulky disease or areas not responding to chemotherapy.'
    elif c_type == 'Multiple lymphoma':
        rad_range = '30 to 36 Gy'
        rad_fract = '18 to 20 times in total'
        rad_dose = '1.7Gy per time'
        add_treatment = 'Radiation therapy used to treat painful bone lesions or to prepare stem cell transplant.'
    else:
        rad_range = 'NA'
        rad_fract = 'NA'
        rad_dose = 'NA'
        add_treatment = 'NA'

def breast():
    global rad_range, rad_fract, rad_dose, add_treatment
    if c_type == 'Non-recurrent':
        rad_range = '50 to 60 Gy'
        rad_fract = '25 to 30 times in total'
        rad_dose = '2Gy per time'
        if stage == 'Advanced':
            add_treatment = 'Radiation Therapy can be delivered after lumpectomy or mastectomy.'
    elif c_type == 'Locally-advanced':
        rad_range = '50 to 60 Gy'
        rad_fract = '25 to 30 times in total'
        rad_dose = '2Gy per time'
        add_treatment = 'Radiation Therapy can be delivered after chemotherapy or surgery.'
    elif c_type == 'Recurrent':
        rad_range = '45 to 50 Gy'
        rad_fract = '25 to 28 times in total'
        rad_dose = '1.8Gy per time'
        add_treatment = 'Radiation is given to the chest wall and lumph nodes.'
    else:
        rad_range = 'NA'
        rad_fract = 'NA'
        rad_dose = 'NA'
        add_treatment = 'NA'
     
def lung():
    global rad_range, rad_fract, rad_dose, add_treatment
    if c_type == 'Non-Small cell':
        if stage == 'Early':
            if age < 70:
                rad_range = '60 to 70 Gy'
                rad_fract = '30 to 35 times in total'
                rad_dose = '2Gy per time'
            else:
                rad_range = '45 to 60 Gy'
                rad_fract = '15 to 25 times in total'
                rad_dose = '2.5Gy per time'
        elif stage == 'Advanced':
            rad_range = '60 to 70 Gy'
            rad_fract = '30 to 35 times in total'
            rad_dose = '2Gy per time'
            add_treatment = 'Radiation Therapy can be combined with chemotherapy or immunotherapy.'
    elif c_type == 'Small cell':
        if stage == 'Early':
            rad_range = '45 to 50 Gy'
            rad_fract = '25 times in total'
            rad_dose = '2Gy per time'
            add_treatment = 'Radiation Therapy can be combined with chemotherapy.'
        elif stage == 'Advanced':
            rad_range = '60 to 70 Gy'
            rad_fract = '30 to 35 times in total'
            rad_dose = '2Gy per time'
            add_treatment = 'Radiation therapy used to relieve symptoms.'
    else:
        rad_range = 'NA'
        rad_fract = 'NA'
        rad_dose = 'NA'

def skin():
    global rad_range, rad_fract, rad_dose, add_treatment
    if c_type == 'Basal cell carcinoma':
        if stage == 'Early':
            if age < 60:
                rad_range = '45 to 50 Gy'
                rad_fract = '22 to 25 times in total'
                rad_dose = '2Gy per time'
            else:
                rad_range = '34 Gy'
                rad_fract = '10 times in total'
                rad_dose = '3.4Gy per time'
        elif stage == 'Advanced':
            if age < 60:
                rad_range = '60 to 70 Gy'
                rad_fract = '30 to 35 times in total'
                rad_dose = '2Gy per time'
            else:
                rad_range = '34 Gy'
                rad_fract = '10 times in total'
                rad_dose = '3.4Gy per time'
    elif c_type == 'Squamous cell carcinoma' or c_type == 'Merkel  cell carcinoma': 
        if stage == 'Early':
            if age < 60:
                rad_range = '50 to 60 Gy'
                rad_fract = '25 to 30 times in total'
                rad_dose = '2Gy per time'
            else:
                rad_range = '40 to 50 Gy'
                rad_fract = '15 to 20 times in total'
                rad_dose = '2.5Gy per time'
        elif stage == 'Advanced':
            if age < 60:
                rad_range = '60 to 70 Gy'
                rad_fract = '30 to 35 times in total'
                rad_dose = '2Gy per time'
            else:
                rad_range = '50 to 60 Gy'
                rad_fract = '25 to 30 times in total'
                rad_dose = '2Gy per time'
    else:
        rad_range = 'NA'
        rad_fract = 'NA'
        rad_dose = 'NA'
    
def prostate():
    global rad_range, rad_fract, rad_dose, add_treatment
    if c_type == 'Non-recurrent':
        if stage == 'Early':
            rad_range = '70 to 78 Gy'
            rad_fract = '28 to 39 times in total'
            rad_dose = '2.5Gy per time'
        elif stage == 'Advanced':
            rad_range = '78 to 80 Gy'
            rad_fract = '39 to 41 times in total'
            rad_dose = '2Gy per time'
            add_treatment = 'Radiation Therapy can be combined with hormone therapy.'
    elif c_type == 'Locally-advanced':
        rad_range = '78 to 80 Gy'
        rad_fract = '39 to 41 times in total'
        rad_dose = '2Gy per time'
        add_treatment = 'Radiation Therapy can be combined with hormone therapy.'
    elif c_type == 'Recurrent':
        rad_range = '64 to 66 Gy'
        rad_fract = '32 to 33 times in total'
        rad_dose = '2Gy per time'
    else:
        rad_range = 'NA'
        rad_fract = 'NA'
        rad_dose = 'NA'
        add_treatment = 'NA'

#suggestions based on telomere length
if age<=20:
    if predicted_length < 12000:
        flag = 1
        add_suggest = 'Healthy diet must be followed and it should include more fresh green vegitables. Patient has to follow basic exercise plans.'
    else:
        add_suggest = 'Maintain healthy life-style.'
elif age>20 and age<=35:
    if predicted_length < 9000:
        flag = 1
        add_suggest = 'Healthy diet must be followed. Patient has to follow basic exercise plans and try to stop consuming of unhealthy beverages such as alcohol, energy and soft drinks (if consuming).'
    elif predicted_length > 12000:
        flag = 2
    else:
        add_suggest = 'Maintain healthy life-style.'
elif age>35 and age<50:
    if predicted_length < 7000:
        flag = 1    
        add_suggest = 'Healthy diet must be followed. Patient has to follow basic exercise plans and try to stop consuming of unhealthy beverages such as alcohol, energy and soft drinks (if consuming). If patient has a practice of smoking he should immediately stop.'
    elif predicted_length > 11000:
        flag = 2
    else:
        add_suggest = 'Maintain healthy life-style.'
elif age>50:
    if predicted_length < 5000:
        flag = 1
        add_suggest = 'Try taking more rest and follow a simple exercise plans (Yoga). Do not consume unhealthy beverages and stop smoking (if smoking). eat healthy foods and maintain good life style.'
    elif predicted_length > 10000:
        flag = 2
    else:
        add_suggest = 'Maintain healthy life-style and practices yoga and exercises.'
    
if flag == 1:
    tel_cond = 'Patient has telomere length of below normal for their age group. To improve it patient must follow the suggestions provided and maintain healthy life-style.'
elif flag == 2:
    add_suggest = 'Please consult the doctor and follow healthy life style.'
    tel_cond = 'Patient has abnormal telomere length for their age group. There is a chance of recurring cancer. Consulting a cancer doctor (oncologists) must be done.'
else:
    tel_cond = 'Patient has normal telomere length for their age group. Keep following healthy life-style.'


def cancer_types(c_name):
    cTypes = {
        'Blood': blood,
        'Breast': breast,
        'Lung': lung,
        'Skin': skin,
        'Prostate': prostate
    }
    return cTypes.get(c_name, lambda: 'Invalid Type')()

cancer_types(c_name)


print("Analysis is completed...")

'''
print(rad_range)
print(rad_fract)
print(rad_dose)
print(add_treatment)
print(tel_cond)
print(add_suggest)
'''