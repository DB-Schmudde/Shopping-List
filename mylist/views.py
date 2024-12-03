from django.shortcuts import render
from .models import ShoppingItem

def mylist(request):
    all_items = ShoppingItem.objects.all()  # Fetch all items regardless of request method

    if request.method == 'POST':
        item_name = request.POST.get('itemName', '')  # Get item name from POST data
        if item_name:
            try:
                ShoppingItem.objects.create(name=item_name)  # Create new ShoppingItem
                # Optionally, you can add more logic here (e.g., success message)
            except Exception as e:
                print('Error creating item:', e)
        
        # Refresh all_items after adding a new item
        all_items = ShoppingItem.objects.all()

    return render(request, 'shopping_list.html', {'all_items': all_items})
