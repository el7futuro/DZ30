from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=500)
    is_published = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='pictures', blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = "Выборка"
        verbose_name_plural = "Выборки"

    def __str__(self):
        return self.name
