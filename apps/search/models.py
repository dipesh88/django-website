from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class Objects(models.Manager):
    pass


class SearchItems(models.Model):
    
    class Meta:
        managed = False # uses custom sql migration for full text index  
        db_table = "search_searchitems"    
    
    object_name = models.CharField(max_length=255)
    search_text = models.CharField(max_length=1024)
    app_label = models.CharField(max_length=128)
    model_name = models.CharField(max_length=128)
    object_pk = models.IntegerField()
    
    objects = Objects()
    
    
@receiver(post_save)
def save_search_item(*args,**kwargs):
    
    instance = kwargs['instance']
    if not hasattr(instance,'SearchConfig'):
        return
    
    item_name_field = instance.SearchConfig.item_name_field
    search_fields_set = set(instance.SearchConfig.search_fields)
   
    s = search_fields_set.copy()
    s.add(item_name_field)
    if kwargs['update_fields'] != None:
        if len(s.intersection(kwargs['update_fields'])) == 0:
            return

    search_text = ""
    for field in search_fields_set:
        search_text = search_text + getattr(instance,field) + " "
        

    item = SearchItems.objects.get_or_create(object_pk=instance.pk,
                                             app_label=instance._meta.app_label,
                                             model_name=instance._meta.model_name)[0]
    
    item.object_name = getattr(instance,item_name_field)
    item.search_text = search_text
    item.save()    
   
    return
    
    

    
       
