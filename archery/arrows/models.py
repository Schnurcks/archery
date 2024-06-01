from django.db import models



class Arrow(models.Model):
    # Represents a complete arrow modell
    title = models.CharField()
    foc = models.FloatField()
    total_weight = models.FloatField()

    def __str__(self):
        return {self.title}

class ArrowComponentType(models.Model):
    # Contains possible types of arrow components 
    #   e.g. shaft, feather, ...
    label = models.CharField(max_length=30) 

class ArrowComponentPropertyType(models.Model):
    # Contains possibke properties of a specific component type
    #   e.g. max_length, inner_diameter, etc.
    label = models.TextField

    class PropertyUnit(models.TextChoices):
        GRAIN = "gn"
        INCH = "in"
        GRAIN_PER_INCH = "gn/in" 
    
    unit = models.CharField(max_length=5, choices=PropertyUnit, null=True)

class ArrowComponent(models.Model):
    # Possible arrow components 
    type = models.ForeignKey(ArrowComponentType)

class ArrowComponentProperty(models.Model):
    # Property of an arrow component
    arrow_component = models.ForeignKey(ArrowComponent, on_delete=models.CASCADE)
    property_type = models.ForeignKey(ArrowComponentPropertyType, on_delete=models.PROTECT)
    unit_value = models.FloatField(null=True)
    non_unit_value = models.CharField(null=True)

class ArrowComponentRelation(models.Model):
    # Lists Describes the properties of an arrow
    arrow = models.ForeignKey(Arrow, on_delete=models.CASCADE, null=False)
    arrow_component = models.ForeignKey(ArrowComponent, on_delete=models.CASCADE, null=False)

    class PositionStart(models.TextChoices):
        SHAFT_FRONT = "FRONT"
        SHAFT_BACK = "BACK"   

    position_start = models.CharField(max_length=5, choices=PositionStart, default=PositionStart.SHAFT_FRONT) # either the component label or an own label 
    position_distance_mm = models.DecimalField() # position measured from the end of the arrow shaft 

class KnowHow_Arcticle(models.Model):
    title = models.CharField()
    content = models.TextField()