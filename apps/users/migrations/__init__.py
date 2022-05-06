from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('users', '0003_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Updated Datetime')),
                ('home', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='home.home')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'favourite',
            },
        ),
    ]
