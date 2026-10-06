from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores') #就是把每筆成績連到 Django 內建的會員。
    score = models.IntegerField() #分數
    wpm = models.IntegerField() #每分鐘打字數
    accuracy = models.IntegerField() #準確率
    correct = models.IntegerField() #正確字數
    wrong = models.IntegerField() #錯誤字數

    category = models.CharField(max_length=100) #類別
    mode = models.CharField(max_length=20) #練習類別

    duration = models.IntegerField(default=0) #測驗時間

    created_at = models.DateTimeField(auto_now_add=True) #創建時間

    def __str__(self):
        return f'{self.user.username} - {self.score}'
    