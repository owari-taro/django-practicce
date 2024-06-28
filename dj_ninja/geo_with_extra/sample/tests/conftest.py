# from accounts.models import CustomUser
from pytest_factoryboy import register
import pytest
from sample.models import Author, Store
import factory
from faker import Faker
from factory import PostGenerationMethodCall
from datetime import datetime
from factory.fuzzy import FuzzyChoice
from factory.django import Password

# from emb.models import Product, Grid, Order
from datetime import datetime

# from emb.db_utils import calc_quarter
from functools import partial

NOW = datetime.now()
# fake = Faker()


class BaseFactory(factory.django.DjangoModelFactory):
    created_at = factory.LazyFunction(datetime.now)
    updated_at = factory.LazyFunction(datetime.now)


@register
class AuthorFactory(BaseFactory):
    name = factory.Faker("name")
    # pen_name=factory.Faker("name")

    @factory.lazy_attribute
    def pen_name(self):
        # reverse order
        return self.name[::-1]

    class Meta:
        model = Author


@register
class StoreFactory(BaseFactory):
    name = factory.Faker("name")
    # pen_name=factory.Faker("name"

    class Meta:
        model = Store


"""

@register
class ProductFactory(BaseFactory):
    product_uri = factory.Sequence(lambda n: 'S2B_dummy_%s' % n)
    label = FuzzyChoice(choices=["test1", "test2", "test3"])
    acq_date = factory.LazyFunction(datetime.now)
    # acq_period = factory.LazyFunction(create)
    cloud_coverage = FuzzyChoice(choices=[i for i in range(0, 99, 1)])

    class Meta:
        model = Product


DUMMY_IP_ADDRESS = [f"127.0.0.{i}" for i in range(10)]


@register
class OrderFactory(BaseFactory):
    old_product_file = factory.Sequence(lambda n: 'S2B_dummy_%s.zip' % n)
    new_product_file = factory.Sequence(lambda n: 'S2B_dummy_%s.zip' % n)
    ip_address = FuzzyChoice(DUMMY_IP_ADDRESS)

    class Meta:
        model = Order


@register
class CustomUserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    is_staff = False
    is_superuser = False
    # email
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username.replace(" ", ""))
    password = Password("test")  # PostGenerationMethodCall("set_password", "test")
    is_active = True
    updated_at = factory.LazyFunction(datetime.now)
    date_joined = factory.LazyFunction(datetime.now)
    organization = FuzzyChoice(choices=["test_org", "dummy_org", "abcd_org"])

    class Meta:
        model = CustomUser

@register
class FiscalYearFactory(BaseFactory):
    year = FuzzyChoice(choices=[year for year in range(NOW.year - 3, NOW.year, 1)])

    class Meta:
        model = FiscalYear


@register
class AcqPeriodFactory(BaseFactory):
    fiscal_year = factory.SubFactory(FiscalYearFactory)
    quarter = FuzzyChoice(choices=QuarterChoices.values)

    class Meta:
        model = AcqPeriod


def create() -> AcqPeriod:
    if query_set := FiscalYear.objects.filter(year=NOW.year):
        fiscal_year = query_set[0]
    else:
        fiscal_year = FiscalYearFactory.create(year=NOW.year)
    quarter = calc_quarter(NOW)
    if query_set := AcqPeriod.objects.filter(quarter=quarter, fiscal_year=fiscal_year):
        acq = query_set[0]
    else:
        acq = AcqPeriodFactory.create(fiscal_year=fiscal_year, quarter=quarter)
    return acq
"""


"""

class Order(Base):
    盛土抽出処理の管理テーブル
    

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    status = models.CharField(
        "処理状況",
        # verbose_name="処理状況",
        choices=OrderStatusChoices.choices,
        max_length=30,
        default=OrderStatusChoices.waiting.value,
    )
    expired_at = models.DateTimeField("有効期限", null=True, default=None, blank=True)
    old_product_file = models.FileField("旧時期画像", null=True, max_length=300)
    new_product_file = models.FileField(
        "新時期画像", null=True, max_length=300
    )  # .ForeignKey(Product,on_delete=models.CASCADE,related_name="tasks_new")
    result_file = models.FileField(null=True, blank=True, max_length=500)
    start_at = models.DateTimeField(
        "処理開始時刻", default=None, null=True, blank=True, help_text="処理開始時刻"
    )
    end_at = models.DateTimeField(
        "処理終了時刻", default=None, null=True, blank=True, help_text="処理終了時刻"
    )
    # is_uploadのほうがわかりやすい"
    is_uploaded = models.BooleanField(
        default=False, help_text="対象画像がアップロードされたものならTrue"
    )
    ip_address = models.GenericIPAddressField(
        "利用者IP", null=True, blank=True, help_text="clientのIPアドレス"
    )
    deleted_at = models.DateTimeField(
        "ファイル削除時刻",
        default=None,
        blank=True,
        null=True,
        help_text="抽出結果・アップロード画像の削除フラグ",
    )


"""


"""
@pytest.fixture
def create_acq_period():
    def _func(year: int, quarter: QuarterChoices):
        if query_set := FiscalYear.objects.filter(year=year):
            fiscal_year = query_set[0]
        else:
            fiscal_year = FiscalYear.objects.create(year=year)
        return AcqPeriod.objects.create(fiscal_year=fiscal_year, quarter=quarter)

    return _func
"""

"""
@pytest.fixture
def create_product_pair(create_acq_period):
    def _func(
        new_year=2023,
        new_quarter=3,
        old_year=2021,
        old_quarter=3,
        grid_name="test_grid",
    ):
        grid = Grid.objects.create(name=grid_name)
        new_acq = create_acq_period(new_year, new_quarter)
        old_acq = create_acq_period(old_year, old_quarter)
        new_product = ProductFactory.create(
            grid=grid,
            acq_period=new_acq,
        )
        old_product = ProductFactory.create(grid=grid, acq_period=old_acq)
        return new_product, old_product
        # new_product=ProductFactory(grid=grid)

    return _func
"""
