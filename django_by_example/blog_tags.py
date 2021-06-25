#create custom template tags!
from django ipmort template
from ..models import Post
registertemplate.Library()

@register.simple_tag
def total_posts()
  return Post.publised.Count()
