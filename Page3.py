from fpdf import FPDF
#from webcolors import name_to_rgb

#importing data from Child Model
#from CMC_20SEP import plot_BW,plot_FM,plot_FM_id,plot_H,Total_carb,Total_Fat,Total_Prot,Totalt,plot_age,plot_status,plot_status_id,plot_FMP,plot_FMP_id,plot_BMI,plot_BMI_id,plot_H_id

pdf=FPDF(format='letter',unit='in')

#New Page With Boarder
def newpg():
    pdf.add_page()
    global left
    left = pdf.l_margin
    global right
    right = pdf.r_margin
    global top
    top = pdf.t_margin
    global bottom
    bottom = pdf.b_margin
    pdf.ln(0.15)

    global epw
    epw = pdf.w - left - right
    global eph
    eph = pdf.h - top -bottom

    pdf.rect(left, top, w=epw, h=eph)
    #ybefore=pdf.get_y()
    #pdf.set_xy(epw/3+left, ybefore)
    pdf.image(logo,x=6.2 , y=10.3, w=2 , h= 0.5, type ='PNG')
    #pdf.set_xy(left, ybefore)

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

BMI_pic="Body Mass Index_.PNG" 

BPF_pic="Body Fay_.png"

Weight_pic="Body Weight_.png"



#Text Lines

title = """
Your Personalised Health Report:-

"""

int111 = """'If you could give every individual the right amount of \
nourishment and exercise, not too little and not too much, then we have fond the\
 safest way to health.'"""

intro2 = """Metflux is pleased to provide you with your personalized overall\
 health Report designed to help you discover a healthier and better you \
by providing recommendations to your daily diet based on cutting-edge \
technology developed by our team.
Everything you eat and drink over time matters. \
The right mix can help you be healthier now and in the future.
Start with small changes to make healthier choices and enjoy life \
keeping your body at its prime and we can help you get there!!"""

Macro_Nutri = """Macronutrients are defined as a class of chemical compounds which humans consume in the \
largest quantities and which provide humans with the bulk of energy. There are 3 major \
Macronutrients Namely Carbohydrates, Proteins & Fats and a healthy diet includes a balance of \
protein, carbohydrates and fats. Reducing or increasing any one of these nutrients \
can have major consequences on the body."""

Body_Comp = """Experimental investigation of human metabolism, nutrition, and body \
composition over the past century has produced a wealth of quantitative data on how \
the body dynamically adapts in response to diet changes and an imbalance between energy \
intake and energy expenditure will lead to a change in body weight (mass) and body composition (fat and lean masses)."""

BMI = """The BMI is an attempt to quantify the amount of tissue mass (muscle, fat, and bone) in an individual, \
and then categorize that person as underweight, normal weight, overweight, or obese based on that value. \
A healthy BMI is between 18.5 and 23. BMI is calculated by dividing your weight by the square of your height,\
and is a general guide to let you know if you're within your healthy weight range.

The generic classification is as shown below:-

Underweight(<18) - Risk of developing problems such as nutritional deficiency and osteoporosis
Normal(18-23) - Healthy Range
Moderately Obese(23-28) - Moderate risk of developing heart disease, high blood pressure, stroke, diabetes.
Severely Obese(>28) - High risk of developing heart disease, high blood pressure, stroke, diabetes


"""

BMI_Result = """For a normal healthy adult, the BMI ranges from 18-23 and your current score is at """+str(BMI_CValue)+""". Continuing \
with your current lifestyle and diet, your score is predicted to be """+str(BMI_PValue)+""" after a year."""

Body_Weight = """

Body weight is the measurement of weight without items located on the person \
and any Excess or reduction in the body weight is regarded as an indicator of determining a person's health, \
with body volume measurement providing an extra dimension by calculating the distribution of body weight.




"""

Body_Weight_Result = """Considering that a normal healthy adult weigh around 47 to 60 kgs., \
your current weight is """+str(BW_CValue)+""" kgs and is predicted to rise to """+str(BW_PValue)+""" kgs with the current lifestyle and diet."""

BPF = """The body fat percentage (BFP) is the total mass of fat \
divided by total body mass \
where in body fat includes essential body fat and storage body fat. \
The BPF is considered as \
a fitness level measure as only body measurement calculates a persons \
relative body composition \
without regard to either height or body."""

Lean_Muscle = """Lean muscle is related to lean body mass, which is the \
content of the body without any fat. Lean body mass is used to calculate \
basal metabolic rate. Lean muscle refers to muscle that is independent, \
devoid of fat."""

##Page 1

newpg()

##Code for boxes

pdf.set_font('times','B',11)
pdf.image(logo,x= None, y=None, w= epw, h= 2, type ='JPEG')
pdf.ln()
pdf.cell(0.9)
pdf.cell(3,0.2,'Name: {}'.format(Name),border = 1 ,align = 'L')
pdf.cell(3,0.2,'Age: {}'.format(Age),border = 1, align ='L')
pdf.ln()
pdf.cell(0.9)
pdf.cell(3,0.2,'Gender: {}'.format(Sex),border = 1 ,align = 'L')
pdf.cell(3,0.2,'Body Weight: {} kgs'.format(Weight),border = 1, align ='L')
pdf.ln()
pdf.cell(0.9)
pdf.cell(3,0.2,'Height: {} cms'.format(Height),border = 1 ,align = 'L')
pdf.cell(3,0.2,'Date: {}'.format(Date),border = 1, align ='L')
pdf.ln(0.4)

##Code for Intro

pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,int111)
pdf.ln(0.15)
pdf.set_font('times','B',11)
pdf.cell(0,0,'Dear ABC,')
pdf.ln(0.15)
pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,intro2)
pdf.ln(0.25)

##Code for Macro Nutrients

pdf.set_font('times','B',14)
#pdf.set_fill_color(*name_to_rgb('black'))
#pdf.set_text_color(*name_to_rgb('white'))
pdf.multi_cell(epw,0.15,title, fill= 1, align = 'C')
#pdf.set_text_color(*name_to_rgb('Black'))
pdf.ln(0.25)
pdf.set_font('times','B',12)
pdf.cell(0,0,'Macronutrient Ratio')
pdf.ln(0.15)
pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,Macro_Nutri)
pdf.ln(0.15)

##Page 2

newpg()

##Code for Body Composition

pdf.set_font('times','B',12)
pdf.cell(0,0,'Body Composition Dynamics')
pdf.ln(0.15)
pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,Body_Comp)
pdf.ln(0.25)

##Code for BMI

pdf.set_font('times','B',12)
pdf.cell(0,0,'BMI- Body Mass Index')
pdf.ln(0.15)
pdf.set_font('times','',11)
ybeforeBMI = pdf.get_y()
pdf.multi_cell(epw/2,0.15,BMI)
yafterBMI = pdf.get_y()
hei = yafterBMI - ybeforeBMI
pdf.set_xy(epw/2+left, ybeforeBMI)
pdf.image(BMI_pic,x= None, y=None, w= epw/2, h= hei, type ='PNG')
pdf.set_xy(left, yafterBMI)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,'Your BMI Test Result:-', fill= 1, align = 'C')
pdf.ln(0.15)
pdf.set_font('times','',11)
#pdf.set_fill_color(*name_to_rgb('white'))
pdf.multi_cell(epw,0.15,BMI_Result,fill=1)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,' ', fill= 1, align = 'C')
pdf.ln(0.25)
##Code for Body Weight

pdf.cell(0,0,'Body Weight')
pdf.ln(0.15)
pdf.set_font('times','',11)
ybeforeBW = pdf.get_y()
pdf.image(Weight_pic,x= None, y=None, w= epw/2, h= 2, type ='PNG')
pdf.set_xy(epw/2+left,ybeforeBW)
pdf.multi_cell(epw/2,0.15,Body_Weight)
yafterBW = pdf.get_y()

pdf.set_xy(left,yafterBW)
pdf.ln(0.1)
pdf.set_font('times','B',12)
pdf.set_fill_color(229,229,229)
pdf.multi_cell(epw,0.15,'Your Body Weight Test Result:-', fill= 1, align = 'C')
pdf.ln(0.15)
pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,Body_Weight_Result)
pdf.ln(0.1)
pdf.set_font('times','B',12)
pdf.set_fill_color(229,229,229)
pdf.multi_cell(epw,0.15,' ', fill= 1, align = 'C')
pdf.ln(0.25)

##Page 3

newpg()

##Code for % fat

pdf.set_font('times','B',12)
pdf.cell(0,0,'BPF- Body Percentage Fat')
pdf.ln(0.15)
pdf.set_font('times','',11)
ybeforeBPF = pdf.get_y()
pdf.multi_cell(epw/2,0.15,BPF)
yafterBPF = pdf.get_y()
heig = yafterBPF - ybeforeBPF
pdf.set_xy(epw/2+left, ybeforeBPF)
pdf.image(BMI_pic,x= None, y=None, w= epw/2, h= heig, type ='PNG')
pdf.set_xy(left, yafterBPF)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,'Your BPF Test Result:-', fill= 1, align = 'C')
pdf.ln(0.15)
pdf.set_font('times','',11)
##pdf.set_fill_color(*name_to_rgb('yellow'))
##pdf.multi_cell(epw,0.15,BMI_Result,fill=1)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,' ', fill= 1, align = 'C')
pdf.ln(0.25)

##Code for Lean Muscle

pdf.cell(0,0,'Lean Muscle Mass')
pdf.ln(0.15)
pdf.set_font('times','',11)
ybeforeLM = pdf.get_y()
pdf.set_xy(epw/2+left,ybeforeLM)
pdf.multi_cell(epw/2,0.15,Lean_Muscle)
yafterLM = pdf.get_y()

##Space for Pic

pdf.set_xy(left,yafterLM)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,'Your Lean Muscle Mass Test Result:-', fill= 1, align = 'C')
pdf.ln(0.15)
pdf.set_font('times','',11)
#pdf.multi_cell(epw,0.15,Body_Weight_Result)
pdf.ln(0.1)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,' ', fill= 1, align = 'C')
pdf.ln(0.25)

##page 4

newpg()

##New idea

pdf.set_font('times','B',12)
pdf.cell(0,0,'Title')
pdf.ln(0.15)
pdf.set_font('times','',11)
pdf.multi_cell(epw/2,0.15,'Some Random Text')
pdf.ln(0.15)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,' ', fill= 1, align = 'C')
ybef=pdf.get_y()
pdf.ln(0.25)
ybeforeF = pdf.get_y()
pdf.cell(epw/2,0.15,'Your present day data')
pdf.ln(0.2)
pdf.image(BMI_pic,x= None, y=None, w= epw/2, h= 3, type ='PNG')
ybeforez=pdf.get_y()
pdf.ln(0.15)
pdf.set_xy(left, ybeforez)
pdf.set_font('times','',11)
pdf.multi_cell(epw/2,0.15,'Some Random Text for Present data                       \
dasdsadssa asdsdsadsdsad sdsdsdsfggth hthhdtheth thdthtdth htheththdhbth               ththbtbttb ththdggfb dffdgdfgtb dgbdbd,')
pdf.ln(0.15)
ylastP=pdf.get_y()
pdf.set_xy(epw/2+left, ybeforeF)
pdf.set_font('times','B',12)
pdf.multi_cell(epw/2,0.15,'Your Future Data')
ybeforex=pdf.get_y()
pdf.ln(0.2)
pdf.set_xy(epw/2+left, ybeforex)
pdf.image(BMI_pic,x= None, y=None, w= epw/2, h= 3, type ='PNG')
ybeforey=pdf.get_y()
pdf.ln(0.15)
pdf.set_xy(epw/2+left, ybeforey)
pdf.set_font('times','',11)
pdf.multi_cell(epw/2,0.15,'Some Random Textfor Future Data dsfsdfsdf sdfsdfsdf dfsdfsdf sdfsfsdf sfdfsdfdsf sdfsdfsdfsd sdfsdfdfsdf sdgsdgdsf dsfsdfdsfdsf')
pdf.ln(0.15)
ylastF=pdf.get_y()
ylast=ylastP
if ylastF > ylastP:
    ylast = ylastF
pdf.rect(epw/2+left, ybef, w= 0.01, h=ylast-ybef)
pdf.set_xy(left, ylast)
pdf.set_font('times','B',12)
#pdf.set_fill_color(*name_to_rgb('lightgray'))
pdf.multi_cell(epw,0.15,'Your Title Test Result:-', fill= 1, align = 'C')
pdf.ln(0.15)



##Code for Output

pdf.output('Final_Report.pdf','F')
