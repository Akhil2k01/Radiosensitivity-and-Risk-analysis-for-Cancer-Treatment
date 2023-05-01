import analysis as a
from fpdf import FPDF
from fpdf.enums import XPos, YPos

print("\nRunning end.py")

#Accessing all the required variables
id = a.t.r.id
name = a.t.r.name
age = str(a.age)
patient_email = a.t.r.patient_email
gender = a.t.r.gender
phone = a.t.r.phone
address = a.t.r.address
c_name = a.c_name
c_type = a.c_type
stage = a.stage
rad_range = a.rad_range
rad_fract = a.rad_fract
rad_dose = a.rad_dose
add_treatment = a.add_treatment
add_suggest = a.add_suggest
tel_cond = a.tel_cond


#Creating pdf
class PDF(FPDF):
    def header(self):
        #Border
        self.rect(5, 5, 200, 297-10)
        # Logo
        #self.image('C:/Users/Dell/Desktop/final_proj/augmentation.py', 10, 10, 25)
        # font
        self.set_font('times', 'BI', 20)
        # Padding
        self.cell(160)
        # Title
        self.cell(0, 10, 'RRCT', border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.set_font('times', 'BU', 30)
        self.cell(0, 10, 'Final Report', align='C')
        self.ln(20)
    
    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_xy(-205, -7.5)
        # set font
        self.set_font('times', '', 10)
        self.cell(0, 10, 'RRCT', align='L')
        # Page number
        self.set_font('helvetica', 'I', 9)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')
        

def setup(arg, wd):
    pdf.set_fill_color(200)
    pdf.cell(wd, 10, arg, border=True, fill=True, align='L')

def setvalue(arg, wd):
    pdf.multi_cell(wd, 10, arg, border=True)
    
def sidehead(arg):
    pdf.set_font('times', 'U', 22)
    pdf.cell(0, 10, arg, align='L')
    pdf.ln(12)
    pdf.set_font('times', '', 16)

def setaddvalue(arg, wd):
    pdf.multi_cell(wd, 8, arg, border=True)

# Create a PDF object
pdf = PDF('P', 'mm', 'A4')

pdf.set_title("Report")
pdf.set_author("RRCT Research Team")
pdf.set_creator("RRCT")
pdf.set_producer("RRCT Team")

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 10)

#Add Page
pdf.add_page()

#pdf.set_margin(10)

# specify font

#---------------------------------------------------------Patient Details------------------------------------------------------------
sidehead('Patient Details')

setup(' Patient ID', 35)
y = pdf.get_y()
setvalue(id, 40)
x = pdf.get_x()
pdf.set_xy(x, y)
setup(' Name', 35)
setvalue(name, 0)
pdf.ln(0)

setup(' Age', 20)
y = pdf.get_y()
setvalue(age, 20)
x = pdf.get_x()
pdf.set_xy(x, y)
setup(' Email', 35)
setvalue(patient_email, 0)
pdf.ln(0)

setup(' Gender', 30)
y = pdf.get_y()
setvalue(gender, 40)
x = pdf.get_x()
pdf.set_xy(x, y)
setup(' Phone Number', 50)
setvalue(phone, 0)
pdf.ln(0)

setup('Address', 30)
pdf.ln(10)
setvalue(address, 0)
pdf.ln(2.5)

#---------------------------------------------------------Cancer Details------------------------------------------------------------

sidehead('Cancer Details')

setup(' Cancer Name', 40)
y = pdf.get_y()
setvalue(c_name, 50)
x = pdf.get_x()
pdf.set_xy(x, y)
setup(' Stage', 35)
setvalue(stage, 0)
pdf.ln(0)

setup(' Cancer Type', 40)
setvalue(c_type, 0)
pdf.ln(2.5)

#---------------------------------------------------------Radiation Therapy Details------------------------------------------------------------

sidehead('Radiation Therapy Details')

setup(' Radiation Range', 50)
y = pdf.get_y()
setvalue(rad_range, 50)
x = pdf.get_x()
pdf.set_xy(x, y)
setup(' Doses', 35)
setvalue(rad_dose, 0)
pdf.ln(0)

setup(' Fraction', 80)
setvalue(rad_fract, 0)
pdf.ln(2.5)

#---------------------------------------------------------Extra------------------------------------------------------------

sidehead('Additional Treatments')
setaddvalue(add_treatment, 0)
pdf.ln(2.5)

sidehead('Suggestions')
setaddvalue(add_suggest, 0)
pdf.ln(2.5)

sidehead('Telomere Condition')
setaddvalue(tel_cond, 0)
pdf.ln(2.5)

res='C:/Users/Dell/Desktop/final_proj/results/reports/'+id+'.pdf'
pdf.output(res)


print("Creation of PDF is successful...")