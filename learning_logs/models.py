from django.db import models

# Create your models here.
class Groups(models.Model):
    """These are the technical groups we support e.g. Avamar, ITSM, Batch Errors, etc."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #adds timestamp for current time
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Post(models.Model):
    """An informational post for the selected group."""
    groups = models.ForeignKey(
        'groups' ,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:120] + "..."