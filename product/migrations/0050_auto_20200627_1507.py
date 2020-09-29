# Generated by Django 3.0.4 on 2020-06-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0049_auto_20200627_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={},
        ),
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.CharField(choices=[('false', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('false', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]