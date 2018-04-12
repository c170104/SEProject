from ChildCares.models import ChildCare, Price, Timing, Vacancy, Review
from django.db.models import Q
from django.utils.html import escape

class ChildCareController:    
    def get(self, sort):
        sort = escape(sort) if escape(sort) !=  '' else 'centre_code'
        return ChildCare.objects.all().order_by(sort)

    def search(self, query, sort, searchType="all"):
        query = escape(query)
        sort = escape(sort) if escape(sort) !=  '' else 'centre_code'
        if(searchType == "all"):
            return ChildCare.objects.filter(
                Q(centre_code__icontains=query)     |
                Q(centre_name__icontains=query)     |
                Q(centre_address__icontains=query)  |
                Q(centre_postal_code__icontains=query)
            ).order_by(sort)
        elif(searchType == "cc"):
            return ChildCare.objects.filter(centre_code=query).order_by(sort)
