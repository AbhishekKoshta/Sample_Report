from col20 import *
import matplotlib.pyplot as plt
import math
# Defining a function for making a circle with a number inside it
def num_graph(Heading,Num,Unit,color):
#    if __name__ == '__main__':
        fnt = "felix titling"
#        fnt = "Quicksand"
        plt.rcParams["font.family"] = fnt   # Setting font for the graph
        fig, grp = plt.subplots()
        grp.annotate(Heading, xy= ([0,8]),size=20, weight='bold')
        grp.annotate(Num, xy = ([1,3.2]), size = 100, weight='bold', color = color)    

        if type(Num) == int:
            temp = str(Num)  
            ones, lnt = temp.count('1'), len(temp)
            x = 2 + ones*1.1 + (lnt-ones)*2.25
            grp.annotate(Unit, xy = ([x,3.5]), size=15)
        else:   
            temp = str(Num)  
            ones, lnt = temp.count('1'), len(temp)
            x = 2 + ones*1.1 + (lnt-ones-1)*2.5 + 0.5
            grp.annotate(Unit, xy = ([x,3.5]), size=15)
        plt.ylim([0,10])
        plt.xlim([0,15])
        plt.axis('off')
        # Making a circle with the centre (5,5) and radius 3
        circle1 = plt.Circle((5,5), 3.2, color = 'k',alpha = 0.05)
#        grp.add_artist(circle1)
        plt.savefig(Heading +"_.jpeg", dpi = 400)
        plt.grid()
        plt.show()
        # Figure completed but have extra borders, need to be cropped
        from PIL import Image
        img = Image.open("{}_.jpeg".format(Heading))
        w,h = img.size[0],img.size[1]
        # Cropping the image 
        img1 = img.crop((200,200,w-400,h-400))
        im = img1.save(Heading +".jpeg")
        # Removing the previous image which has been cropped for optimizing the storage space
        import os
        os.remove(Heading +"_.jpeg")
        return (img1.save(Heading +".jpeg"))

#num_graph("Body Weight", 70 , "kg", wisteria[8])    
#num_graph("Health Score", 98 , "", midnight_blue[5])    
#num_graph("Height", 167 , "cm", emerald[8])    
#num_graph("Body Mass Index", 24 , "kg/m\N{SUPERSCRIPT Two}", sunflower[8])    
#num_graph("Body Fat", 28 , "%" , pomegranate[8])    
#num_graph("Daily Exercise", 200 , "kcal/d" , emerald[8])    
#num_graph("Energy Excess", 120 , "kcal/d" , pomegranate[8])    
#num_graph("Energy Deficit", 000 , "kcal/d" , alizarin[8])    
#num_graph("Basal Metabolic Rate", 1603 , "kcal/d" , green_sea[8])    
#num_graph("Diabetes Risk", 36 , "%", carrot[8])    
#num_graph("Heart Risk", 17 , "%", sunflower[8])    

# Graph for when you eat
iBLSD = [25,30,15,30]
aBLSD = [5,40,15,40]

def Food_Comp1(C_P_F):
#    if __name__ == '__main__':
        import matplotlib.pyplot as plt
        plt.rcParams["font.family"] = 'Times New Roman'
        plt.rc('grid', color='black', alpha = 0.075)
        fig, fcmp = plt.subplots()
        fig.set_size_inches(8,4)
        x0,y0 = -0.5,0
        fcmp.fill_between([2+x0,3+x0],20,60,color = nephritis[3])
        fcmp.annotate("65", xy = ([1.5+x0,60+y0]), color = concrete[7], size = 20)
        fcmp.annotate("45", xy = ([1.5+x0,15+y0]), color = concrete[7], size = 20)
        fcmp.annotate("Carb", xy = ([2+x0,1+y0]), color = midnight_blue[9], size = 20)
        fcmp.plot([2+x0,3+x0],[2*C_P_F[0]-70,2*C_P_F[0]-70],'-k', 3 + x0,2*C_P_F[0]-70,'<k')
        fcmp.annotate(str(C_P_F[0])+"%",xy=([3.25+x0,2*C_P_F[0]-70+y0]),size=20,color=asbestos[8],weight='bold')
        
        x1,y1 = -0.25,0
        fcmp.fill_between([4.75+x1,5.75+x1],20,60,color = nephritis[3])
        fcmp.annotate("35", xy = ([4.25+x1,60+y1]), color = concrete[7], size = 20)
        fcmp.annotate("15", xy = ([4.25+x1,15+y1]), color = concrete[7], size = 20)
        fcmp.annotate("Protein", xy = ([4.75+x1,1+y1]), color = midnight_blue[9], size = 20)
        fcmp.plot([4.75+x1,5.75+x1],[2*C_P_F[1]-10,2*C_P_F[1]-10],'-k', 5.75+x1,2*C_P_F[1]-10,'<k')
        fcmp.annotate(str(C_P_F[1])+"%",xy=([6+x1,2*C_P_F[1]-10+y1]),size=20,color=asbestos[8],weight='bold')
        
        x2,y2 = 0.25,0
        fcmp.fill_between([7.5+x2,8.5+x2],20,60,color = nephritis[3])
        fcmp.annotate("25", xy = ([7+x2,60+y2]), color = concrete[7], size = 20)
        fcmp.annotate("15", xy = ([7+x2,15+y2]), color = concrete[7], size = 20)
        fcmp.annotate("Fat", xy = ([7.75+x2,1+y2]), color = midnight_blue[9], size = 20)
        fcmp.plot([7.5+x2,8.5+x2],[4*C_P_F[2]-40,4*C_P_F[2]-40],'-k', 8.5+x2,4*C_P_F[2]-40,'<k', alpha=0.8)
        fcmp.annotate(str(C_P_F[2])+"%",xy=([8.75+x2,4*C_P_F[2]-40+y2]),size=20,color=asbestos[8],weight='bold')
        
        x4,y4=0,-12
        fcmp.plot([11+x4,11.5+x4],[60+y4,60+y4],'-k',11.5+x4,60+y4,'<k')
        fcmp.annotate("Actual",xy=([11.85+x4,59+y4]),size=15 )
        fcmp.fill_between([11+x4,11.75+x4],50+y4,53+y4,color = nephritis[3])
        fcmp.annotate("Ideal",xy=([12.1+x4,50+y4]),size=15 )
        
        plt.ylim([0,80])
        plt.xlim([0,12.75])
#        plt.grid()
        plt.axis('off')
        plt.savefig("Macro1.jpeg", dpi=400)
        plt.show()

        from PIL import Image
        img = Image.open("Macro1.jpeg")
        w,h = img.size[0], img.size[1]
        print (w,h)
        img1 = img.crop((300,200,w-200,h-100))
        img1.save("Macro_edited.jpeg")
        
C_P_F = [55,26,19]    
#Food_Comp1(C_P_F)


# Graph for glucose dynamics and diab risk
def Glc_Dyn(G_f,Gpp):
#    if __name__ == "__main__":
        minutes = 1000
        import numpy as np
        from scipy.integrate import trapz
        # Parameters for glucose dynamics
        #G_f=float(G_f); Gpp = float(Gpp)
        x_h = 1.2; y_h = 62 ; z_h = 3; v_max_h =2.4 
        x_d = 1.2; y_d = 70; z_d =2.2 ; v_max_d = 3
        x_iv = 1.2; y_iv =0.14*G_f+60.7; z_iv =4.37-0.01739*G_f; 
        GL_healthy_curve=np.zeros((minutes+1));GL_diab_curve=np.zeros((minutes+1));GL_indv_curve=np.zeros((minutes+1))
        v_max_iv = (Gpp/G_f-1)/((120**x_iv/(120**x_iv+y_iv**x_iv ))*(y_iv**z_iv/(120**z_iv+y_iv**z_iv)))
        time2=np.ones((minutes+1))
        for t in range (minutes):
            GL_healthy_curve[t] = v_max_h*  t**x_h/(t**x_h+y_h**x_h )*y_h**z_h/(t**z_h+y_h**z_h)*79+79
            GL_diab_curve[t] = v_max_d*  t**x_d/(t**x_d+y_d**x_d )*y_d**z_d/(t**z_d+y_d**z_d)*125+125
            GL_indv_curve[t] = v_max_iv*  t**x_iv/(t**x_iv+y_iv**x_iv )*y_iv**z_iv/(t**z_iv+y_iv**z_iv)*G_f+G_f
            time2[t] = t
        Area_Healthy = trapz(GL_healthy_curve[:-1],time2[:-1])
        Area_Diab = trapz(GL_diab_curve[:-1],time2[:-1])
        Area_Indv = trapz(GL_indv_curve[:-1],time2[:-1])
        # Area_Healthy = np.trapz(time2,GL_healthy_curve)
        # Area_Diab = np.trapz(time2,GL_diab_curve)
        # Area_Indv = np.trapz(time2,GL_indv_curve)
        #print "Area_Healthy",Area_Healthy,"Area_Diab",Area_Diab,"Area_Indv",Area_Indv
        fig, gldyn = plt.subplots()
        gldyn.plot(time2[:-1], GL_indv_curve[:-1], '^', label="Individual")
        gldyn.plot(time2[:-1], GL_healthy_curve[:-1], 'g', label = "Healthy")
        gldyn.plot(time2[:-1], GL_diab_curve[:-1], 'r', label = "Diabetic")
#        gldyn.set_facecolor('xkcd:green')
        plt.xlabel("Time (in minutes)")
        plt.ylabel("Glucose dynamics")
        plt.legend()
        Gl_Dyn_pic =  "_Gl_Dyn.png"
        plt.savefig(Gl_Dyn_pic)
        plt.show()
        # The values for healthy and diabetic is taken from "http://www.webmd.com/diabetes/guide/glycated-hemoglobin-test-hba1c"
        Hb_h = 5.5; Hb_d=6.5
        slope = (Hb_d-Hb_h)/(Area_Diab-Area_Healthy)
        intercept = Hb_h - slope*Area_Healthy
        Hb_Ind_P = (slope*Area_Indv + intercept)*0.92
        sl_risk = (100-0)/(Hb_d-Hb_h)
        incpt_risk = 0 - sl_risk*Hb_h
        Current_Diab_Risk = (Hb_Ind_P*sl_risk+incpt_risk)
        if Current_Diab_Risk < 1 :
            Current_Diab_Risk = 1
        elif Current_Diab_Risk > 99 :
            Current_Diab_Risk = 98
        return (Current_Diab_Risk)
G_f,Gpp = 100,120
#Glc_Dyn(G_f,Gpp) 
 

# Graph for visualzing fat percent

def Fat_Vis(Fat,Fatp):
#    if __name__ == "__main__":
        from matplotlib.patches import Ellipse
        el = Ellipse((0, 0), 10, 20, facecolor='r', alpha=0.5)
        ###==============Less charaterization==============####
        pos1 = 10 ;     pos2 = 20
        wd = [[pos1,pos1],[pos2,pos2]]
        plt.fill_between([2,5],wd[0],wd[1],color=alizarin[7])
        plt.fill_between([6,13],wd[0],wd[1], color=emerald[8])
        plt.fill_between([14,17],wd[0],wd[1],color=green_sea[7])
        plt.fill_between([18,24],wd[0],wd[1], color=turquoise[6])
        plt.fill_between([25,35],wd[0],wd[1],color=orange[5])
        plt.fill_between([36,60],wd[0],wd[1],color=pomegranate[8])
        
        sz = 12
        up = wd[0][0] + 11; down = wd[0][0] - 2
        plt.annotate("2", xy = ([2, down]), size =sz, weight= 'bold')
        plt.annotate("6", xy = ([6, down]), size =sz, weight= 'bold')
        plt.annotate("14", xy = ([14, down]), size =sz, weight= 'bold')
        plt.annotate("18", xy = ([18, down]), size =sz, weight= 'bold')
        plt.annotate("25", xy = ([25, down]), size =sz, weight= 'bold')
        plt.annotate("35", xy = ([35, down]), size =sz, weight= 'bold')
        plt.annotate("50", xy = ([50, down]), size =sz, weight= 'bold')
        
        plt.annotate('Current Body Fat: {}%'.format(Fat),
                  xy=(Fat, up+2), xycoords='data',
                  xytext=(-100,up+20), textcoords='offset points',
                  size=18, va="center",
                  bbox=dict(boxstyle="round", fc=(0.7,0.9,1), ec="none"),
                  arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                  fc=(0.7,0.9,1), ec="none",
                                  patchA=None,
                                  patchB=el,
                                  relpos=(0.2, 0.5)))
        plt.annotate('After one year: {}%'.format(Fatp),
                  xy=(Fatp, down), xycoords='data',
                  xytext=(-50,down-80), textcoords='offset points',
                  size=18, va="bottom",ha='left',
                  bbox=dict(boxstyle="round", fc=(0.9, 0.9, 0.9), ec="none"),
                  arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                  fc=(0.9, 0.9, 0.9), ec="none",
                                  patchA=None,
                                  patchB=el,
                                  relpos=(0.2, 0.5)))
        plt.plot(Fat,21,'v',color =(0.7,0.9,1) ,markersize = 15,alpha=0.4)
        plt.plot(Fatp,9,'^k',markersize = 15,alpha=0.3)
        
        sz=10.5
        plt.annotate("Essential", xy = ([3,17.5]), rotation=90, color= 'w',size =sz, weight= 'bold')
        plt.annotate("Athlete", xy = ([9,17]), rotation=90, color= 'w',size =sz, weight= 'bold')
        plt.annotate("Fitness", xy = ([15,17]), rotation=90, color= 'w',size =sz, weight= 'bold')
        plt.annotate("Average", xy = ([21,17]), rotation=90, color= 'w',size =sz, weight= 'bold')
        plt.annotate("Overweight", xy = ([29,17.5]), rotation=90, color= 'w',size =sz, weight= 'bold')
        plt.annotate("Obese", xy = ([43,15]), rotation=90, color= 'w',size =sz, weight= 'bold')
        
        
        plt.xlim([0,60])
        plt.ylim([0,35])
        plt.axis('off')
        
        plt.savefig("Body_Fat_Vis.jpeg", dpi=400, bbox_inches='tight')
        plt.show()

#Fat_Vis(28,32.2)


def BW_grph(BWkg_m,Height):
#    if __name__ == "__main__":
        fig , bw = plt.subplots()
        bwi = BWkg_m[0]
        bw.plot(1,bwi,'og')
        bw.plot(list(range(2,13)), BWkg_m[1:], '*k')
        uul,ul,ll,lll = 30*Height*Height/10000,25*Height*Height/10000, 18*Height*Height/10000, 15*Height*Height/10000

        bw.fill_between([0,15],150,uul,color = pomegranate[3])
        bw.fill_between([0,15],ul,uul,color = pomegranate[2])        
        bw.fill_between([0,15],ll,ul,color = green_sea[2])
        bw.fill_between([0,15],lll,ll,color = sunflower[2])
        bw.fill_between([0,15],0,lll,color = sunflower[3])

        ymx,ymin = max(BWkg_m)+5,min(BWkg_m)-5
        plt.xlim([0,13])
#        plt.ylim([ymx,ymin])
        plt.show()

Height = 167
BWkg_m = [70, 70.2, 71, 71.1, 70.8, 69.9, 70.3, 70, 70.5, 71, 71.3,71.7] 
#BW_grph(BWkg_m,Height)    


# Pie chart for daily kcal breakdown
def Diet_dt(C_P_F,BLSD):
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 14    
    fig, nutri = plt.subplots()                
    colors1 = [All_colors[0][4] ,All_colors[12][2], All_colors[14][4]]                    
    colors1 = [All_colors[0][5] ,All_colors[4][5], All_colors[14][4]]                    
    nutri.pie(C_P_F,labels=['Carb','Fat','Protein'],colors=colors1,autopct='%1.1f%%',shadow=True,explode=[0,0,0.05])
    plt.savefig("Nutritional_Info.png")
    
    colors1 = All_colors[14][0:10:3]         
    colors1 = [All_colors[0][4] ,All_colors[12][2], All_colors[14][4], All_colors[18][4]]                    
    fig, daily_brk = plt.subplots()
    daily_brk.pie(BLSD,colors=colors1,shadow=True,explode=[0.05,0,0,0], labels=['Breakfast','Lunch','Snacks','Dinner'],autopct='%1.1f%%')
    plt.savefig("Daily_Kcal_Breakdown.png")
    
    colors1 = All_colors[18][0:10:4] 
    fig, nutri_id = plt.subplots()        
    nutri_id.pie(C_P_F,colors=colors1,shadow=True,explode=[0,0,0.05], labels=['Carb','Fat','Protein'],autopct='%1.1f%%')
    plt.savefig("Ideal_Nutritional_Info.png")
    
    colors1 = All_colors[2][0:10:3] 
    colors1 = [All_colors[0][4] ,All_colors[12][2], All_colors[14][4], All_colors[18][4]]                    
    fig, daily_brk_id = plt.subplots()        
    daily_brk_id.pie([25,30,15,30],colors=colors1,shadow=True,explode=[0.05,0,0,0], labels=['Breakfast','Lunch','Snacks','Dinner'],autopct='%1.1f%%')
    plt.savefig("Ideal_Daily_Kcal_Breakdown.png")
C_P_F,BLSD = [65,15,20], [15,30,15,40]
#Diet_dt(C_P_F,BLSD)
   


'''
# Graph for what you eat
def Food_Comp(C_P_F):
    if __name__ == '__main__':
        import matplotlib.pyplot as plt
        plt.rcParams["font.family"] = 'Times New Roman'
        plt.rc('grid', color='black', alpha = 0.075)
        
        plt.fill_between([1,3],45,65,color = emerald[3])
        plt.annotate("Carb", xy = ([1,1]), color = midnight_blue[9], size = 20)
        plt.plot([1,3],[C_P_F[0],C_P_F[0]],'-k', 3,C_P_F[0],'<k')
        plt.annotate(str(C_P_F[0]),xy=([2,C_P_F[0]+ 2]),size=20,color=asbestos[8],weight='bold')
        
        plt.fill_between([4,6],10,35,color = emerald[3])
        plt.annotate("Protein", xy = ([4,1]), color = midnight_blue[9], size = 20)
        plt.plot([4,6],[C_P_F[1],C_P_F[1]],'-k', 6,C_P_F[1],'<k')
        plt.annotate(str(C_P_F[1]),xy=([5,C_P_F[1]+ 2]),size=20,color=asbestos[8],weight='bold')
        
        plt.fill_between([7,9],15,25,color = emerald[3])
        plt.annotate("Fat", xy = ([7,1]), color = midnight_blue[9], size = 20)
        plt.plot([7,9],[C_P_F[2],C_P_F[2]],'-k', 9,C_P_F[2],'<k')
        plt.annotate(str(C_P_F[2]),xy=([8,C_P_F[2]+ 2]),size=20,color=asbestos[8],weight='bold')
        
        plt.ylim([0,80])
        plt.xlim([0,10])
        plt.annotate("Ideal", xy = ([10,80]))
        plt.xticks([])
        plt.grid()
#        plt.yticks([10,50,100])
        plt.axis('off')
        plt.savefig("Macro1.png", dpi=400)
        plt.show()

C_P_F = [40,40,20]    
Food_Comp(C_P_F)
'''

'''
# For checking the graph with different colors
def num_graph(Heading,Num,Unit):
    import matplotlib.pyplot as plt
    for i in range(len(All_colors)):
        fnt = "felix titling"
        plt.rcParams["font.family"] = fnt
        fig, grp = plt.subplots()
        grp.annotate(Heading, xy = ([0,10]), size = 20)
        
        
        grp.annotate(Num, xy = ([3,3.2]), size = 100, weight='bold', color = All_colors[i][8])
        grp.annotate(Unit, xy = ([7.25,3.5]), size=15)
        
        grp.annotate(All_colors[i][8], xy = ([0,0]), size = 20)
        
        plt.ylim([0,10])
        plt.xlim([0,10])
        plt.axis('off')
        
        circle1 = plt.Circle((5,5), 3, color = 'k',alpha = 0.05)
#        grp.add_artist(circle1)
        plt.savefig(All_colors[i][8]+".png", dpi = 400)
        plt.show()
    
    
num_graph("Health Score", 98 , "%")    
'''
