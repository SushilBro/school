from odoo import api, fields, models, _
class SchoolStudents(models.Model):
    _name = "school.student"
    _description = "School Students"
    _rec_name="first_name"

    reference = fields.Char(string='Student ID:',required=True, copy=False,readonly=True,default=lambda self: _('New'))
    first_name = fields.Char(string='First Name', required=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name', required=True)
    clas = fields.Many2one('school.class',string='Class',default=1)
    section = fields.Many2one('school.section',string='Section')

    P_address = fields.Char(string='Permanent Address',required=True)
    P_first_street_name = fields.Char(string='First Street Name',required=True)
    P_second_street_name = fields.Char(string='Second Street Name')
    P_palika = fields.Char(string='पालिका',required=True)
    P_district = fields.Char(string='District',required=True)
    P_state = fields.Char(string='State',required=True)
    P_country = fields.Char(string='Country',required=True)
    zip_code = fields.Char(string='Zip Code')

    T_address = fields.Char(string='Temporary Address')
    T_first_street_name = fields.Char(string='First Street Name')
    T_second_street_name = fields.Char(string='Second Street Name')
    T_palika = fields.Char(string='पालिका')
    T_district = fields.Char(string='District')
    T_state = fields.Char(string='Temporary State')

    check_address = fields.Boolean('Same as Above', default=lambda self: self.env['school.class'].search([]))

    age  = fields.Integer(string='Age', tracking=True) 
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')

    parents_fullname = fields.Char(string='Full Name')
    phone_number = fields.Char(string='Phone Number')
    address = fields.Char(string='Address')
    dob = fields.Date(string='Date of Birth:')

    guardians_fullname = fields.Char(string='Full Name')
    guardinas_phone_number = fields.Char(string='Phone Number')
    guardinas_address = fields.Char(string='Address')
    
    image = fields.Binary(
        string='Student Image',
    )
    
    

    
    
    @api.model
    def create(self, vals):
        
        class_value=vals.get('clas')
        section_value=vals.get('section')

        print('-------------------------------->',class_value)
        print('------------------------------------------->',section_value)

        if vals.get('reference', _('New')) == ('New'):
            vals['reference'] =self.env['ir.sequence'].next_by_code('school.student') or _('New')
        
        res=super(SchoolStudents,self).create(vals)
        print('values------->', vals)
        return res
    

    def action_print(self):
        return self.env.ref('samata_school.report_student_pdf').report_action(self)
    
    def action_print_excel(self):
         return self.env.ref('samata_school.report_student_details_xls').report_action(self)

    @api.onchange('check_address')
    def check(self):
        # classes=self.clas.id
        # query=self.env.cr.execute("""SELECT * FROM school_class where id=('%s')"""% (classes))
        # section = self.env.cr.fetchall()
        print("------------------------------>" )
        if self.check_address:
            self.T_address=self.P_address
            self.T_district=self.P_district
            self.T_first_street_name=self.P_first_street_name
            self.T_second_street_name=self.P_second_street_name
            self.T_palika=self.P_palika
            self.T_state=self.P_state
        else:
            self.T_address=''
            self.T_district=''
            self.T_first_street_name=''
            self.T_second_street_name=''
            self.T_palika=''
            self.T_state=''
        
   
    


    
   