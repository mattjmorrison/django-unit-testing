from django.db import models

class SampleManager(models.Manager):

    @property
    def base_query(self):
        return self.order_by('one', 'two', 'three')

    @property
    def filter_property(self):
        return self.filter(one=1, two=2).filter(three=3)

    @property
    def ordering(self):
        return self.order_by('one', 'two', 'three')

    def some_chained_call(self):
        return self.base_query.filter(one=1).filter(two=2).filter(three=3)

class Sample(models.Model):
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()

    objects = SampleManager()


