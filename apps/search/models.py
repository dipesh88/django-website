from django.db import models

class SearchItems(models.Model):
    
    class Meta:
        managed = False # uses custom sql migration for full text index  
        db_table = "search_searchitems"    
    
    object_name = models.CharField(max_length=255)
    search_text = models.CharField(max_length=1024)
    app_label = models.CharField(max_length=128)
    model_name = models.CharField(max_length=128)
    object_pk = models.IntegerField()
    
    

    
       
