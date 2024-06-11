from django.db import models

class ArrowShaftModel(models.Model):
    # Arrow Shaft
    manufacturer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    inner_diameter = models.FloatField()
    color = models.CharField(max_length=30, default='black')
    
    def __str__(self):
        return f'{self.manufacturer} - {self.name} {self.inner_diameter}'

class ArrowShaftSpecific(models.Model):
    arrow_shaft = models.ForeignKey(ArrowShaftModel, on_delete=models.CASCADE)
    spine = models.IntegerField()
    outer_diameter = models.FloatField()
    weight_per_inch = models.FloatField()
    max_mength = models.FloatField()

    def __str__(self):
        return f'{self.arrow_shaft} (Spine: {self.spine}, {self.weight_per_inch} gn/in)'

class Arrow(models.Model):
    # Represents a complete arrow modell
    title = models.CharField(max_length=50)
    foc = models.FloatField(null=True)
    total_weight = models.FloatField(null=True)
    shaft = models.ForeignKey(ArrowShaftSpecific, on_delete=models.PROTECT, null=True)
    shaft_length = models.FloatField(null=True)

    def __str__(self):
        return self.title

class ArrowComponentType(models.Model):
    # Contains possible types of arrow components 
    #   e.g. shaft, feather, ...
    label = models.CharField(max_length=30) 

    def __str__(self):
        return self.label

class ArrowComponentPropertyType(models.Model):
    # Contains possibke properties of a specific component type
    #   e.g. max_length, inner_diameter, etc.
    label = models.TextField

    class PropertyUnit(models.TextChoices):
        GRAIN = "gn"
        INCH = "in"
        GRAIN_PER_INCH = "gn/in" 
    
    unit = models.CharField(max_length=5, choices=PropertyUnit, null=True)
    
    def __str__(self):
        return f'{self.label} ({self.unit})'

class ArrowComponent(models.Model):
    # Specific arrow components 
    type = models.ForeignKey(ArrowComponentType, on_delete=models.PROTECT)
    manufacturer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.manufacturer} - {self.name} ({self.type.label})'

class ArrowComponentProperty(models.Model):
    # Property of an arrow component
    arrow_component = models.ForeignKey(ArrowComponent, on_delete=models.CASCADE)
    property_type = models.ForeignKey(ArrowComponentPropertyType, on_delete=models.PROTECT)
    unit_value = models.FloatField(null=True)
    non_unit_value = models.CharField(max_length=20, null=True)

    
    def __str__(self):
        return self.arrow_component

class ArrowComponentRelation(models.Model):
    # Lists Describes the properties of an arrow
    arrow = models.ForeignKey(Arrow, on_delete=models.CASCADE, null=False)
    arrow_component = models.ForeignKey(ArrowComponent, on_delete=models.CASCADE, null=False)

    class PositionStart(models.TextChoices):
        SHAFT_FRONT = "FRONT"
        SHAFT_BACK = "BACK"   

    position_start = models.CharField(max_length=5, choices=PositionStart, default=PositionStart.SHAFT_FRONT) # either the component label or an own label 
    position_distance_mm = models.FloatField() # position measured from the end of the arrow shaft 

class KnowHowArticle(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()#

    
    def __str__(self):
        return self.title