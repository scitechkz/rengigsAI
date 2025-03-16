from rest_framework import serializers
from .models import SOPDocument

class SOPDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOPDocument
        fields = ["id", "title", "document", "uploaded_at"]
