# Generated by Django 3.0.8 on 2020-07-02 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(help_text='eg: 24cm x 24cm, 60cm x 60cm...', max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='eg: White, Yellow, Red...', max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductOrigin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='eg: Spanish, Indian, Iraqi...', max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='eg: Ceramic, Porsilan, Marmar...', max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('old_price', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='products.ProductArea')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='products.ProductColor')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='products.ProductOrigin')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='products.ProductType')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
