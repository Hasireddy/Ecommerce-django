from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"] # "-name" (descending order of the name)
        # We specify indexes to make the db query faster (Indexed DB > DB)
        indexes = [
            models.Index(fields=["name"])
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["-name"]),
            models.Index(fields=["created"]),
        ]


    def _str_(self):
        # This method customizes that what should be printed on screen when an object of the class is printed.
        return "\n".join([self.prop for prop in vars(self)])



