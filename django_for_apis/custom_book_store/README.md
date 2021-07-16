## memo
・ForiegnKey uniqueの時の挙動
└onetooneと同じ？
onettooneと同じ。book1.commentをbook2.commentに結びつけようとすると
book1.commentがNoneになってbook2.commentだけに結びつくようになる！




・Forienkeyを指定した時テーブル構成
forienkeyを競って下側のテーブルにbook_idというキーが自動が作られる１

## check
```
python manage.py shell
from books.models import *
>>> from books.models import *

>>> books=Book.objects.all()  
>>> book1=books[1]
>>> book2=books[2]

>>> book2.comments.set([book1.comments.get()])  
>>> book2.save()
save method
<class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>    
1
>>> exit()

```
 


```
import sqlite3
con=sqlite3.connect("db.sqlite3")
con.row_factory = dict_factory
cur=con.cursor()
cur.execute("select * from sqlite_master where type='table'")
```

select * from sqlite_master;








), ('index', 'sqlite_autoindex_auth_user_1', 'auth_user', 8, None), 

('table', 'books_book', 'books_book', 10, 'CREATE TABLE "books_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "author" varchar(200) NOT NULL, "title" varchar(200) NOT NULL, "is_special" bool NOT NULL)'), ('table', 'books_publisher', 'books_publisher', 11, 'CREATE TABLE "books_publisher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL)'),


 ('table', 'django_session', 'django_session', 35, 'CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL)'), ('index', 'sqlite_autoindex_django_session_1', 'django_session', 36, None), ('index', 'django_session_expire_date_a5c62663', 'django_session', 37, 'CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date")'), ('table', 'books_comment', 'books_comment', 38, 'CREATE TABLE "books_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "book_id" integer NOT NULL UNIQUE REFERENCES "books_book" ("id") DEFERRABLE INITIALLY DEFERRED)'), ('index', 'sqlite_autoindex_books_comment_1', 'books_comment', 39, None), ('index', 'books_comment_author_id_2f3e73d3', 'books_comment', 32, 'CREATE INDEX "books_comment_author_id_2f3e73d3" ON "books_comment" ("author_id")')]





('table', 'django_migrations', 'django_migrations', 2, 'CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL)'), ('table', 'sqlite_sequence', 'sqlite_sequence', 3, 'CREATE TABLE sqlite_sequence(name,seq)'), ('table', 'auth_group_permissions', 'auth_group_permissions', 9, 'CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY 
AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED)'), ('table', 'auth_user_groups', 'auth_user_groups', 12, 'CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED)'), ('table', 'auth_user_user_permissions', 'auth_user_user_permissions', 13, 'CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED)'), ('table', 'django_admin_log', 'django_admin_log', 29, 'CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime 
NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0))'), ('table', 'django_content_type', 'django_content_type', 5, 'CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL)'), ('table', 'auth_permission', 'auth_permission', 30, 'CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL)'), ('table', 'auth_group', 'auth_group', 15, 'CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE)'), 
('table', 'auth_user', 'auth_user', 7, 'CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL)'),

 ('table', 'books_book', 'books_book', 10, 'CREATE TABLE "books_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "author" varchar(200) 
NOT NULL, "title" varchar(200) NOT NULL, "is_special" bool NOT NULL)'), ('table', 'books_publisher', 'books_publisher', 11, 'CREATE TABLE "books_publisher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL)'),
 ('table', 'books_comment', 'books_comment', 32, 'CREATE TABLE "books_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" varchar(200) NOT NULL, 
"created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" 
("id") DEFERRABLE INITIALLY DEFERRED,
 "book_id" integer NOT NULL REFERENCES "books_book" ("id") DEFERRABLE INITIALLY DEFERRED)'), ('table', 'django_session', 'django_session', 35, 'CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL)')]
>>> cur.execute("select