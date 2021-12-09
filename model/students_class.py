from odoo import api, fields, models, _
class students_class(models.Model):
    _name = "school.class"
    _description = "Students Classes"
    _rec_name="clas"

    className = fields.Char(string='Class Name', required=True)
    clas = fields.Integer(string='Class',required=True)
    _sql_constraints = [ ('unique_clas','UNIQUE (clas)','This class is already inserted on your system') ]
    
    
    