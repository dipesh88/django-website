

from .task import Task
from . import helpers

def push_task_to_queue(a_callable,*args,**kwargs):
    
    new_task = Task(a_callable,*args,**kwargs)
    task_id = helpers.save_task_to_db(new_task)
    
    
    
    
