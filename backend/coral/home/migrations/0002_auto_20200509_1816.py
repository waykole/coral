# Generated by Django 3.0.5 on 2020-05-09 12:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Coral Home Page'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='content_walls',
            field=wagtail.core.fields.StreamField([('content_wall', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('content_wall', wagtail.snippets.blocks.SnippetChooserBlock('blocks.ContentWall')), ('show_content_wall_on_children', wagtail.core.blocks.BooleanBlock(default=False, help_text='If this is checked, the content walls will be displayed on all children pages of this page.', required=False, verbose_name='Show content walls on children pages?'))]))], blank=True, verbose_name='Content Walls'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Cover image'),
        ),
    ]
