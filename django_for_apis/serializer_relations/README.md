## stringrelatedfield
```
#see example.py for 
>>> from  example.serializer import AlbumSerializer
>>> from example.models import Album
>>>
>>> album=Album.objects.all()
>>> seri=AlbumSerializer(album[1])
>>> print(seri.data)
{'album_name': 'sundaysongbook', 'artist': 'yamashita', 'tracks': ['1: ヘロン', '2: 明日への扉', '3: jody']}
>>> album[1].tracks.all()
<QuerySet [<Track: 1: ヘロン>, <Track: 2: 明日への扉>, <Track: 3: jody>]>

```


## primarykey
only return primarykey
```
>>> from  example.serializer import AlbumSerializer
>>> from example.models import Album
>>>
>>> album=Album.objects.all()
>>> seri=AlbumSerializer(album[1])
>>> print(seri.data)
{'album_name': 'sundaysongbook', 'artist': 'yamashita', 'tracks': [1, 2, 3]}
>>> album[1].tracks.all()
<QuerySet [<Track: 1: ヘロン>, <Track: 2: 明日への扉>, <Track: 3: jody>]>
>>>
>>> 
'''