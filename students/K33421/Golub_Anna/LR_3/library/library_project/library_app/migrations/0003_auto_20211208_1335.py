# Generated by Django 3.2.8 on 2021-12-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20211208_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_total', models.IntegerField()),
                ('readers_total', models.IntegerField()),
                ('books_new', models.IntegerField()),
                ('readers_new', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='reader',
            name='reader_book',
            field=models.ManyToManyField(through='library_app.ReaderBook', to='library_app.Book', verbose_name='Книга'),
        ),
    ]