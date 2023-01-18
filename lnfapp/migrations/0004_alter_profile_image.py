# Generated by Django 4.1.5 on 2023-01-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lnfapp', '0003_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH8AAAB/CAMAAADxY+0hAAAAY1BMVEX///8WFhbu7u4AAAB5eXn8/Pz5+fne3t4ODg719fXy8vIKCgoTExPp6ekGBga6uro6OjpISEienp6Hh4fJycmtra3CwsKWlpbS0tIzMzNhYWEuLi6kpKQbGxtVVVU/Pz9vb29yJLQAAAACqElEQVRoge3bW3OqQAwAYNggLIIIeEME7P//lYe1WqvuYhIFp2eSl3b6wLfsJSQ7Uy9Sn4zIU94nQ4kvvvjiiy+++OKLL7744osv/rMIq03TNNvFR/zZsoNzHEr2ENj+NgdI/e/Q0O7mk/pxAIn/K1Ioogn9uAD/LjJYT+bPjg+8mYJqKj+w8P0u0Iw9wPGXVt73IZjED4+J3fcZK8DwXa/f+/UUfpG5/LQlH0K6r/zU5fuwHN9fO6efswPp/mbAz4rx/XLA1/v/328G/OQ4vu8+/pwEQPejZOD8leP73kG7fXICZvg75wIkRTiBHzkTIDTUZ7G+vyvHBOh9PIkf7+0fYE4Fxqp/KrBtQdjRn8SsP5eWAXCqH3b9vYW7PaBhxXkOu/9QNWTXY5DAgVV9v9J/VXUGkGid9A1YUc6YT3ml/4w2X0WeH+uyop+7d/jviBf8+SK6BL8D5/nz9a5r0+TSf2faz4MlqwHl+NGq772z9CY0QFuvyZ8fhr8IwJr++gYUuu3ofnO9dniMDGpiD0ryZ96iG9BPWTihJSLa+1f7geLvkohJRQDJj9qnvNkGpYfPhhRfta7G+24NCF0gwQ9tty72AeDLUILvKrseQ+foU4D31092/s0EoIsBvJ/jFv8UKWCTMdofarssE4BtxNC+89LptQnA+hHp9fHFMNZ3N1320Ie3+mFHmn4zAbiaBOkrwuE7+5t3+tTlR6cApE87fSf/653+0KWTPZIOVYwhfXzu//FxdxFIvwFydKgiAOnHu4AauAT4h/sf8cUXX3zxxRdffPGn82eXCH9+m8T/Nk3E8fwacR/mj/SBMHxjG1wt+jCX730oZUbBGAF1/k9T/uv91Uk2M2Dw8f3zGM7rcPuTswf+6P4XX3zxxRdf/D/uf/j/3/8B/CkfcRXTRGcAAAAASUVORK5CYII='),
        ),
    ]
