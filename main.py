import gdspy
from Template.Template import Template

Template().put('og', (0, 0, 0))
gdspy.write_gds('Template.gds')