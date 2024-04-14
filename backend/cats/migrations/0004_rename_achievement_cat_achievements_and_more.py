# Generated by Django 4.2.11 on 2024-04-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_rename_achievements_cat_achievement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='achievement',
            new_name='achievements',
        ),
        migrations.AlterField(
            model_name='achievementcat',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_cats', to='cats.achievement'),
        ),
        migrations.AlterField(
            model_name='achievementcat',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_achievements', to='cats.cat'),
        ),
    ]