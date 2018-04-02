from IPython import get_ipython
get_ipython().magic('reset -sf')
from fpdf import FPDF
pdf=FPDF(format='letter',unit='in')

global epw , width, height
width = pdf.w
height = pdf.h
epw = pdf.w - 2*pdf.l_margin

#New Page With Boarder
def newpg():
    pdf.add_page()
    pdf.set_margins(0.75, 1, 0.5)

    pdf.set_font('times','I',18)
    pdf.text(1,0.85, "{}'s Health Report".format(Name))
    pdf.set_font('times','UI',12)
    pdf.text(1,height-0.7, "Doctor's Comment:-")
#    pdf.line(1,height-0.7,2,height-0.7)
#    pdf.line(1,height-0.5,2,height-0.5)
#    pdf.line(1,height-0.5,2,height-0.5)
#    pdf.multi_cell(0,0, "{}'s Health Report".format(Name))
#    pdf.multi_cell(0,9, "Doctor's comment".format(Name))
    pdf.image(logo, x= 6.2 , y=0.3, w=2 , h= 0.5)

#    pdf.rect(0.75,1,width-1,height-2)        # (pdf.rect(left,top,right,bottom))
    pdf.set_font('times','',14)

# Variables
Name = "Shreesha"
Age = "24"
Sex = "Male"
Height = "169"
Weight = "65"
Date = " "
BMI_CValue = "2000 "
BMI_PValue = "51351"
BW_CValue = "546516"
BW_PValue = "6454665"
#Lean_Mass_RValue =" "

#Images
logo = "MetFlux_Logo.png"
Body_Weight = "Body Weight_.png"
Height = "Height_.png"
BMI = "Body Mass Index_.png"
Health_Score = "Health Score_.png"
newpg()
##============================================Page 1======================================#
pdf.add_page()
pdf.image(logo, x= 2.5 , y=0.1, w=4 , h= 0.75, )
pdf.rect(0.75,1,width-1,height-2)
pdf.set_font('times','I',20)
pdf.text(2,1.5, "{}'s Health Report".format(Name))

x0 = -0.5; y0 = 1
pdf.rect(1.75+x0,1.25+y0,4+x0,1.75+y0)       # (pdf.rect(left,top,right,bottom))
pdf.set_font('times','',14)
pdf.text(2+x0,1.75+y0, "Name:           Shreesha")
pdf.text(2+x0,2.25+y0, "ID:               MFSH93")
pdf.text(2+x0,2.75+y0, "Gender:             Male")
pdf.text(2+x0,3.25+y0,  "DOB:         07/01/1993")

#pdf.image(Health_Score,x=5.5,y=2.5, w=2,h=1.75)
#pdf.ln(pdf.font_size)
pdf.text(1.1,5.5,"Dear {}".format(Name))
intro = """Metflux is pleased to provide you with your personalized overall \
health Report designed to help you discover a healthier and better you\
by providing recommendations to your daily diet based on cutting-edge \
technology developed by our team.\
Everything you eat and drink over time matters. \
The right mix can help you be healthier now and in the future.\
Start with small changes to make healthier choices and enjoy life \
keeping your body at its prime and we can help you get there!!"""
pdf.ln(0.15)
ylastP=pdf.get_y()
pdf.set_xy(1.1,5.65)
pdf.set_font('times','',12)
pdf.multi_cell(epw-0.75,0.25,intro)
##============================================Page 2======================================#

newpg()
basic_details = [['Name', 'Gender', 'Age'],
                 ['Shreesha', 'Male', '24'],
                 ['ID','XYZ','ABC' ],
                 ['CPnsk12', 'XYZ1','ABC1']]
col_width = epw/3
th = pdf.font_size
#pdf.cell(epw, 0.0, 'Demographic data', align='C', )
pdf.ln(0.75)
for row in basic_details:
    for r in row:
#        pdf.cell(col_width,th, str(r),align ='C',border=1)
        pdf.cell(col_width,2*th, str(r),align ='C',border=1)
    pdf.ln(2*th)    
#pdf.image(Body_Weight, x=2,y = 4, w=2.2,h=1.5)
Text1 = "Your body weight is in healthy range. \
          But you accumulated too much of fat"

#pdf.text(4,4,Text1)

pdf.multi_cell(7,0.5,Text1)
pdf.image(Health_Score, x=5,y = 4, w=2.2,h=1.5)
pdf.image(Height, x=2,y = 8, w=2.2,h=1.5)
pdf.image(BMI, x=5,y = 8, w=2.2,h=1.5)

pdf.output('Page_1.pdf','F')
