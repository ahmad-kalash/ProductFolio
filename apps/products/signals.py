import os

from django.db.models.signals import post_delete, pre_save


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
    # ...When product has been updated.
    if not instance.id:
        return False
    else:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
            print(old_image)
        except sender.DoesNotExist:
            return False
        
        new_image = instance.image
        print(new_image)

        if old_image != new_image:
            _delete_file(old_image.path)


# Resources:
# Source1: https://stackoverflow.com/questions/16041232/django-delete-filefield
# Source2: https://stackoverflow.com/questions/33080360/how-to-delete-files-from-filesystem-using-post-delete-django-1-8
