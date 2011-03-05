from django.contrib.admin.options import ModelAdmin, StackedInline, TabularInline

class ServeeModelAdmin(ModelAdmin):
    
    def __init__(self, *args, **kwargs):
        super(ServeeModelAdmin, self).__init__(*args, **kwargs)
        opts = self.model._meta
        app_label = opts.app_label
        
        self.change_form_template =  [
            "servee/%s/%s/change_form.html" % (app_label, opts.object_name.lower()),
            "servee/%s/change_form.html" % app_label,
            "servee/change_form.html",
            "admin/%s/%s/change_form.html" % (app_label, opts.object_name.lower()),
            "admin/%s/change_form.html" % app_label,
            "admin/change_form.html",
        ]
        self.add_form_template =  [
            "servee/%s/%s/add_form.html" % (app_label, opts.object_name.lower()),
            "servee/%s/add_form.html" % app_label,
            "admin/%s/%s/add_form.html" % (app_label, opts.object_name.lower()),
            "admin/%s/add_form.html" % app_label,
        ].append(self.change_form_template)
        self.change_list_template =  [
            "servee/%s/%s/change_list.html" % (app_label, opts.object_name.lower()),
            "servee/%s/change_list.html" % app_label,
            "servee/change_list.html",
            "admin/%s/%s/change_list.html" % (app_label, opts.object_name.lower()),
            "admin/%s/change_list.html" % app_label,
            "admin/change_list.html",
        ]
        self.delete_confirmation_template = [
            "servee/%s/%s/delete_confirmation.html" % (app_label, opts.object_name.lower()),
            "servee/%s/delete_confirmation.html" % app_label,
            "servee/delete_confirmation.html",
            "admin/%s/%s/delete_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_confirmation.html" % app_label,
            "admin/delete_confirmation.html",
        ]
        self.delete_selected_confirmation_template = [
            "servee/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "servee/%s/delete_selected_confirmation.html" % app_label,
            "servee/delete_selected_confirmation.html",
            "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_selected_confirmation.html" % app_label,
            "admin/delete_selected_confirmation.html",
        ]
        self.object_history_template = [
            "servee/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "servee/%s/object_history.html" % app_label,
            "servee/object_history.html",
            "admin/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "admin/%s/object_history.html" % app_label,
            "admin/object_history.html",
        ]

class ServeeStackedInline(StackedInline):
    template = 'servee/edit_inline/stacked.html'

class ServeeTabularInline(TabularInline):
    template = 'servee/edit_inline/tabular.html'