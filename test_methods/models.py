from django.db import models

class TestMethod(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255, unique=True) 
    test_description = models.CharField(max_length=255) 
    test_columns = models.JSONField()  

    def __str__(self):
        return self.test_name


