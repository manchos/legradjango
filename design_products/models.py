from django.db import models
from pytils.translit import slugify


from django.db import models
# from django.contrib.comments.moderation import CommentModerator, moderator
from django.urls import reverse
from autoslug import AutoSlugField


# Create your models here.


class DesignCategory(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name="Название")
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="Порядковый номер")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "категория дизайна"
        verbose_name_plural = "категории"


class DesignProduct(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True, verbose_name="Название")
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True) #models.SlugField()
    category = models.ForeignKey(DesignCategory, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name="Краткое описание")
    content = models.TextField(verbose_name="Полное описание")
    image = models.ImageField(upload_to="design_products/main", verbose_name="Основное изображение")

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        try:
            this_record = DesignProduct.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(DesignProduct, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(DesignProduct, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("goods_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "дизайн-работы"
        verbose_name_plural = "дизайн"


class DesignProductImage(models.Model):
    design_product = models.ForeignKey(DesignProduct, verbose_name="Дизайн-продукт", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="design_products/detail", verbose_name="Дополнительное изображение")
    description = models.TextField(verbose_name="Краткое описание")
    thumbnail = models.ImageField(upload_to="design_products/thumbnails", verbose_name="Дополнительное изображение")

    def save(self, *args, **kwargs):
        try:
            this_record = DesignProduct.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(DesignProduct, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(DesignProduct, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "изображение к дизайну"
        verbose_name_plural = "изображения к дизайну"

        # class GoodModerator(CommentModerator):
        #   email_notification = True

        # moderator.register(Good, GoodModerator)