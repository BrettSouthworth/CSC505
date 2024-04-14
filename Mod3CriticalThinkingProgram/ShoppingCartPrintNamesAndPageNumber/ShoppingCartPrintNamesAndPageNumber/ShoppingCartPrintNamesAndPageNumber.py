class view:
    def __init__(self, viewName, viewPageNumber):
        self.viewName = viewName
        self.viewPageNumber = viewPageNumber
        
class shoppingCenter:
    def __init__(self):
        self.views = []
    
    def addView(self, viewName, viewPageNumber):
        self.views.append(view(viewName, viewPageNumber))
        
    def prettyPrint(self):
        print("Available Views: ")
        for i, view in enumerate(self.views, start=1):
            print(f"Name: {view.viewName}, PageNumber: {view.viewPageNumber}")


center = shoppingCenter()

# TODO: Have this load in from a configuration file
center.addView("ShoppingListView", 1)
center.addView("CartView", 2)
center.addView("NavigationModalWindow", 3)

# TODO: Load data from DB / data source and push to ShoppingListView

center.prettyPrint()
