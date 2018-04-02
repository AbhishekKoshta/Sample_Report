from col20 import *
# Defining a function for making a circle with a number inside it
def num_graph(Heading,Num,Unit,color):
    if __name__ == '__main__':
        import matplotlib.pyplot as plt
        fnt = "felix titling"
        plt.rcParams["font.family"] = fnt   # Setting font for the graph
#        plt.rcParams["font.family"] = "Quick Sand" 

        fig, grp = plt.subplots()
        grp.annotate(Num, xy = ([3,3.2]), size = 100, weight='bold', color = color)    
        if Heading == 'Body Mass Index' or Heading == 'Body Fat':       
            grp.annotate(Unit, xy = ([6.5,3.5]), size=15)
        else:
            grp.annotate(Unit, xy = ([7,3.5]), size=15)     
#        plt.title(Heading, y=0.85, size = 20, )
#        plt.rcParams["font.family"] = "Quick Sand" 
        plt.annotate(Heading, xy= ([2.5,8]),size=20, weight='bold')

        plt.ylim([0,10])
        plt.xlim([0,10])
        plt.axis('off')
        # Making a circle with the centre (5,5) and radius 3
        circle1 = plt.Circle((5,5), 3.2, color = 'k',alpha = 0.05)
#        grp.add_artist(circle1)
        plt.savefig(Heading +".png", dpi = 400)
        plt.grid()
        plt.show()
        # Figure completed but have extra borders, need to be cropped
        from PIL import Image
        img = Image.open("{}.png".format(Heading))
        w,h = img.size[0],img.size[1]
        # Cropping the image 
        img1 = img.crop((650,200,w-600,h-400))
        img1.save(Heading +"_.png")
        # Removing the previous image which has been cropped for optimizing the storage space
        import os
        os.remove(Heading +".png")

num_graph("Body Weight", 100 , "kg", wisteria[8])    
num_graph("Health Score", 98 , "", midnight_blue[5])    
num_graph("Height", 170 , "cm", emerald[8])    
num_graph("Body Mass Index", 23 , "kg/m\N{SUPERSCRIPT Two}", sunflower[8])    
num_graph("Body Fat", 20 , "%" , pomegranate[8])    

# Graph for when you eat
iBLSD = [25,30,15,30]
aBLSD = [5,40,15,40]





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
        plt.savefig("Macro.png", dpi=400)
        plt.show()

C_P_F = [65,10,25]    
Food_Comp(C_P_F)









# For checking the graph with different colors
'''
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
        grp.add_artist(circle1)
        plt.savefig(All_colors[i][8]+".png", dpi = 400)
        plt.show()
    
    
num_graph("Health Score", 98 , "%")    
'''


