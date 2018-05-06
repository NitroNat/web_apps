from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
'''
Here we have added the four one-to-many relationships:
The first is between Author and Category.
The second is between Author and Tag.
The third is between Post and Author.
The fourth is between Post and Category.
'''
# Create your models here.

# All models auto create a unique id key
class Author(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name="Author Name")
	email = models.EmailField(unique=True, blank=True)
	active = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	last_logged_in = models.DateTimeField(auto_now=True)
	
	def __str__(self):

		return (self.name + "-" + self.email)

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	
	class Meta:
		verbose_name_plural = "Categories"
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('post_by_category', args=[self.slug])

class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('post_by_tag', args=[self.slug])

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True,
		help_text="Slug will be generated automatically from the title of the post")
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	tags = models.ManyToManyField(Tag)
	
	def __str__(self):
		return self.title
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
		
	def get_absolute_url(self):
		return reverse('post_detail', args=[self.id, self.slug])