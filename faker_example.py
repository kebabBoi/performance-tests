from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.email(domain='gmail.com'))

fake2 = Faker('ru_Ru')

print(fake2.name())
print(fake2.address())
print(fake2.email(domain='mail.ru'))