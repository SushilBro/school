odoo.define('samata_school.students', function (require) {
    "use strict";
    var basic_fields = require('web.basic_fields');

    var Toggle = basic_fields.BooleanToggle.extend({
        events: {
            _onClick: function (event) {
                if(this.node.attrs.custom === "click"){
        
                    alert("It works!!");
        
                 }
                 this._super();
                
            },
        }

    
});

fieldRegistry.add('toggle', Toggle);
    });