# Generated by Django 5.1.5 on 2025-02-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_category_todo_due_date_todo_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
