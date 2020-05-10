# Generated by Django 3.0.5 on 2020-04-26 14:30

import blocks.base_blocks
import blocks.html_blocks
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0006_coralnuskaindexpage_coralnuskapage_coralqnaindexpage_coralqnapage_coralrecipeindexpage_coralrecipepa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoralTrackerPage',
            fields=[
                ('coralpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.CoralPage')),
                ('body', wagtail.core.fields.StreamField([('text', blocks.html_blocks.RichTextBlock(icon='fa-file-text-o')), ('button', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False))])), ('image', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))])), ('image_link', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Alternate text to show if the image doesn’t load', max_length=255, required=True))])), ('html', wagtail.core.blocks.RawHTMLBlock(classname='monospace', icon='code', label='HTML')), ('download', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False)), ('automatic_download', wagtail.core.blocks.BooleanBlock(label='Auto download', required=False)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False))])), ('embed_video', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('url', wagtail.embeds.blocks.EmbedBlock(help_text='Link to a YouTube/Vimeo video, tweet, facebook post, etc.', label='URL', required=True))])), ('quote', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.core.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('google_map', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('search', wagtail.core.blocks.CharBlock(help_text='Address or search term used to find your location on the map.', label='Search query', max_length=255, required=False)), ('map_title', wagtail.core.blocks.CharBlock(help_text='Map title for screen readers, ex: "Map to Goodale Park"', label='Map title', max_length=255, required=False)), ('place_id', wagtail.core.blocks.CharBlock(help_text='Requires API key to use place ID.', label='Google place ID', max_length=255, required=False)), ('map_zoom_level', wagtail.core.blocks.IntegerBlock(default=14, help_text='Requires API key to use zoom. 1: World, 5: Landmass/continent, 10: City, 15: Streets, 20: Buildings', label='Map zoom level', required=False))])), ('page_list', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('blocks/pagelist_block.html', 'General, simple list'), ('blocks/pagelist_list_group.html', 'General, list group navigation panel'), ('blocks/pagelist_article_media.html', 'Article, media format'), ('blocks/pagelist_article_card_group.html', 'Article, card group - attached cards of equal size'), ('blocks/pagelist_article_card_deck.html', 'Article, card deck - separate cards of equal size'), ('blocks/pagelist_article_card_columns.html', 'Article, card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('indexed_by', wagtail.core.blocks.PageChooserBlock(help_text='Show a preview of pages that are children of the selected page. Uses ordering specified in the page’s LAYOUT tab.', label='Parent page', required=True)), ('categorized_by', blocks.base_blocks.CategoryTermChooserBlock(help_text='Only show pages with this category.', label='Categorized as', required=False)), ('show_preview', wagtail.core.blocks.BooleanBlock(default=False, label='Show body preview', required=False)), ('num_posts', wagtail.core.blocks.IntegerBlock(default=3, label='Number of pages to show'))])), ('page_preview', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('blocks/pagepreview_card.html', 'Card'), ('blocks/pagepreview_form.html', 'Form inputs')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Show a mini preview of the selected page.', label='Page to preview', required=True))])), ('card', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('blocks/card_block.html', 'Card'), ('blocks/card_head.html', 'Card with header'), ('blocks/card_foot.html', 'Card with footer'), ('blocks/card_head_foot.html', 'Card with header and footer'), ('blocks/card_blurb.html', 'Blurb - rounded image and no border'), ('blocks/card_img.html', 'Cover image - use image as background')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=255, required=False)), ('subtitle', wagtail.core.blocks.CharBlock(label='Subtitle', max_length=255, required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link'], label='Body')), ('links', wagtail.core.blocks.StreamBlock([('Links', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False))]))], blank=True, label='Links', required=False))])), ('carousel', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('carousel', wagtail.snippets.blocks.SnippetChooserBlock('blocks.Carousel'))])), ('image_gallery', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('collection', blocks.base_blocks.CollectionChooserBlock(label='Image Collection', required=True))])), ('modal', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False)), ('header', wagtail.core.blocks.CharBlock(label='Modal heading', max_length=255, required=False)), ('content', wagtail.core.blocks.StreamBlock([('text', blocks.html_blocks.RichTextBlock(icon='fa-file-text-o')), ('button', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False))])), ('image', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))])), ('image_link', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Alternate text to show if the image doesn’t load', max_length=255, required=True))])), ('html', wagtail.core.blocks.RawHTMLBlock(classname='monospace', icon='code', label='HTML')), ('download', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False)), ('automatic_download', wagtail.core.blocks.BooleanBlock(label='Auto download', required=False)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False))])), ('embed_video', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('url', wagtail.embeds.blocks.EmbedBlock(help_text='Link to a YouTube/Vimeo video, tweet, facebook post, etc.', label='URL', required=True))])), ('quote', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('text', wagtail.core.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.core.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('google_map', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('search', wagtail.core.blocks.CharBlock(help_text='Address or search term used to find your location on the map.', label='Search query', max_length=255, required=False)), ('map_title', wagtail.core.blocks.CharBlock(help_text='Map title for screen readers, ex: "Map to Goodale Park"', label='Map title', max_length=255, required=False)), ('place_id', wagtail.core.blocks.CharBlock(help_text='Requires API key to use place ID.', label='Google place ID', max_length=255, required=False)), ('map_zoom_level', wagtail.core.blocks.IntegerBlock(default=14, help_text='Requires API key to use zoom. 1: World, 5: Landmass/continent, 10: City, 15: Streets, 20: Buildings', label='Map zoom level', required=False))])), ('page_list', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('blocks/pagelist_block.html', 'General, simple list'), ('blocks/pagelist_list_group.html', 'General, list group navigation panel'), ('blocks/pagelist_article_media.html', 'Article, media format'), ('blocks/pagelist_article_card_group.html', 'Article, card group - attached cards of equal size'), ('blocks/pagelist_article_card_deck.html', 'Article, card deck - separate cards of equal size'), ('blocks/pagelist_article_card_columns.html', 'Article, card masonry - fluid brick pattern')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('indexed_by', wagtail.core.blocks.PageChooserBlock(help_text='Show a preview of pages that are children of the selected page. Uses ordering specified in the page’s LAYOUT tab.', label='Parent page', required=True)), ('categorized_by', blocks.base_blocks.CategoryTermChooserBlock(help_text='Only show pages with this category.', label='Categorized as', required=False)), ('show_preview', wagtail.core.blocks.BooleanBlock(default=False, label='Show body preview', required=False)), ('num_posts', wagtail.core.blocks.IntegerBlock(default=3, label='Number of pages to show'))])), ('page_preview', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('blocks/pagepreview_card.html', 'Card'), ('blocks/pagepreview_form.html', 'Form inputs')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Show a mini preview of the selected page.', label='Page to preview', required=True))]))], label='Content')), ('footer', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.CharBlock(icon='fa-file-text-o', label='Simple Text', max_length=255)), ('button', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False)), ('ga_tracking_event_category', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Category', max_length=255, required=False)), ('ga_tracking_event_label', wagtail.core.blocks.CharBlock(default='', label='Tracking Event Label', max_length=255, required=False))])), ('page_link', wagtail.core.blocks.PageChooserBlock(label='Page link', required=False)), ('doc_link', wagtail.documents.blocks.DocumentChooserBlock(label='Document link', required=False)), ('other_link', wagtail.core.blocks.CharBlock(label='Other link', max_length=255, required=False)), ('button_title', wagtail.core.blocks.CharBlock(label='Button Title', max_length=255, required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary'), ('btn-success', 'Success'), ('btn-danger', 'Danger'), ('btn-warning', 'Warning'), ('btn-info', 'Info'), ('btn-link', 'Link'), ('btn-light', 'Light'), ('btn-dark', 'Dark'), ('btn-outline-primary', 'Outline Primary'), ('btn-outline-secondary', 'Outline Secondary'), ('btn-success', 'Outline Success'), ('btn-outline-danger', 'Outline Danger'), ('btn-outline-warning', 'Outline Warning'), ('btn-outline-info', 'Outline Info'), ('btn-outline-light', 'Outline Light'), ('btn-outline-dark', 'Outline Dark')], label='Button Style', required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(choices=[('btn-sm', 'Small'), ('', 'Default'), ('btn-lg', 'Large')], label='Button Size', required=False))]))], label='Modal footer', required=False))])), ('pricelist', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('heading', wagtail.core.blocks.CharBlock(label='Heading', max_length=255, required=False)), ('items', wagtail.core.blocks.StreamBlock([('item', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('name', wagtail.core.blocks.CharBlock(label='Name', max_length=255, requred=True)), ('description', wagtail.core.blocks.TextBlock(label='Description', required=False, rows=4)), ('price', wagtail.core.blocks.CharBlock(help_text='Any text here. Include currency sign if desired.', label='Price', required=True))]))], label='Items'))])), ('reusable_content', wagtail.core.blocks.StructBlock([('settings', wagtail.core.blocks.StructBlock([('custom_template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default')], label='Template', required=False)), ('custom_css_class', wagtail.core.blocks.CharBlock(default='', label='Custom CSS Class', max_length=255, required=False)), ('custom_id', wagtail.core.blocks.CharBlock(default='', label='Custom ID', max_length=255, required=False))])), ('content', wagtail.snippets.blocks.SnippetChooserBlock('blocks.ReusableContent'))]))], blank=True, null=True)),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='Caption')),
                ('author_display', models.CharField(blank=True, help_text='Override how the author’s name displays on this article.', max_length=255, verbose_name='Display author as')),
                ('date_display', models.DateField(blank=True, null=True, verbose_name='Display publish date')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Coral Tracker Page',
            },
            bases=('pages.coralpage',),
        ),
        migrations.CreateModel(
            name='CoralChildGrowthPage',
            fields=[
                ('coraltrackerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trackers.CoralTrackerPage')),
            ],
            options={
                'verbose_name': 'Coral Child-Growth tracker page',
            },
            bases=('trackers.coraltrackerpage',),
        ),
        migrations.CreateModel(
            name='CoralOvulationPage',
            fields=[
                ('coraltrackerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trackers.CoralTrackerPage')),
            ],
            options={
                'verbose_name': 'Coral Ovulation tracker page',
            },
            bases=('trackers.coraltrackerpage',),
        ),
        migrations.CreateModel(
            name='CoralPregnancyPage',
            fields=[
                ('coraltrackerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trackers.CoralTrackerPage')),
            ],
            options={
                'verbose_name': 'Coral Pregnancy tracker page',
            },
            bases=('trackers.coraltrackerpage',),
        ),
    ]
