import os
import re

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import SuspiciousFileOperation
from django.db import models


ONE_TO_TEN_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


def safe_filename(filename):
    filename = re.sub(r'[^\w\s.-]', '', filename).strip()
    if '..' in filename or filename.startswith('/'):
        raise SuspiciousFileOperation("Detected path traversal attempt")
    return filename


class BusinessForm(models.Model):
    def get_upload_photo_path(self, filename):
        filename = safe_filename(filename)
        return os.path.join('banners', filename)

    def get_upload_spasibo_path(self, filename):
        filename = safe_filename(filename)
        return os.path.join('spasibo', filename)

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to=get_upload_photo_path)
    spasibo_photo = models.ImageField(upload_to=get_upload_spasibo_path)

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Конфигурации форм"
        verbose_name_plural = "Конфигурации форм"


class NewProduct(models.Model):
    SOURCE_CHOICES = [
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
    ]
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        verbose_name='Я увидел(а) эту анкету в:'
    )

    BOUGHT_PRODUCTS_CHOICES = [
        ('no', 'Нет'),
        ('yes', 'Да'),
    ]
    bought_products = models.CharField(
        max_length=20,
        choices=BOUGHT_PRODUCTS_CHOICES,
        verbose_name='Вы покупали какие-то мои продукты?'
    )

    city = models.CharField(
        max_length=120,
        verbose_name='Город проживания в настоящий момент'
    )

    age = models.CharField(
        max_length=50,
        verbose_name='Возраст'
    )

    specialization = models.CharField(
        max_length=255,
        verbose_name='Специализация (рефракционный хирург, ординатор, аспирант, врач-диагност и т.д.)'
    )

    income_rub = models.CharField(
        max_length=120,
        verbose_name='Ваш средний доход в месяц, в рублях, суммарный со всех источников'
    )

    OPERATIONS_STATUS_CHOICES = [
        ('self', 'Делаю самостоятельно'),
        ('mentor', 'Делаю под контролем наставника'),
        ('plan_to_start', 'Не делаю, планирую начать'),
        ('not_planning', 'Не делаю, не планирую начинать'),
        ('expand_horizon', 'Хочу изучить для расширения кругозора'),
    ]
    operations_status = models.CharField(
        max_length=40,
        choices=OPERATIONS_STATUS_CHOICES,
        verbose_name='Рефракционные операции (лазерные коррекции):'
    )

    study_goal = models.TextField(
        verbose_name='Зачем вы хотите изучить базовый курс рефракционной хирургии?'
    )

    current_difficulties = models.TextField(
        verbose_name='Какие сложности есть сейчас в области рефракционной хирургии? Что останавливает от того, чтобы достичь целей выше?'
    )

    attempted_solutions = models.TextField(
        verbose_name='Что уже пробовали делать, чтобы решить проблему? Что помогло, а что - не очень?'
    )

    subscription_info = models.TextField(
        verbose_name='Как давно вы на меня подписаны и откуда узнали?'
    )

    top_questions = models.TextField(
        verbose_name='ТОП-1 или ТОП-3 вопроса по рефракционной хирургии, которые вы хотите решить прямо сейчас:'
    )

    warmup_level = models.CharField(
        max_length=2,
        choices=ONE_TO_TEN_CHOICES,
        verbose_name='На сколько от 0 до 10 вы прогреты, чтобы начать у меня обучение любого формата?'
    )

    workload_level = models.CharField(
        max_length=2,
        choices=ONE_TO_TEN_CHOICES,
        verbose_name='Оцените уровень вашей занятости от 0 до 10'
    )

    full_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Ваше ФИО'
    )

    instagram = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Ссылка на ваш инстаграм'
    )

    telegram_channel = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Ссылка на ваш телеграм-канал'
    )

    telegram = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Ссылка на ваш личный телеграм (не канал) в формате https://t.me/doc_malahova или через @'
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Контактный телефон'
    )

    email = models.EmailField(
        blank=True,
        verbose_name='Адрес электронной почты'
    )

    policy_agreement = models.BooleanField(
        default=False,
        verbose_name='Согласен с политикой обработки персональных данных'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Анкета предзаписи на базовый курс по рефракционной хирургии'
        verbose_name_plural = 'Анкеты предзаписи на базовый курс по рефракционной хирургии'

    def __str__(self):
        return f"Анкета от {self.full_name or 'аноним'}"
