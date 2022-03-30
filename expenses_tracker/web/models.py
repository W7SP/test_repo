from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.

from expenses_tracker.web.validators import only_letter_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0
    IMAGE_MAX_FILE_SIZE_IN_MB = 5
    UPLOAD_TO_DIR = 'profiles/'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letter_validator,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letter_validator,
        ),
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    image = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
          MaxFileSizeInMbValidator(IMAGE_MAX_FILE_SIZE_IN_MB),
        ),
    )


class Expenses(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )



