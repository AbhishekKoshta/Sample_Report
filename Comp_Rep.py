#from IPython import get_ipython
#get_ipython().magic('reset -sf')
import time
start = time.clock()
from fpdf import FPDF
pdf=FPDF(format='letter',unit='in')
pdf.set_margins(0.75, 1, 0.5)

global epw , width, height,left,right
left = pdf.l_margin
right = pdf.r_margin
top = pdf.t_margin
bottom = pdf.b_margin

width = pdf.w
height = pdf.h
epw = width - pdf.l_margin - pdf.r_margin
eph = height - pdf.l_margin - pdf.r_margin

#New Page With Boarder
def newpg():
    pdf.add_page()
    pdf.set_margins(0.75, 1, 0.5)

    pdf.set_font('times','I',12)
    pdf.text(0.75,0.65, "{}'s Health Report".format(Name))
    pdf.set_font('times','UI',12)
    pdf.text(1,height-0.7, "Doctor's Comment:-")
#    pdf.line(1,height-0.7,2,height-0.7)
    pdf.line(1,height-0.5,4,height-0.5)
    pdf.line(1,height-0.3,4,height-0.3)
#    pdf.multi_cell(0,0, "{}'s Health Report".format(Name))
#    pdf.multi_cell(0,9, "Doctor's comment".format(Name))
    pdf.image(logo, x= 6.2 , y=0.3, w=2 , h= 0.5)

#    pdf.rect(0.75,1,width-1,height-2)        # (pdf.rect(left,top,right,bottom))
    pdf.set_font('times','',14)
    pn = pdf.page_no()
    pdf.text(4.75,height-0.15, str(pn))
# Variables
Name = "Shreesha"
Age = "24"
Sex = "Male"
Height = "169"
Weight = "65"
Date = " "
htmp = float(Height)
Weight_Range = str(round(18*htmp*htmp/10000))+'-' +str(round(25*htmp*htmp/10000,1))  

if Sex == 'Male' and htmp > 165:
    Height_Comment = "You are taller than the average Indian male"
elif Sex == 'Male' and htmp < 165:
    Height_Comment = "You are shorter than the average Indian male"
elif Sex == 'Male' and htmp == 165: 
    Height_Comment = "Your height represents the average Indian's height"
elif Sex == 'Female' and htmp > 155:
    Height_Comment = "You are taller than the average Indian female"
elif Sex == 'Female' and htmp < 155:
    Height_Comment = "You are shorter than the average Indian female"
else:
    Height_Comment = "Your height represents the average Indian's height"

#Images
logo = "MetFlux_Logo.png"

# Page 1
#Body_Weight = "Body Weight.png"
#Height = "Height.png"
#BMI = "Body Mass Index.png"
#Health_Score = "Health Score.png"
#Fatpc = "Body Fat.png"

Body_Weight = "Body Weight.jpeg"
Height = "Height.jpeg"
BMI = "Body Mass Index.jpeg"
Health_Score = "Health Score.jpeg"
Fatpc = "Body Fat.jpeg"

# Page 2
Macronutrient = "Macro_edited.jpeg"
Kcl_brk = "Daily_Kcal_Breakdown.png"
Idl_Kcl_brk = "Ideal_Daily_Kcal_Breakdown.png"
BMR = "Basal Metabolic Rate.jpeg"
EE = "Energy Excess.jpeg"
ED = "Energy Deficit.jpeg"
DE = "Daily Exercise.jpeg"

BMI_pred = "BMI_bimonthly.png"
BWkg_pred = "BWkg.png"
Body_Fatpc = "Body_Fat_Vis.JPEG"

Glc_Dyn = "Glc_Dyn.png"
Hrt  =  "Heart Risk.jpeg"
Diab  = "Diabetes Risk.jpeg"

#newpg()



##============================================Page 1======================================#
pdf.add_page()
pdf.image(logo, x= 2.5 , y=0.1, w=4 , h= 0.75, )
#pdf.rect(pdf.l_margin,1,width-1,height-2)
pdf.set_font('times','B',14)
pdf.set_xy(0.75,1.2)
pdf.cell(0,0, "{}'s Health Report".format(Name),align = 'C')

x0 = 0; y0 = 0
pdf.rect(0.75+x0,1.45+y0,4+x0,2.25+y0)       # (pdf.rect(left,top,right,bottom))
#pdf.rect(.75+x0,1.25+y0,4+x0,1.75+y0)       # (pdf.rect(left,top,right,bottom))

pdf.set_font('times','',12)
pdf.text(1+x0,1.75+y0, "Name:           Shreesha")
pdf.text(1+x0,2.25+y0, "ID:               MFSH93")
pdf.text(1+x0,2.75+y0, "Gender:             Male")
pdf.text(1+x0,3.25+y0,  "DOB:         07/01/1993")

pdf.image(Health_Score,x=5.5,y=1.5, w=2,h=1.75)
#pdf.ln(pdf.font_size)
pdf.text(0.75,4,"Dear {},".format(Name))
intro = """Metflux is pleased to provide you with your personalized overall \
Health Report designed to help you discover a healthier and better you, \
by providing recommendations to your daily diet based on cutting-edge \
technology developed by our team. \

Everything you eat and drink over time matters. \
The right mix can help you be healthier now and in the future.\
Start with small changes to make healthier choices and enjoy life \
keeping your body at its prime and we can help you get there!!"""

pdf.set_xy(0.75,4.1)
pdf.set_font('times','',11)
pdf.multi_cell(epw,0.15,intro)
pdf.ln(0.25)
pdf.set_font("times",'BUI',12,)
pdf.multi_cell(epw+1,0.25,"Current Health Status", align='L')

frh = pdf.get_y()
pdf.set_font('times','',11)
#pdf.rect(left,frh, epw/2.1, 2 )
#<<<<<<< HEAD
#pdf.image(Body_Weight, x=left-0.2, y=frh, w=2.2,h=1.5, type = 'jpeg')
#pdf.set_xy(2.2,frh+0.15)
#pdf.multi_cell((epw/2)-0.15,0.15,"sdasdadasdasdasdasdasdsdasdasdsdasdasdsa\
#=======")
pdf.image(Body_Weight, x=left-0.2, y=frh, w=2,h=1.25, type = 'jpeg')
pdf.set_xy(2.1,frh+0.15)
##<<<<<<< HEAD
Body_Weight_Text = """Body Weight \

Body weight is the measurement of weight without items located on the person \
and any Excess or reduction in the body weight is regarded as an indicator of \
determining a person's health."""

pdf.multi_cell((epw/2)-1.25,0.15,Body_Weight_Text,align='L')
#=======
#pdf.multi_cell((epw/2)-2.25,0.15,"According to your height your ideal body weight \
#               should be in the {} range ".format(Weight_Range))
#>>>>>>> 263d03cb269bb5639ff5288508a5721979658fdf

rw,rh = epw/2.1-left + 0.55, 2
#pdf.rect(5,frh, rw, rh )
pdf.image(Height, x=4.5, y=frh, w=2,h=1.25, type = 'jpeg')
pdf.set_xy(6-0.1,frh+0.15)
pdf.multi_cell((epw/2)-2.25,0.15,Height_Comment)

#pdf.rect(left,frh+2.1, epw/2.1, 2 )
pdf.image(BMI, x=left-0.2, y=frh+2.1, w=2,h=1.25, type = 'jpeg')
pdf.set_xy(2.1,frh+0.15+2.1)
BMI_Text = """The BMI is an attempt to quantify the amount of tissue mass in an individual, \
and then categorize that person as underweight, \
normal weight, or obese based on that value."""
pdf.multi_cell((epw/2)-1.25,0.15,BMI_Text,align = 'L')

#pdf.rect(5,frh+2.1, rw,rh )
pdf.image(Fatpc, x=5-0.5, y=frh+2.1, w=2,h=1.25, type = 'jpeg')
pdf.set_xy(5.9,frh+0.15+2.1)
BFP_Text = """The BPF is considered as a fitness level measure \
as only body measurement calculates a \
person's relative body \
composition without regard to either height or body."""
pdf.multi_cell((epw/2)-1.25,0.15,BFP_Text,align = 'L')


##============================================Page 2======================================#

newpg()
pdf.set_font('times','B',12)
pdf.cell(0,0,"WHAT YOU EAT")
pdf.image(Macronutrient, x=left,y = top+0.55, w=epw,h=3)
macro = "Macronutrients, namely Carbohydrates, Proteins & Fats, \
are consumed in large quantities and provide humans with bulk of energy.  \
A healthy diet includes a balance of protein, carbohydrates and fats and \
Reducing or increasing any one of these nutrients can have major consequences \
on the body.\
\
Your current macronutrient intake is in the healthy range. Keep the \
good habit on!. You can add some fibrous food items in you diet such as \
banana/orange"
pdf.set_font('times','',11)
y = pdf.get_y()
#print (y)
pdf.set_xy(left,top+3.5)
pdf.multi_cell(epw,0.2,macro)
pdf.ln()

y = pdf.get_y()
#print (y)
pdf.set_font('times','B',12)
pdf.cell(0,0,"WHEN YOU EAT")
pdf.image(Kcl_brk, x=left,y = top+4.55, w=epw/2,h=3)
pdf.image(Idl_Kcl_brk, x=4.5,y = top+4.55, w=epw/2,h=3)
Kbr = "Taking the right balance of nutricious food as just as important as \
Taking the right amount of food at the right time.\
\
You have most of the food at your dinner time. Please make a \
habit of eating as much as you can in your breakfast.This will help\
you feel energetic through out the day and maintain your body weight."
pdf.set_font('times','',12)
pdf.set_xy(left,top+7.5)
pdf.multi_cell(epw,0.2,Kbr)
pdf.ln()



##============================================Page 3======================================#
newpg()
pdf.set_font('times','B',14)
pdf.cell(0,0,"PHYSICAL ACTIVITY/ENERGY EXPENDITURE DETAILS")
pdf.set_font('times','',11)
#pdf.line(1,top+0.5,epw-4,top+0.5)
#pdf.line(1,top+0.75,epw-6,top+0.75)
#pdf.line(1,top+1,epw-2,top+1)
pdf.set_xy(left,top+0.5)
pdf.multi_cell(epw,0.15,"zscsssssssssssssssssssssssssssssssss\
               \ssssssssssssssssssssssssssssssssssssssssssssssss")
btw= width-(left+2.6)-right
pdf.image(BMR, x = left, y = top+1, w=2.5,h=2.5)
pdf.set_xy(left+2.5,top+1.5)
pdf.multi_cell(btw,0.15,"zscsssssssssssssssssssssssssssssssss\
               \ssssssssssssssssssssssssssssssssssssssssssssssss")
pdf.image(DE, x = left, y = top+3.5, w=2.5,h=2.5)
pdf.set_xy(left+2.5,top+3.5+0.5)
pdf.multi_cell(btw,0.15,"zscsssssssssssssssssssssssssssssssss\
               \ssssssssssssssssssssssssssssssssssssssssssssssss")
pdf.set_xy(left+2.5,top+6+0.5)
pdf.image(EE, x = left, y = top+6, w=2.5,h=2.5)
pdf.multi_cell(btw,0.15,"zscsssssssssssssssssssssssssssssssss\
               \ssssssssssssssssssssssssssssssssssssssssssssssss")
#pdf.line(1,top+4.5,epw-6,top+4.5)
#pdf.line(1,top+4.75,epw-2,top+4.75)
'''
'''
##============================================Page 4======================================#
newpg()
pdf.set_font('times','B',14)
pdf.cell(0,0,"HEALTH PREDICTIONS")
# BMI prediction graph
pdf.set_font('times','',11)
pdf.image(BMI_pred, x=left,y = top+0.55, w=epw/2,h=2.5)
pdf.set_xy(epw/2+0.5,1.75)
BMI_Graph_Text= """BMI Prediction Graph

The BMI is an attempt to quantify the amount of tissue mass (muscle, fat, and bone) in an individual, \
and then categorize that person as underweight, normal weight, \
overweight, or obese based on that value. A healthy BMI is between 18.5 and 23. \
BMI is calculated by dividing your weight by the square of your height"""
pdf.multi_cell(epw/2-0.05,0.15,BMI_Graph_Text,align = 'L')
# Body weight dynamics
pdf.set_xy(left,4.25)
BMI_Graph_Text= """Body Weight Dynamics

Body weight is the measurement of weight without items located on the person \
and any Excess or reduction in the body weight is regarded \
as an indicator of determining a person's health, with body volume measurement \
providing an extra dimension by calculating the distribution of body weight."""
pdf.multi_cell(epw/2-0.05,0.15,BMI_Graph_Text,align = 'L')
pdf.image(BWkg_pred, x=left + epw/2,y = top+3, w=epw/2,h=2.5)
# Suggesting the fat %
pdf.image(Body_Fatpc, x=left,y = top+ 5.55, w=epw/2,h=2.5)
pdf.set_xy(epw/2+0.75,6.75)
BMI_Graph_Text= """Body Fat Percentage(BFP)

The body fat percentage (BFP) is the total mass of fat divided by total \
body mass where in body fat includes essential body fat and storage body fat. The BPF is \
considered as a fitness level measure as only body measurement calculates a person's \
relative body composition without regard to either height or body."""
pdf.multi_cell(epw/2-0.05,0.15,BMI_Graph_Text,align = 'L')

##============================================Page 5======================================#
newpg()
pdf.set_font('times','B',14)
pdf.cell(0,0,"HEALTH PREDICTIONS")
pdf.set_font('times','',11)
pdf.image(Glc_Dyn, x=left+0.5,y = top+0.55, w=epw/1.1,h=3)
pdf.set_xy(left,4.75)
Health_Text = """Diabetes is a disease in which your blood glucose, or \
blood sugar, levels are too high. Glucose comes from the foods you eat. \
Insulin is a hormone that helps the glucose get into your cells to give \
them energy. With type 1 diabetes, your body does not make insulin 

1) With type 2 diabetes, the more common type, the body does not produce \
enough insulin for proper function, or the cells in the body do not react \
to insulin.
2) Without enough insulin, the glucose stays in your blood. You can also \
have prediabetes. This means that your blood sugar is higher than normal but \
not high enough to be called diabetes."""

pdf.multi_cell(epw,0.15,Health_Text,align ='L')

pdf.image(Diab, x=left,y = top+5, w=epw/2.1,h=2)
pdf.set_xy(left,top+5+2.1)
Diab_Text = """Total cholesterol is a measure of the total amount of \
cholesterol in your blood, including low-density lipoprotein (LDL) \
cholesterol and high-density lipoprotein (HDL) cholesterol.
Cholesterol levels should be measured at least once every five years in \
everyone over age 20. Experts recommend that men ages 35 and \
older and women ages 45 and older be more frequently screened for lipid \
disorders
"""
pdf.multi_cell(epw/2-1,0.15,Diab_Text,align ='L')

pdf.image(Hrt, x=left+4.5,y = top+5, w=epw/2.1,h=2)
pdf.set_xy(epw/2+1,top+5+2.1)
Hrt_Text = """Some Random Text zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"""
pdf.multi_cell(epw/2-1,0.15,Hrt_Text,align ='L')

pdf.output('Demo4.pdf','F')
print ("Time taken ",time.clock()-start, "sec")
