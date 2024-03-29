# Generated by Django 3.0.5 on 2020-04-20 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL', verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, help_text='Your Twitter page URL', verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255, verbose_name='Instagram')),
                ('youtube', models.URLField(blank=True, help_text='Your YouTube channel or user account URL', verbose_name='YouTube')),
                ('linkedin', models.URLField(blank=True, help_text='Your LinkedIn page URL', verbose_name='LinkedIn')),
                ('googleplus', models.URLField(blank=True, help_text='Your Google+ page or Google business listing URL', verbose_name='Google')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='SeoSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_meta', models.BooleanField(default=True, help_text='Show an optimized preview when linking to this site on Facebook, Linkedin, Twitter, and others. See http://ogp.me/.', verbose_name='Use OpenGraph Markup')),
                ('twitter_meta', models.BooleanField(default=True, help_text='Shows content as a "card" when linking to this site on Twitter. See https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards.', verbose_name='Use Twitter Markup')),
                ('struct_meta', models.BooleanField(default=True, help_text='Optimizes information about your organization for search engines. See https://schema.org/.', verbose_name='Use Structured Data')),
                ('amp_pages', models.BooleanField(default=True, help_text='Generates an alternate AMP version of Article pages that are preferred by search engines. See https://www.ampproject.org/', verbose_name='Use AMP Pages')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'SEO',
            },
        ),
        migrations.CreateModel(
            name='MailchimpApiSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailchimp_api_key', models.CharField(blank=True, help_text='The API Key used for Mailchimp.', max_length=255, verbose_name='Mailchimp API Key')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Mailchimp API',
            },
        ),
        migrations.CreateModel(
            name='LayoutSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbar_color_scheme', models.CharField(blank=True, choices=[('navbar-light', 'Light - for use with a light-colored navbar'), ('navbar-dark', 'Dark - for use with a dark-colored navbar')], default='navbar-light', help_text='Optimizes text and other navbar elements for use with light or dark backgrounds.', max_length=50, verbose_name='Navbar color scheme')),
                ('navbar_class', models.CharField(blank=True, default='bg-light', help_text='Custom classes applied to navbar e.g. "bg-light", "bg-dark", "bg-primary".', max_length=255, verbose_name='Navbar CSS class')),
                ('navbar_fixed', models.BooleanField(default=False, help_text='Fixed navbar will remain at the top of the page when scrolling.', verbose_name='Fixed navbar')),
                ('navbar_wrapper_fluid', models.BooleanField(default=True, help_text='The navbar will fill edge to edge.', verbose_name='Full width navbar')),
                ('navbar_content_fluid', models.BooleanField(default=False, help_text='Content within the navbar will fill edge to edge.', verbose_name='Full width navbar contents')),
                ('navbar_collapse_mode', models.CharField(blank=True, choices=[('', 'Never show menu - Always collapse menu behind a button'), ('navbar-expand-sm', 'sm - Show on small screens (phone size) and larger'), ('navbar-expand-md', 'md - Show on medium screens (tablet size) and larger'), ('navbar-expand-lg', 'lg - Show on large screens (laptop size) and larger'), ('navbar-expand-xl', 'xl - Show on extra large screens (desktop, wide monitor)')], default='navbar-expand-lg', help_text='Control on what screen sizes to show and collapse the navbar menu links.', max_length=50, verbose_name='Collapse navbar menu')),
                ('navbar_format', models.CharField(blank=True, choices=[('', 'Default Bootstrap Navbar'), ('coral-navbar-center', 'Centered logo at top')], default='', max_length=50, verbose_name='Navbar format')),
                ('navbar_search', models.BooleanField(default=True, help_text='Show search box in navbar', verbose_name='Search box')),
                ('frontend_theme', models.CharField(blank=True, choices=[('', 'Default - Classic Bootstrap'), ('cerulean', 'Cerulean - A calm blue sky'), ('cosmo', 'Cosmo - An ode to Metro'), ('cyborg', 'Cyborg - Jet black and electric blue'), ('darkly', 'Darkly - Flatly in night mode'), ('flatly', 'Flatly - Flat and modern'), ('journal', 'Journal - Crisp like a new sheet of paper'), ('litera', 'Litera - The medium is the message'), ('lumen', 'Lumen - Light and shadow'), ('lux', 'Lux - A touch of class'), ('materia', 'Materia - Material is the metaphor'), ('minty', 'Minty - A fresh feel'), ('pulse', 'Pulse - A trace of purple'), ('sandstone', 'Sandstone - A touch of warmth'), ('simplex', 'Simplex - Mini and minimalist'), ('sketchy', 'Sketchy - A hand-drawn look for mockups and mirth'), ('slate', 'Slate - Shades of gunmetal gray'), ('solar', 'Solar - A dark spin on Solarized'), ('spacelab', 'Spacelab - Silvery and sleek'), ('superhero', 'Superhero - The brave and the blue'), ('united', 'United - Ubuntu orange and unique font'), ('yeti', 'Yeti - A friendly foundation')], default='', help_text='Change the color palette of your site with Bulma theme.', max_length=50, verbose_name='Theme variant')),
                ('favicon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favicon', to='wagtailimages.Image', verbose_name='Favicon')),
                ('logo', models.ForeignKey(blank=True, help_text='Brand logo used in the navbar and throughout the site', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Layout',
            },
        ),
        migrations.CreateModel(
            name='GoogleApiSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_maps_api_key', models.CharField(blank=True, help_text='The API Key used for Google Maps.', max_length=255, verbose_name='Google Maps API Key')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Google API',
            },
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email_address', models.CharField(blank=True, help_text='The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)', max_length=255, verbose_name='From email address')),
                ('search_num_results', models.PositiveIntegerField(default=10, verbose_name='Number of results per page')),
                ('external_new_tab', models.BooleanField(default=False, verbose_name='Open all external links in new tab')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'General',
            },
        ),
        migrations.CreateModel(
            name='AnalyticsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ga_tracking_id', models.CharField(blank=True, help_text='Your Google Analytics tracking ID (begins with "UA-")', max_length=255, verbose_name='GA Tracking ID')),
                ('ga_track_button_clicks', models.BooleanField(default=False, help_text='Track all button clicks using Google Analytics event tracking. Event tracking details can be specified in each button’s advanced settings options.', verbose_name='Track button clicks')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Tracking',
            },
        ),
        migrations.CreateModel(
            name='ADASettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skip_navigation', models.BooleanField(default=False, help_text='Shows a "Skip Navigation" link above the navbar that takes you directly to the main content.', verbose_name='Show skip navigation link')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Accessibility',
            },
        ),
    ]
