from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph ,Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from django.contrib.auth.models import User 
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.units import inch

from django.utils.timezone import datetime
from dollar.models import Banco , Precio


 
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
 
    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
 
    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))


class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize


    


    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()
 
        # Header
        header = Image('/home/automation/webpage/borbolla_automation/static/images/pdf/header.png')
        header.drawHeight = 85
        header.drawWidth = 488
        header.hAlign = 'RIGHT'
        w , h = header.wrap(doc.width , doc.topMargin)
        header.drawOn(canvas , doc.leftMargin , 700)

        # Footer
        footer = Image('/home/automation/webpage/borbolla_automation/static/images/pdf/footer.png')
        footer.drawHeight = 150
        footer.drawWidth = 850
        #footer.hAlign = 'RIGHT'
        w , h = footer.wrap(doc.width , doc.bottomMargin)
        footer.drawOn(canvas , doc.leftMargin , h)
 
        # Release the canvas
        canvas.restoreState()

    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)
 
        # Our container for 'Flowable' objects
        elements = []
 
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
 
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        today = datetime.today()
        precios_hoy = Precio.objects.filter(fecha_creacion__year = today.year , fecha_creacion__month = today.month , fecha_creacion__day = today.day)
        users = User.objects.all()
        elements.append(Paragraph('Precio Dolar Hoy %s'%today, styles['Heading1']))

        for i, precio in enumerate(precios_hoy):
            elements.append(Paragraph('%s -- compra : %s venta : %s'%(precio.banco.nombre , precio.compra , precio.venta), styles['Normal']))
 
        doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)
 
        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf    

