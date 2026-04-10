from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("detection", "0002_userstatistics_useractivity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diseasedetection",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="detections/"),
        ),
    ]

