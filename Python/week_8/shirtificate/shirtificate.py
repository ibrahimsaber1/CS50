from fpdf import FPDF

name = input("Enter Your Name pls: ")

pdf = FPDF(orientation='P', format='A4')
pdf.add_page()

pdf.set_font("Arial", size=24)
pdf.cell(0, 40, txt="CS50 Shirtificate", ln=True, align='C')

pdf.image("shirtificate.png", x=0, y=60, w=pdf.w)

pdf.set_font("Arial", size=32)
pdf.set_text_color(255, 255, 255)

pdf.set_xy(0, 130)
pdf.cell(0, 20, txt=f"{name} took CS50", align='C')

pdf.output("shirtificate.pdf")
