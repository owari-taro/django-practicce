from django.urls import path
from accounts.views import top,edit,Delete,csv_export,inquiry,create_user,reset

urlpatterns=[
   path("",top,name="accounts_top"),
   path("create",create_user,name="accounts_create"),
   path("edit/<int:user_id>",edit,name="accounts_edit"),
   path("delete/<int:pk>",Delete.as_view(),name="delete"),
   path("csv",csv_export,name="accounts_csv"),
   path("inquiry",inquiry,name="accounts_inquiry"),
   path("reset/<int:user_id>",reset,name="accounts_reset"),

   #path("message",csv_export,name="accounts_password_reset"),


]