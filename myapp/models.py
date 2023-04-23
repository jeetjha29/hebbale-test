from django.db import models

class CategoryView(models.Model):
    name = models.CharField(max_length=50)
    cat_type = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    class Meta:
        db_table = "category"

