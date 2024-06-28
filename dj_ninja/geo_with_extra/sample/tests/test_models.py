from sample.models import Author
import pytest
from shapely import Polygon
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class Test:

    # @pytest.mark.django_db
    def test_author(self, author_factory):
        author = author_factory.create()
        assert type(author) == Author

    # @pytest.mark.django_db
    @pytest.mark.parametrize("author__name", ["hoge"])
    def test_model_author(self, author):
        print(author)
        assert author.name == "hoge"
        # breakpoint()

    @pytest.mark.smoke
    def test_store_with_invalid_polygon(self, store_factory):
        '''
        Polygon outside of japanese extent is not allowed
        '''
        coords = ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0))
        polygon = Polygon(coords)
        # breakpoint()
        with pytest.raises(ValidationError):
            store_factory.create(geometry=polygon.wkt)
