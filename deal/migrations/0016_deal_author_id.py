# Generated by Django 2.1.4 on 2018-12-20 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0015_order_author_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='author_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='deal_requests_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
