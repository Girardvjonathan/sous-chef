# coding=utf-8
import factory
import datetime
import random
from django.contrib.auth.models import User
from member.models import Member, Address, Contact, Client, PAYMENT_TYPE
from member.models import DELIVERY_TYPE, GENDER_CHOICES


class AddressFactory (factory.DjangoModelFactory):

    class Meta:
        model = Address

    street = factory.Faker('street_address')
    city = 'Montreal'
    postal_code = factory.Faker('postalcode')


class ContactFactory (factory.DjangoModelFactory):

    class Meta:
        model = Contact

    type = 'Home phone'
    value = factory.Faker('phone_number')
    #member = factory.SubFactory(MemberFactory)



class MemberFactory (factory.DjangoModelFactory):

    class Meta:
        model = Member

    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    address = factory.SubFactory(AddressFactory)


class ClientFactory (factory.DjangoModelFactory):

    class Meta:
        model = Client

    member = factory.SubFactory(MemberFactory)
    billing_member = member
    billing_payment_type = random.choice(PAYMENT_TYPE)[0]
    rate_type = "default"
    member = member
    emergency_contact = factory.SubFactory(MemberFactory)
    status = random.choice(Client.CLIENT_STATUS)[0]
    language = "en"
    alert = factory.Faker('sentence')
    delivery_type = random.choice(DELIVERY_TYPE)[0]
    gender = random.choice(GENDER_CHOICES)[0]
    birthdate = factory.Faker('date')
