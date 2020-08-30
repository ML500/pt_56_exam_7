from django.db import models
from django.urls import reverse


class Poll(models.Model):
    text = models.TextField(max_length=200, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('-created_at',)


class Choice(models.Model):
    text = models.TextField(max_length=200, verbose_name='Текст')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос', related_name='choices')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'
