from django.db import models
from django.db.models import Count, F, ExpressionWrapper
from django.urls import reverse


class Poll(models.Model):
    text = models.TextField(max_length=200, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('poll_detail', kwargs={'pk': self.pk})

    def get_answers_count(self):
        return self.answers.count()

    def get_choices_with_stats(self):
        total_answers = self.get_answers_count()
        answer_counted = self.choices.annotate(answers_count=Count('answers'))
        expr = ExpressionWrapper(F('answers_count') / float(total_answers) * 100, output_field=models.FloatField())
        return answer_counted.annotate(answer_percent=expr)

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


class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос', related_name='answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='Вариант ответа', related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return f'{self.poll} - {self.choice}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('-created_at',)
