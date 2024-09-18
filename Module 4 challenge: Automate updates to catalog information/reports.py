#!/usr/bin/env python3

import reportlab.lib.styles
import reportlab.platypus

def generate_report(attachment, title, paragraph):
  styles = reportlab.lib.styles.getSampleStyleSheet()
  report = reportlab.platypus.SimpleDocTemplate(attachment)
  report_title = reportlab.platypus.Paragraph(title, styles["h1"])
  
  report_info = reportlab.platypus.Paragraph(paragraph, styles["BodyText"]) # Importante, para hacer saltos de linea en Paragraph usar etiqueta html <br/>

  report.build([report_title, report_info])