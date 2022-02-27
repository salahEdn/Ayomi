# Generated by Django 3.1.3 on 2020-11-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil_app', '0002_auto_20171013_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('Hardcover', 'Hardcover'), ('Paperback', 'Paperback'), ('E-book', 'E-book')], max_length=120),
        ),
    ]
