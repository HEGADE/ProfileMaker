from math import ceil
from os import write

import fpdf
from helpers.pic_download import pic_download
import os

class PDF(fpdf.FPDF, fpdf.HTMLMixin):
    pass


class Pdf():
    def _create_pdf__(self, profile_data):
        pdf = PDF(orientation='P', unit='mm', format='A4')
        pdf.set_doc_option("core_fonts_encoding","utf-8'")
        pdf.add_page()
        pdf.set_font('Arial', '', 23)

        pdf.set_xy(0, 0)
        pdf.set_fill_color(21, 206, 235)
        pdf.cell(219, 70, '', fill=True)
        pdf.set_xy(80, 20)
        pdf.write(5, profile_data["name"].upper())
        pdf.set_font('Arial', '', 14)
        pdf.set_xy(80, 25)
        pdf.set_font_size(10)
        pdf.cell(10,10,profile_data["location"])
        pdf.set_left_margin(80)
        pdf.set_font_size(14)
        if profile_data["bio"]:
            pdf.set_y(35)
            pdf.write(7, profile_data["bio"])
        else:
            #need to add default profile bio
            pass
        saved_path = pic_download(profile_data["img"])
        
        pdf.image(saved_path, 10, 10, 50, 50, "jpg")
        #github
    
        pdf.set_xy(80,50)
        pdf.set_text_color(255,255,255)
        pdf.cell(10,10,"Github",link=f'https://github.com/{profile_data["name"]}')
        pdf.set_margins(99,40,0)
        pdf.cell(10,10,"Twitter",link=f'{profile_data["twiter"]}')
        pdf.set_margins(120,40,0)
        pdf.cell(10,10,"Personal site",link=f'{profile_data["site"]}')

        #projects display starts here
        pdf.set_font_size(22)
        pdf.set_xy(10,90)
        pdf.set_text_color(255, 196, 20)
        pdf.write(5,"My projects")
        # pdf.set_xy(10,100)
        # pdf.cell(20,10,"",border=3)
        pdf.set_font_size(17)

        initial_count=100
     
        pdf.set_text_color(0,0,0)
        for _,repo_name in enumerate(profile_data["repo"]):
            pdf.set_xy(10,initial_count)
            pdf.write(5,repo_name)
            initial_count+=20
        initial_count=110
        pdf.set_font_size(14)
        for repo_dec in profile_data["rep_des"]:
            try:
                pdf.set_xy(10,initial_count)
                pdf.set_right_margin(10)
                pdf.write(5,repo_dec)
                initial_count+=20
            except Exception as e:
                pass



        return pdf
