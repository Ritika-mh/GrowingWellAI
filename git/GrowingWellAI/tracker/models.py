from django.db import models

# Create your models here.

from django.db import models


class DailyRecord(models.Model):
    child_age = models.DecimalField(max_digits=4, decimal_places=1)

    food = models.TextField()
    protein_foods = models.TextField(blank=True)

    sleep_hours = models.DecimalField(
        max_digits=4, decimal_places=1
    )
    outdoor_minutes = models.PositiveIntegerField(default=0)
    study_minutes = models.PositiveIntegerField(default=0)
    screen_minutes = models.PositiveIntegerField(default=0)

    record_date = models.DateField()
    ai_response = models.TextField(blank=True, default='')
    def __str__(self):
        return f"Daily record - {self.record_date}"
        
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["record_date"],
                name="unique_daily_record_date"
            )
        ]


