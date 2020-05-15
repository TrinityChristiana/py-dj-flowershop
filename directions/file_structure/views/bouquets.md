# Views

## Bouquets List
- Function: [list_bouquets(request)]()
    - This view handles all request to the list of bouquet page
    - url_ex: /
    - GET: Shows list of all bouquets in abc order
    - POST: handles post method for add_bouquets. Redirects to bouquet list
    
## Bouquets Details
- Function: [details_bouquets(request, bouquet_id)]()
    - This view handels all request to the bouquets details page
    - url_ex: bouquet/1
    - GET: Gets and grabs details of each flower

## Bouquets Form
- Function: [add_bouquets(request)]()
    - This view handles all request to the add bouquets page
    - url_ex: bouquet/form
    - GET: Shows form to add new bouquet

- Function: [edit_bouquets(request, bouquet_id)]()
    - This view handles all request to the edit bouquet page
    - url_ex: bouquet/1/form
    - GET: