from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model): 
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=2000) 
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        """Devolve uma representação em string do modelo."""
        return f"{self.owner}: {self.text[:50]}..."
        #return self.owner + " " +  self.text[:50] + "..."