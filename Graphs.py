from col20 import *
# Defining a function for making a circle with a number inside it
def num_graph(Heading,Num,Unit,color):
    if __name__ == '__main__':
        import matplotlib.pyplot as plt
        fnt = "felix titling"
        plt.rcParams["font.family"] = fnt   # Setting font for the graph
        fig, grp = plt.subplots()
        grp.annotate(Num, xy = ([3,3.2]), size = 100, weight='bold', color = color)    
        if Heading == 'Body Mass Index' or Heading == 'Body Fat':       
            grp.annotate(Unit, xy = ([6.5,3.5]), size=15)
        else:
            grp.annotate(Unit, xy = ([7,3.5]), size=15)
        
        plt.title(Heading, y=0.85, size = 20)
        plt.ylim([0,10])
        plt.xlim([0,10])
        plt.axis('off')
        # Making a circle with the centre (5,5) and radius 3
        circle1 = plt.Circle((5,5), 3.2, color = 'k',alpha = 0.05)
        grp.add_artist(circle1)
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


