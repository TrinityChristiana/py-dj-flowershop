# Views

## Bouquets List
- Function: [list_bouquets(request)]()
    - This view handles all request to the list of bouquet page
    - url_ex: /
    
## Bouquets Details
- Function: [details_bouquets(request, bouquet_id)]()
    - This view handels all request to the bouquets details page
    - url_ex: bouquet/1

## Bouquets Form
- Function: [add_bouquets(request)]()
    - This view handles all request to the add bouquets page
    - url_ex: bouquet/form
- Function: [edit_bouquets(request, bouquet_id)]()
    - This view handles all request to the edit bouquet page
    - url_ex: bouquet/1/form