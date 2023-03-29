from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.SET_DEFAULT, verbose_name="Автор", default=2)
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.authorUser}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating = pRat * 3 + cRat
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

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
    category = models.ManyToManyField('Category', through='PostCategory', verbose_name="Категория")
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    img = models.ImageField(upload_to="posts", verbose_name="Изображение")
    text = models.TextField(verbose_name="Текст")
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def display_category(self):
        """
        Для получения категории в админке
        """
        return ', '.join([category.name for category in self.category.all()[:3]])
    display_category.short_description = "Категория"

    def __str__(self):
        return f'{self.title}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ... {self.rating}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Статья")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    authorUser = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2, verbose_name="Пользователь")
    text = models.TextField(verbose_name="Текст")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Комментарии'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()