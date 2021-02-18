from django.db import models

# Create your models here.

class pollQuestion(models.Model):
  poll_question=models.CharField(max_length=200)
  poll_date=models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.poll_question


class Choice(models.Model):
  poll_question =  models.ForeignKey(pollQuestion, on_delete=models.CASCADE)
  choice_text =  models.CharField(max_length=200,null=True)
  votes=models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text





