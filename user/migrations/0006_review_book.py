# Generated by Django 5.0.1 on 2024-02-04 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_delete_review_remove_bookmodel_borrow_books'),
        ('user', '0005_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.bookmodel'),
        ),
    ]
