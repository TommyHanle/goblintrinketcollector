from django.db import models
from django.urls import reverse

QUESTS = (
    ('F', 'Fetch'),
    ('E', 'Escort'),
    ('G', 'Gather'),
    ('K', 'Kill'),
    ('D', 'Delivery'),
    ('M', 'Mystery'),
    ('L', 'Lore'),
)

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchants_detail', kwargs={'pk': self.id})

class Trinket(models.Model):
    name = models.CharField(max_length=100)
    abilities = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    merchants = models.ManyToManyField(Merchant)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trinket_id': self.id})

class Uses(models.Model):
    date = models.DateField('date of usage')
    quest = models.CharField(
        max_length=1,
        choices=QUESTS,
        default=QUESTS[0][0]
    )
    details = models.TextField(max_length=250)

    trinket = models.ForeignKey(Trinket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_quest_display()} on {self.date}: {self.details}"

    class Meta:
        ordering = ['-date']

