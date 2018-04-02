from col20 import *
# Graph for what you eat
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
        plt.savefig("Macro1.png", dpi=400)
        plt.show()

        from PIL import Image
        img = Image.open("Macro1.png")
        w,h = img.size[0], img.size[1]
        print (w,h)
        img1 = img.crop((300,200,w-200,h-100))
        img1.save("Macro_edited.png")
        
C_P_F = [55,26,19]    
Food_Comp1(C_P_F)