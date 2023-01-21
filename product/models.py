from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", related_name="children", on_delete=models.PROTECT, null=True, blank=True
    )

    class MPPTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = TreeForeignKey(
        "Category",
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
