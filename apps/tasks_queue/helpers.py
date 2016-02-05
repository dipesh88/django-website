import datetime
import cPickle
import base64

from . import models
from .task import Task

def save_task_to_db(new_task):
    
    pickled_task = base64.b64encode(cPickle.dumps(new_task))
    t = models.QueuedTasks(pickled_task=pickled_task)
    t.save()
    new_task.db_id = t.id
    return

def save_task_failed(task,exception):
    
    t = models.FailedTasks(task_id=task.db_id,
                           exception=exception.message)
    t.save()
    
    
def save_task_success(task):
    
    t = models.SuccessTasks(task_id=task.db_id)
    t.save()
    
    
    
    
    
    