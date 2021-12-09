from odoo import models
class Student_Details_Xlsx(models.AbstractModel):
    _name = 'report.samata_school.report_student_details_xl'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, student):
        print("student",student)
        for obj in student:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)