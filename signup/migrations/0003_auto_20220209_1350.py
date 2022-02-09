# Generated by Django 2.2.12 on 2022-02-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20220208_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade_produtos', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='cidade',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='endereco',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]