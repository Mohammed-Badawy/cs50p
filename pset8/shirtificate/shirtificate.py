from fpdf import FPDF

# Prmpt user for name
name = input("Name: ").strip()

# Text to be printed
text = f"{name} took CS50"

# Create pdf handle
pdf = FPDF(orientation="Portrait", format="A4")

# Add a new file and set font 
pdf.add_page()
pdf.set_font("helvetica", style="B",  size=40)

# Add Title to the page
pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# Add image to pdf page
pdf.image("shirtificate.png", w=pdf.epw)

# Set font and location of text
pdf.set_font_size(24)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, -240, text, new_x="LMARGIN", new_y="NEXT", align="C")

# Save to new file
pdf.output("shirtificate.pdf")