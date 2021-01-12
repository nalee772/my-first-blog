from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# 모델을 정의하는 코드 / class:객체를 정의한다 / Post: 변수명(post라는 객체 선언)
# models : Post가 장고 모델임을 의미 (이 코드로 장고는 post가 DB에 저장되어야 한다고 알게 됨
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 글자수가 제한된 텍스트 정의
    text = models.TextField()                # 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # def:메서드라는 뜻 / publish: 메서드명
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
