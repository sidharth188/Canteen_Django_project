# Generated by Django 5.1.7 on 2025-04-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0003_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
