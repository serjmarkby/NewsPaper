from django_filters import FilterSet, DateFilter
from .models import Post
import django.forms


class PostFilter(FilterSet):
    date_create = DateFilter(
        lookup_expr="gte",
        widget=django.forms.DateInput(
            attrs={
                'type': "date"
            }
        )
    )

    class Meta:
        model = Post

        fields = {
            "title": ["exact"],
            "category": ["exact"],

        }