from col20 import *
import matplotlib.pyplot as plt
Height = 167
BWkg_m = [70, 70.2, 71, 71.1, 70.8, 69.9, 70.3, 70, 70.5, 71, 71.3,71.7]
def BW_grph(BWkg_m,Height,Gender):
    if __name__ == "__main__":
        import matplotlib.pyplot as plt
        fig , bw = plt.subplots()
        bwi = BWkg_m[0]
        if Gender == "Male":
            bw.plot(1,bwi,color = peter_river[9], markersize= 18, marker= '$\u2640$')
        else:
            bw.plot(1,bwi,'fuchsia', markersize= 18, marker= '$\u2642$')
        
        bw.annotate(str(bwi), xy = ([0.6,bwi+2.5]), size=15)
        bw.plot(list(range(2,13)), BWkg_m[1:], 'o-k')
        uul,ul,ll,lll = 30*Height*Height/10000,25*Height*Height/10000, 18*Height*Height/10000, 15*Height*Height/10000

        bw.fill_between([0,15],150,uul,color = alizarin[3])
        bw.fill_between([0,15],ul,uul,color = alizarin[2])        
        bw.fill_between([0,15],ll,ul,color = green_sea[2])
        bw.fill_between([0,15],lll,ll,color = sunflower[2])
        bw.fill_between([0,15],0,lll,color = sunflower[3])

        ymx,ymin = max(BWkg_m)+5,min(BWkg_m)-5
        plt.xlim([0,13])
        plt.xticks([])
#        plt.ylim([ymin,ymx])
        plt.ylim([lll,uul])
        plt.show()
    
BW_grph(BWkg_m,Height, "Male")    

uul,ul,ll,lll = 30*Height*Height/10000,25*Height*Height/10000, 18*Height*Height/10000, 15*Height*Height/10000

plt.fill_between([0,15],150,uul,color = alizarin[4])
plt.fill_between([0,15],ul,uul,color = alizarin[5])        
plt.fill_between([0,15],ll,ul,color = green_sea[2])
plt.fill_between([0,15],lll,ll,color = sunflower[2])
plt.fill_between([0,15],0,lll,color = sunflower[3])

plt.scatter(2,68, marker= '$\u2640$', color='pink', alpha=0.2)

#marker=ur'$\u2640$'