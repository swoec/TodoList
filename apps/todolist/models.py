from django.db import models


# Create your models here.

class TodoList(models.Model):
    location = models.CharField(max_length=30, default="", verbose_name="location", help_text="location")
    priority = models.IntegerField(default=0, verbose_name='priority', help_text='priority')
    time = models.DateTimeField(verbose_name='data tiem', help_text='date time')
    repeat = models.IntegerField(default=0, verbose_name='repeat', help_text='repeat')
    notes = models.TextField(default='', verbose_name='notes', help_text='notes')
    alarm = models.IntegerField(default=0, verbose_name='alarm', help_text='alarm')
    reminder = models.IntegerField(default=0, verbose_name='reminder', help_text='reminder')
    name = models.CharField(default='', max_length=30, verbose_name='name', help_text='name')
    userid = models.IntegerField(default=0, verbose_name="userid", help_text='userid')

    class Meta:
        verbose_name = "todoitme"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
