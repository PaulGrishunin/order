import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import glob, os
from datetime import datetime

class Order(models.Model):
    order_item = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=50, unique=True, default=uuid.uuid1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_name')
    created_on = models.DateTimeField(default=datetime.now)
    cost = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return self.order_list


