import re
color = [];
ntpd = open('colors.txt', 'r')
for line in ntpd:
    try:
        col_num = re.findall('^/.*/',line)[0][3:][:-3]
    except:
        pass
    if col_num not in color:
        color.append(col_num)
    globals()[color[len(color)-1].lower().replace(' ','_')]=[]
    try:
        col_nam = re.findall('^..+-',line)[0][1:][:-1]
    except:
        pass
ntpd = open('colors.txt', 'r')
for line in ntpd:
    for i in range(len(color)):
        if color[i-1].lower().replace(' ','-')+'-' in line:  
            globals()[color[i-1].lower().replace(' ','_')].append(re.findall('.*(#.+);',line)[0])


All_colors = (turquoise,
green_sea,
emerald,
nephritis,
peter_river,
belize_hole,
amethyst,
wisteria,
wet_asphalt,
midnight_blue,
sunflower,
orange,
carrot,
pumpkin,
alizarin,
pomegranate,
clouds,
silver,
concrete,
asbestos)


