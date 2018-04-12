from ChildCares.models import ChildCare

class ChildCareController:
    def __init__(self):
        print("test")
        
    def get(self):
        return ChildCare.objects.all().order_by('centre_code')

    def search(self, query):
        print(query)
        return ChildCare.objects.filter(
            centre_code__icontains=query
        ).filter(centre_name__icontains=query)
        
        # ).filter(
        #     centre_address__icontains=query
        # ).filter(
        #     centre_postal_code__icontains=query
        # )
