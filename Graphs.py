from col20 import *
# Defining a function for making a circle with a number inside it
def num_graph(Heading,Num,Unit,color):
    if __name__ == '__main__':
        import matplotlib.pyplot as plt
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
        img1.save(Heading +".jpeg")
        # Removing the previous image which has been cropped for optimizing the storage space
        import os
        os.remove(Heading +"_.jpeg")

num_graph("Body Weight", 70 , "kg", wisteria[8])    
num_graph("Health Score", 98 , "", midnight_blue[5])    
num_graph("Height", 167 , "cm", emerald[8])    
num_graph("Body Mass Index", 24 , "kg/m\N{SUPERSCRIPT Two}", sunflower[8])    
num_graph("Body Fat", 28 , "%" , pomegranate[8])    
num_graph("Daily Exercise", 200 , "kcal/d" , emerald[8])    
num_graph("Energy Excess", 120 , "kcal/d" , pomegranate[8])    
num_graph("Energy Deficit", 000 , "kcal/d" , alizarin[8])    
num_graph("Basal Metabolic Rate", 1603 , "kcal/d" , green_sea[8])    

num_graph("Diabetes Risk", 36 , "%", carrot[8])    
num_graph("Heart Risk", 17 , "%", sunflower[8])    

# Graph for when you eat
iBLSD = [25,30,15,30]
aBLSD = [5,40,15,40]

def Food_Comp1(C_P_F):
    if __name__ == '__main__':
        import matplotlib.pyplot as plt
        plt.rcParams["font.family"] = 'Times New Roman'
        plt.rc('grid', color='black', alpha = 0.075)
        fig, fcmp = plt.subplots()
        fig.set_size_inches(8,4)
        x0,y0 = -0.5,0
        fcmp.fill_between([2+x0,3+x0],20,60,color = nephritis[3])
        fcmp.annotate("65", xy = ([1.5+x0,60+y0]), color = concrete[7], size = 20)
        fcmp.annotate("45", xy = ([1.5+x0,20+y0]), color = concrete[7], size = 20)
        fcmp.annotate("Carb", xy = ([2+x0,1+y0]), color = midnight_blue[9], size = 20)
        fcmp.plot([2+x0,3+x0],[2*C_P_F[0]-70,2*C_P_F[0]-70],'-k', 3 + x0,2*C_P_F[0]-70,'<k')
        fcmp.annotate(str(C_P_F[0])+"%",xy=([3.25+x0,2*C_P_F[0]-70+y0]),size=20,color=asbestos[8],weight='bold')
        
        x1,y1 = -0.25,0
        fcmp.fill_between([4.75+x1,5.75+x1],20,60,color = nephritis[3])
        fcmp.annotate("35", xy = ([4.25+x1,60+y1]), color = concrete[7], size = 20)
        fcmp.annotate("15", xy = ([4.25+x1,20+y1]), color = concrete[7], size = 20)
        fcmp.annotate("Protein", xy = ([4.75+x1,1+y1]), color = midnight_blue[9], size = 20)
        fcmp.plot([4.75+x1,5.75+x1],[2*C_P_F[1]-10,2*C_P_F[1]-10],'-k', 5.75+x1,2*C_P_F[1]-10,'<k')
        fcmp.annotate(str(C_P_F[1])+"%",xy=([6+x1,2*C_P_F[1]-10]),size=20,color=asbestos[8],weight='bold')
        
        x2,y2 = 0.25,0
        fcmp.fill_between([7.5+x2,8.5+x2],20,60,color = nephritis[3])
        fcmp.annotate("25", xy = ([7+x2,60+y2]), color = concrete[7], size = 20)
        fcmp.annotate("15", xy = ([7+x2,20+y2]), color = concrete[7], size = 20)
        fcmp.annotate("Fat", xy = ([7.75+x2,1+y2]), color = midnight_blue[9], size = 20)
        fcmp.plot([7.5+x2,8.5+x2],[4*C_P_F[2]-40,4*C_P_F[2]-40],'-k', 8.5+x2,4*C_P_F[2]-40,'<k', alpha=0.8)
        fcmp.annotate(str(C_P_F[2])+"%",xy=([8.75+x2,4*C_P_F[2]-40]),size=20,color=asbestos[8],weight='bold')
        
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
Food_Comp1(C_P_F)

BWkg_m = [70, 70.2, 71, 71.1, 70.8, 69.9, 70.3, 70, 70.5, 71, 71.3,71.7]
def BW_grph(BWkg_m):
    if __name__ == "__main__":
        import matplotlib.pyplot as plt
        plt.plot(1,BWkg_m[0],'.og')
        plt.plot(list(range(2,13)), )
    
    
    
    
    
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
