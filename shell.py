from credit.models import Client, Account, Credit
from django.utils import timezone


c = Client(name='Бердиев Н.Д.', citizenship='кыргызстан', birth_year=1994, work_place='Codify')
c2 = Client(name='Касымбекова Ж.С.', citizenship='кыргызстан', birth_year=2000, work_place='No')
a = Account(account_type=1, client='Бердиев Н.Д.')
a2 = Account(account_type=1, client='Касымбекова Ж.С.')
cr = Credit(sum=5000)
cr2 = Credit(sum=9000)
