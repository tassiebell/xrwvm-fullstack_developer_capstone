from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class


class CarModelInline(admin.TabularInline):
    model = CarModel
    # Number of empty forms to display for adding new CarModel instances
    extra = 1

# CarModelAdmin class


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    # Allows searching by car make name
    search_fields = ('name', 'car_make__name')
    ordering = ('car_make', 'name')

    # Customize the form fields displayed when adding/editing a CarModel
    fieldsets = (
        ('Car Details', {
            'fields': ('name', 'car_make', 'type', 'year')
        }),
        # Add other fieldsets as needed
    )

    # Customize the display of related CarMake in the CarModel change form
    raw_id_fields = ('car_make',)

    def get_queryset(self, request):
        # Optimize queryset to select related CarMake for performance
        return super().get_queryset(request).select_related('car_make')

# CarMakeAdmin class with CarModelInline


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]

# Register models here
# admin.site.register(CarMake)
# admin.site.register(CarModel)
