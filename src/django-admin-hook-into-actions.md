Title: Django admin: Hook into actions
Tags: django, python
Date: 2012-06-18

I want to do something before actions was executed. For example when admin 
deleting users using 'Delete selected' dropdown in admin panel, I want to run 
some commands in backend system to remove info about that user in a config 
file. If the commands somehow failed, I want to abort the operation so the user 
can't be deleted. Signals won't work here since there's no way to abort the 
request gracefully (other than raising exception and causing the 500 error page 
displayed). Using transaction also wouldn't work since there might be more 
users deleted in single actions and I only want the user that failed get 
aborted, not the whole users selected.

Django allow us to define custom actions in admin, it quite simple but I don't 
want to reimplement what `delete_selected` already doing. The idea is just hook 
before the action function get called and do my stuff. The first part is 
overriding the actions:

    :::python
    class MyModelAdmin(admin.ModelAdmin):
        actions = ['delete_selected',]

        def delete_selected(self, request, queryset):
            pass

This seem to work. When you define action name similar to what already defined 
in `django.contrib.admin`, yours will be used. (TODO: Check if order in 
`INSTALLED_APPS` matters). The next thing to do is to wrap your logic before 
calling actual `delete_selected` function. I have implemented my 
`delete_selected` as:-

    :::python
    from django.contrib.admin.actions import delete_selected

    class MyModelAdmin(admin.ModelAdmin):
        actions = ['delete_selected',]

        def delete_selected(self, request, queryset):
            if not request.POST.get('post'):
                return delete_selected(self, request, queryset)

            if request.POST.get('post'):
                for user in queryset:
                    status = backend.some_command(user)
                    if not status:
                        self.message_user(request, 'Fail to update user')
                        break
                else:
                    delete_selected(self, request, queryset)
        delete_selected.short_description = 'Delete selected'

My code just iterate through the selected users and run backend command on 
them, if the command success it will go through the next user. If the loop 
terminate normally, the else clause will be executed, calling the real 
`delete_selected` function. If somehow the backend function failed, the loop 
`break` and the else clause will never been executed. Here I'd also finally 
found some use case for [python's `for ... else`][1] construct.

Initially I named my `delete_selected` as `custom_delete_selected` and then 
remove the real `delete_selected` by overriding ModelAdmin's `get_actions()` 
method but there's a problem with that. When user submit to delete the selected 
users, a confirmation page is displayed. Only when admin submit the 
confirmation page the function start deleting the user. To facilitate the 
confirmation, it use form validition to make sure the action name 
('delete_selected') exists in the POST data. If we use our 
`custom_delete_selected` as the action then 'delete_selected' not present in 
the POST data and the validation fail, the function will not be executed.


[1]:http://psung.blogspot.com/2007/12/for-else-in-python.html
