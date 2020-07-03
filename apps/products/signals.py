# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

from django.utils.text import slugify


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


def delete_image_post_delete_receiver(sender, instance, *args, **kwargs):
    # Delete image from media folder...
    # ...When product has been deleted.
    if instance.image:
        _delete_file(instance.image.path)
        # print(instance.image.path)


def delete_old_image_pre_save_receiver(sender, instance, *args, **kwargs):
    # Delete old image from media folder...
    # ...When product image has been updated.
    if not instance.id:
        return False
    else:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
            # print(old_image)
        except sender.DoesNotExist:
            return False
        
        new_image = instance.image
        # print(new_image)

        if old_image != new_image:
            _delete_file(old_image.path)


def generate_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    # Generate auto product slug...
    # ...When product has been created or...
    # ...When product name has been updated
    if not instance.id:
        instance.slug = slugify(instance.name)
    else:
        try:
            old_slug = sender.objects.get(pk=instance.pk).slug
            # print('old slug: ' + old_slug)
        except sender.DoesNotExist:
            return False
        
        new_slug = slugify(instance.name)
        # print('new slug: ' + new_slug)

        if old_slug != new_slug:
            instance.slug = new_slug
            # print(instance.slug)


# Resources:
# Source1: https://stackoverflow.com/questions/16041232/django-delete-filefield
# Source2: https://stackoverflow.com/questions/33080360/how-to-delete-files-from-filesystem-using-post-delete-django-1-8
