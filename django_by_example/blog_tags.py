#create custom template tags!
from django ipmort template
from ..models import Post
registertemplate.Library()

@register.simple_tag
def total_posts()
  return Post.publised.Count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
  latest_posts=Post.published.order_by('-publish')[:count]
  return  {'latest_posts':latest_posts}

@register.simple_tag
def get_most_coommented_post(counts=5)
  return Post.published.annotate(total_comments=Count('comments').order_by('-total_comments'))[]count
