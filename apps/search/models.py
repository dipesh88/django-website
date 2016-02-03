from django.db import models

class SearchItems(models.Model):
    
    object_name = models.CharField(max_length=255)
    search_text = models.CharField(max_length=1024)
    model_name = models.CharField(max_length=128)
    object_pk = models.IntegerField()
    
    class Meta:
        managed = False # uses custom sql migration for full text index  
        db_table = "search_searchitems"

    
       
