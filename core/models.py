from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    letter = models.CharField(max_length=1)
    colour = models.CharField(max_length=7, default="#000000")  # Hex colour code

    def __str__(self):
        return self.name

    def get_letter(self):
        return self.letter
    
    def get_colour(self):
        return self.colour

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_link(self):
        return self.link

    def get_description(self):
        return self.description
    
    def get_language(self):
        return self.language
    
    def get_tag(self):
        return (self.language.get_letter(), self.language.get_colour())

    class Meta:
        ordering = ['language__name', 'title']
        
