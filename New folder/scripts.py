import os
import pyxml2pdf
from reportlab.pdfbase.ttfonts import TTFont

xml = os.path.abspath('./sample.xml')
pdf = os.path.abspath('./sample.pdf')

pyxml2pdf.genpdf(xml,pdf)