from fpdf import FPDF
class Pdf():
  
      
    def _create_pdf__(self,profile_data):
        pdf=FPDF(orientation = 'P', unit = 'mm', format='A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(90, 10, "Hello World!")
        pdf.cell(100, 10, 'Powered by FPDF.')
        return pdf