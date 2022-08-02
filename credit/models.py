from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.TextField(verbose_name='Гражданство', default='кыргызстан')
    birth_year = models.DateField(verbose_name='Дата рождения')
    work_place = models.TextField(verbose_name='Место работы', blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.IntegerField(verbose_name='Номер аккаунта', primary_key=True)
    account_type = models.IntegerField(verbose_name='Тип аккаунта', default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        db_table = 'accounts'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сума кредита')
    date = models.DateTimeField(verbose_name='Дата получения кредита', auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Кредит')

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'

    def __str__(self):
        return self.sum