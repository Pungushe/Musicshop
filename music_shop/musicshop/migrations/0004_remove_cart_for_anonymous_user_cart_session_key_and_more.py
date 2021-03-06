# Generated by Django 4.0 on 2021-12-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0003_alter_album_out_of_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='for_anonymous_user',
        ),
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, max_length=1900, null=True, verbose_name='Ключ сессии'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='session_key',
            field=models.CharField(blank=True, max_length=1900, null=True, verbose_name='Ключ сессии'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicshop.customer', verbose_name='Покупатель'),
        ),
    ]
