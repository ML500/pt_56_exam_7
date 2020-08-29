from django.db import models


class Poll(models.Model):
    text = models.TextField(max_length=200, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('-created_at',)
