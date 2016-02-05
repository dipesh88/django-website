import cPickle
import base64

from . import models
from .task import Task

def save_task_to_db(new_task):
    
    pickled_task = base64.b64encode(cPickle.dumps(new_task))
    t = models.QueuedTasks(pickled_task=pickled_task)
    t.save()
    return t.id
    
    
    
    