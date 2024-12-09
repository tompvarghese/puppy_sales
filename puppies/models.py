from django.db import models

class Puppy(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    main_image = models.ImageField(upload_to='puppy_images/', blank=True, null=True)  # Main image (optional)
    
    # Many-to-many relation for additional images (optional)
    # additional_images = models.ManyToManyField('PuppyImage', blank=True)
    # main_image = models.ImageField(upload_to='puppy_images/')
    additional_images = models.ManyToManyField('PuppyImage', blank=True, related_name='puppies')
    # videos = models.ManyToManyField('PuppyVideo', related_name='puppies')    
    # Video (optional)
    video = models.FileField(upload_to='puppies/videos/', null=True, blank=True)  # Video field (optional)

    def __str__(self):
        return self.name


# Additional image model for storing multiple images
class PuppyImage(models.Model):
    # Change related_name to avoid conflict
    puppy = models.ForeignKey(Puppy, related_name='puppy_images_set', on_delete=models.CASCADE)  # Use a different related_name here
    image = models.ImageField(upload_to='puppies/images/')

    def __str__(self):
        return f"Image of {self.puppy.name}"
