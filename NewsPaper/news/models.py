from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.SET_DEFAULT, verbose_name="Автор", default=2)
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(
        max_length=18,
        unique=True,
        choices=[
            ("animals", "Животные"),
            ("children", "Дети"),
            ("cinema", "Кинематограф"),
            ("culture", "Культура"),
            ("economics", "Экономика"),
            ("family", "Семья"),
            ("food", "Еда"),
            ("health", "Здоровье"),
            ("humor", "Юмор"),
            ("investments", "Инвестиции"),
            ("music", "Музыка"),
            ("nature", "Природа"),
            ("politics", "Политика"),
            ("psychology", "Психология"),
            ("religion", "Религия"),
            ("science", "Наука"),
            ("technology", "Технологии"),
            ("sex", "Секс"),
            ("society", "Общество"),
            ("sports", "Спорт"),
            ("study", "Учеба"),
            ("travel", "Путешествия"),
            ("work", "Работа")
        ],
        verbose_name="Категория"
    )


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, verbose_name="Автор", default=2)
    type = models.CharField(
        max_length=4,
        choices=[
            ("NEWS", "Новость"),
            ("ARTI", "Статья")
        ],
        default="ARTI",
        verbose_name="Тип"
    )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name="Категория")
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ... {self.rating}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Статья")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    authorUser = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2, verbose_name="Пользователь")
    text = models.TextField(verbose_name="Текст")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()