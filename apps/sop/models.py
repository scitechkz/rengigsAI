from django.db import models
from django.contrib.auth.models import User

class SOPDocument(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='sop_documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
