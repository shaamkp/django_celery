import os
import uuid

from django.db import models


def get_csv_file_path(instance, filename):
    upload_path = f"web/media/csv-files"
    return os.path.join(upload_path, filename)


class CsvFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to=get_csv_file_path, blank=True, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'web_csv_files'
        verbose_name = 'Csv file'
        verbose_name_plural = 'Csv files'
        ordering = ('date_added',)

    def __str__(self):
        return self.name


