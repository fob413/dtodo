from django.db import models

# Create your models here.
class Todo(models.Model):
    """This class represents the todo model"""
    name = models.CharField(max_length=255, blank=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return a human readable representation of the model instance"""
        return "{}".format(self.name)
