#==========================Variables used in the report==================================#
from IPython import get_ipython
get_ipython().magic('reset -sf')
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter

import time
Name = "Abinas"
Current_Body_Weight = 78
Body_Weight_predicted = 79.2
Healthy_Body_Weight_Range = str(18*167*167/10000) + '-' + str(23*167*137/10000)

Current_Fat_mass = 20
Fat_mass_predicted = 23.2

Current_Fat_free_mass = 78-20
Fat_free_mass_predicted = 79.2-23.2    

Gender = 'Male'

Time_Stamp = time.strftime("%d") +' '+time.strftime("%B")+' '+time.strftime("%Y")
Age = 35
Height = 167
Carb_percent = 70
Fat_percent = 19
Prot_percent = 11

Ideal_Carb_percent = 55
Ideal_Fat_percent = 26
Ideal_Prot_percent = 19

Current_BMI = round(78/167/167*10000,1)
Predicted_BMI = round(79.2/167/167*10000,1)

C_P_F = [70,19,11]

def Brief_Report(c):
    X0 = -23; Y0 = -2
    Xl = -20; Yl = 2
    Xr = -20; Yr = 0
    c.drawString(50,50, "==============00==============")
    c.drawString(700,700, "=========+++++++++++++++++++++800")

    c.setFont('Helvetica-Bold',14)
    c.drawString(100+X0,800+Y0, "Personalized Brief Health Report by: ")
    c.drawString(450+X0,800+Y0,Time_Stamp)
    c.line(82+X0,790+Y0,564+X0,790+Y0)

    c.drawImage('MetFlux_Logo.png', 80+X0,685+Y0, 17*cm, 3.5*cm)
    X0 = -23; Y0 = -32
    Xl = -20; Yl = -32
    Xr = -20; Yr = -32
    c.setFont('Helvetica', 11)

    c.drawString(100+X0,700+Y0, "Name")
    c.drawString(230+X0,700+Y0, Name)
    c.drawString(350+X0,700+Y0, "Body Weight (kg)")
    c.drawString(510+X0,700+Y0, str(Current_Body_Weight))
    
    c.line(80+Xl,690+Yl,562+Xl,690+Yl)
    c.drawString(100+X0,680+Y0, "Age (years)")
    c.drawString(240+X0,680+Y0, str(Age))
    c.drawString(350+X0,680+Y0, "Height (cm)")
    c.drawString(510+X0,680+Y0, str(Height))


    X1=0;Y1=0
    c.setFont('Helvetica-Bold', 12)
    c.drawString(100+X0,650+Y0, "Macronutrient Intake")
    c.drawImage("Nutritional_Info.png", 80+X1,470+Y1, 6.5*cm, 5*cm)
    c.setFont('Helvetica', 11)
    c.drawString(350+X0,620+Y0, "Healthy Composition Range")
    c.drawString(350+X0,600+Y0, "Carbohydrate  '45-65'")
    c.drawString(350+X0,580+Y0, "Protein  '10-35'")
    c.drawString(350+X0,560+Y0, "Fat  '15-25'")

    c.setFont('Helvetica-Bold', 12)    
    c.drawString(100+X0,500+Y0, "Macronutrient Analysis")
    c.setFont('Helvetica', 11)
    HCI = '''A high-carb diet boosts blood sugar levels, prompting the pancreas to produce more insulin to handle the excess glucose. Over extended periods, a diet high in carbohydrates cause cells to become resistant to insulin, a major cause in type 2 or adult-onset diabetes High Carb consumption will increase your fat accumulation rate, as the fats are the most efficient way storing energy. Carbs are converted into fats through a metabolic pathways called De Novo Lipogenesis (DNL). As body try to optimize the energy storage, it converts carbs into fats.'''
    HPI='''High protein intake is recommended for individual working/training hard. Body have strict balance on protein synthesis and protein breakdown. If you are not working enough to burn the calories. Please do not take supplements of protein. It will load your kidney/liver with extra work.'''
    HFI='''The most serious risk of high fat diets is heart disease. According to the American Heart Association, a diet high in saturated fat can dramatically raise your cholesterol, increasing your risk of heart disease.'''
    
    
    if C_P_F[0] > 25:
        X_ci = 80; Y_ci=450
        temp=len(HCI)
        c.drawString(X_ci,Y_ci,'* '+ HCI[:90].strip())
        c.drawString(X_ci,Y_ci-10, HCI[90:180].strip())
        c.drawString(X_ci,Y_ci-20, HCI[180:270].strip())
        c.drawString(X_ci,Y_ci-30, HCI[270:360].strip())
        c.drawString(X_ci,Y_ci-40, HCI[360:450].strip())
        c.drawString(X_ci,Y_ci-50, HCI[450:540].strip())
        c.drawString(X_ci,Y_ci-60, HCI[540:temp+1].strip())
        Y_ci=Y_ci-80
    if C_P_F[1] > 15:
        temp=len(HPI)
        c.drawString(X_ci,Y_ci,'* '+ HPI[:90].strip())
        c.drawString(X_ci,Y_ci-10, HPI[90:180].strip())
        c.drawString(X_ci,Y_ci-20, HPI[180:270].strip())
        c.drawString(X_ci,Y_ci-30, HPI[270:360].strip())
        c.drawString(X_ci,Y_ci-40, HPI[360:450].strip())
        c.drawString(X_ci,Y_ci-50, HPI[450:540].strip())
        c.drawString(X_ci,Y_ci-60, HPI[540:temp+1].strip())        
        Y_ci=Y_ci-50
    if C_P_F[2] > 15:
        temp=len(HFI)
        c.drawString(X_ci,Y_ci,'* '+ HFI[:90].strip())
        c.drawString(X_ci,Y_ci-10, HFI[90:180].strip())
        c.drawString(X_ci,Y_ci-20, HFI[180:270].strip())
        c.drawString(X_ci,Y_ci-30, HFI[270:360].strip())
        c.drawString(X_ci,Y_ci-40, HFI[360:450].strip())
        c.drawString(X_ci,Y_ci-50, HFI[450:540].strip())
        c.drawString(X_ci,Y_ci-60, HFI[540:temp+1].strip())        
        Y_ci=Y_ci-80        
        
    c.setFont('Helvetica-Bold', 12)
    c.drawString(100+X0,300+Y0, "Breakup of Calorie Intake")
    c.drawImage("Daily_Kcal_Breakdown.png", 60+X1,125+Y1, 8.5*cm, 5*cm)
 
    c.drawString(330+X0,300+Y0, "Ideal Breakup of Calorie Intake")
    c.drawImage("Ideal_Daily_Kcal_Breakdown.png", 280+X1,125+Y1, 8.5*cm, 5*cm)
    
    c.setFont('Helvetica', 11)
    c.drawString(100+X0,150+Y0, "Comment")
    c.drawString(100+X0,130+Y0,"* Eat a heavy breakfast and it will boost your metabolism and keep you energetic throughout ")
    c.drawString(100+X0,115+Y0,"the day")
    c.drawString(100+X0,95+Y0, "* If you are planning to reduce your body weight, consume only 20 % from the dinner of the ")
    c.drawString(100+X0,80+Y0,"total kcal in a day")



# Next Page
    c.showPage()
    c.setFont('Helvetica-Bold', 14)
    c.drawString(100,798, "Physical Activity Graph")
    c.drawImage("Exercise.png", 60,580,8.5*cm,7.5*cm)    
    
    c.setFont('Helvetica', 12)    
    c.drawString(300,740,"Green area in graph shows the ideal kcal to be")
    c.drawString(300,730,"burnt through exercise on an average in a day")
    c.drawString(300,680,"Red area in graph shows actual kcal you have")
    c.drawString(300,670,"on an average through exercise in a day")
    
    
    X0=-20 ;Y0=-50
    c.setFont('Helvetica-Bold',14)
    c.drawString(100+X0,570+Y0, "Future Predictions")
    c.setFont('Helvetica',12)
    c.drawString(100+X0,540+Y0, "Health Indicators")
    c.drawString(320+X0,540+Y0, "Current")
    c.drawString(400+X0,540+Y0, "Healthy")
    c.drawString(485+X0,540+Y0, "After one year")
    
    c.drawString(190+X0,520+Y0, "Body Weight")
    c.drawString(320+X0,520+Y0, str(Current_Body_Weight))
    c.drawString(400+X0,520+Y0, "BW_range")
    c.drawString(500+X0,520+Y0, Healthy_Body_Weight_Range)
    
    c.drawString(190+X0,500+Y0, "Body Mass Index")
    c.drawString(320+X0,500+Y0, str(Current_BMI))
    c.drawString(400+X0,500+Y0, "18-23")
    c.drawString(500+X0,500+Y0, str(Predicted_BMI)) 
    
    c.drawString(190+X0,480+Y0, "% Fat")
    c.drawString(320+X0,480+Y0, str(Current_Fat_mass))
    if Gender== 'Male' :
        c.drawString(400+X0,480+Y0, "15-25")
    if Gender== 'Female':
        c.drawString(400+X0,480+Y0, "15-35")
    c.drawString(500+X0,480+Y0, str(Fat_mass_predicted))
    
    c.drawString(190+X0,460+Y0, "Lean Muscle Mass")
    c.drawString(320+X0,460+Y0, str(Current_Fat_free_mass))
    c.drawString(400+X0,460+Y0, "75-85")
    c.drawString(500+X0,460+Y0, str(Fat_free_mass_predicted))    
    
    c.drawString(100+X0,438+Y0, "Body composition Analysis")
    c.drawString(320+X0,438+Y0, "Deficient")
    c.drawString(400+X0,438+Y0, "Healthy")
    c.drawString(485+X0,438+Y0, "Excessive")
    
    
    c.drawString(190+X0,420+Y0, "Fat")
#    c.drawString(320+X0,420+Y0, '150')    
    
    c.drawString(400+X0,420+Y0, "30-70")
    c.drawString(500+X0,420+Y0, '---')    

    c.drawString(190+X0,400+Y0, "Protein")
    c.drawString(320+X0,400+Y0, "---")
    c.drawString(400+X0,400+Y0, "< 130")
    c.drawString(500+X0,400+Y0, "---")  

    c.drawString(190+X0,380+Y0, "Salts level")
    c.drawString(320+X0,380+Y0, "---")
    c.drawString(400+X0,380+Y0, "25-160")
    c.drawString(500+X0,380+Y0, "---")  

    c.drawString(190+X0,360+Y0, "Total Body Water")
    c.drawString(320+X0,360+Y0,"---")
    c.drawString(400+X0,360+Y0, "140-250")
    c.drawString(500+X0,360+Y0, "---")   

    c.drawString(190+X0,340+Y0, "Bone mineral mass")
    c.drawString(320+X0,340+Y0, "---")
    c.drawString(400+X0,340+Y0, "6-23")
    c.drawString(500+X0,340+Y0, "---")
    
    c.drawString(100+X0,315+Y0, "Health Analysis")    
    c.drawString(320+X0,300+Y0, '---' )
    if Current_BMI > 14 and Current_BMI < 23:
        c.drawString(190+X0,300+Y0, "Healthy")

    if Current_BMI > 22 and Current_BMI < 27:
        c.drawString(400+X0,300+Y0, "Obese")
    elif Current_BMI < 14:
        c.drawString(400+X0,300+Y0, "Malnourished")
    else:    
        c.drawString(400+X0,300+Y0, "Overweight")
    
    
    X0=-10;Y0=-25
    c.setFont('Helvetica-Bold',14)
    c.drawString(100+X0,215+Y0, "Comments for you")
    c.setFont('Helvetica',12)
    c.drawString (100+X0,180+Y0, "Your current health score is 60 based on your current lifestyle and dietary intake provided")
    c.drawString (100+X0,160+Y0, "* Health score can be increased following the metflux's suggestion")
    c.drawString (100+X0,140+Y0, "* Your macronutrient food composition is in healthy range.")
    c.drawString (100+X0,120+Y0, "* You need to focus on having an active lifestyle to mitigate the disease risk")
    c.drawString (100+X0,100+Y0, "* Please subscribe to MetFlux's advanced plan for getting MetFlux's suggestion")
    c.setFont('Helvetica',14)
#    c.drawString (15+X0,60+Y0, "You can mitigate the diabetes and cardiovascular risk by 40 % with simply following the MetFlux's suggestion")
    c.drawString (100+X0,60+Y0, "You can mitigate the diabetes and cardiovascular risk by 40% ")
    c.drawString (120+X0,40+Y0, "with simply following the MetFlux's suggestion")
#    c.drawString(100+X0,60+Y0,"MetFlux's suggestion")

import sys,os
fle = os.path.basename(sys.argv[0])[:-3]
Report_name = fle + str(Name) + ".pdf"    

c = canvas.Canvas(Report_name)
Brief_Report(c)
c.showPage()
c.save()
