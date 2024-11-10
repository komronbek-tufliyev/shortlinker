from typing import Iterable
from django.db import models
from django.utils import timezone

from .utils import create_shortened_url


class UrlShortener(models.Model):
    url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    times_followed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Url Shortener"
        verbose_name_plural = "Url Shorteners"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.url} to {self.short_url}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)


class AccessLog(models.Model):
    url_shortener = models.ForeignKey(UrlShortener, related_name="access_logs", on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('url_shortener', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.url_shortener.short_url} accessed on {self.date} ({self.count} times)"

