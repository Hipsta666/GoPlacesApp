from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Place(models.Model):
    name = models.CharField('Название', max_length=80)
    address = models.CharField('Адресс', max_length=80)
    rating = models.FloatField('Рейтинг')
    description = models.TextField('Описание')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги', related_name='places')
    average_check = models.PositiveIntegerField('Средний чек', default=0)
    poster = models.ImageField('Постер', upload_to='posters/')
    url = models.SlugField(max_length=80, unique=True)

    def tag_list(self):
        return u" %s" % (u", ".join([tag.title for tag in self.tags.all()]))
    tag_list.short_description = u'Теги'

    def get_absolute_url(self):
        return reverse('offer_detail', kwargs={'slug': self.url})

    def __str__(self):
        return f'{self.name}, {self.address}'


class Answer(models.Model):
    answer_text = models.CharField('Ответ', max_length=255)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги', related_name='answers')

    def tag_list(self):
        return u" %s" % (u", ".join([tag.title for tag in self.tags.all()]))
    tag_list.short_description = u'Теги'

    def __str__(self):
        return f'{self.answer_text}'


class Question(models.Model):
    question_text = models.CharField('Вопрос', max_length=255)
    answers = models.ManyToManyField(Answer, blank=True, verbose_name='Ответы', related_name='questions')

    def __str__(self):
        return f'{self.question_text}'





