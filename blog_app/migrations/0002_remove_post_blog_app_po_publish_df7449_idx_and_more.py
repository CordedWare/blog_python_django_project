# Generated by Django 4.1.13 on 2024-01-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='blog_app_po_publish_df7449_idx',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'Черновик'), ('PB', 'Опубликовано')], default='DF', max_length=2),
        ),
    ]