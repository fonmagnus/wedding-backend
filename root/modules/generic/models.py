from time import timezone
from django.db import models


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):

    objects = models.Manager()
    all_objects = models.Manager()

    is_deleted = models.BooleanField(default=False, editable=False)
    undeleted_objects = SoftDeleteManager()
    deleted_at = models.DateTimeField(null=True, default=None, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True
