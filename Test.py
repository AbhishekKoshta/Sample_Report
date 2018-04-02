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


##Code for Output

pdf.output('Final_Report.pdf','F')
