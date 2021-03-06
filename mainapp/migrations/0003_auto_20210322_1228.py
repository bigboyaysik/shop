# Generated by Django 3.1.5 on 2021-03-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210317_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
        ),
        migrations.RemoveField(
            model_name='symka',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='object_id',
        ),
        migrations.DeleteModel(
            name='Kepka',
        ),
        migrations.DeleteModel(
            name='Symka',
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Товар'),
            preserve_default=False,
        ),
    ]
