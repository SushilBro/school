from odoo import api, fields, models, _
class students_class(models.Model):
    _name = "school.section"
    _description = "Students Classes"
    _rec_name="section_name"

    section_name = fields.Char(string='Section', required=True)
    clas = fields.Many2one(
        'school.class',
        string='Class',
        )
    _sql_constraints = [ ('unique_section_name','UNIQUE (section_name,clas)','This Section is already inserted on your Class') ]

    
    
    