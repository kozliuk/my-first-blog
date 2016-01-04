from django.forms import ModelForm
from posts.models import Posts

class PostsForm(ModelForm):
	class Meta:
		model = Posts
		fields = ['title','text','author']