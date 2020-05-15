# Bouquetapp Views

## Bouquets List
- Function: [list_bouquets(request)](../../../bouquetapp/views/bouquets/bouquets_list.py#L4)
    - This view handles all request to the list of bouquet page
    - url_ex: /
    - GET: Shows list of all bouquets in abc order
    - POST: handles post method for add_bouquets. Redirects to bouquet list
    
## Bouquets Details
- Function: [details_bouquets(request, bouquet_id)]((../../../bouquetapp/views/bouquets/bouquets_details.py#L4)
    - This view handels all request to the bouquets details page
    - url_ex: bouquet/1
    - GET: Gets and grabs details of each flower
    - POST: handles post method for edit_bouquet. Redirects to bouquet details

## Bouquets Form
- Function: [add_bouquets(request)](../../../bouquetapp/views/bouquets/bouquets_form.py#L4)
    - This view handles all request to the add bouquets page
    - url_ex: bouquet/form
    - GET: Shows form to add new bouquet

- Function: [edit_bouquets(request, bouquet_id)](../../../bouquetapp/views/bouquets/bouquets_form.py#L15)
    - This view handles all request to the edit bouquet page
    - url_ex: bouquet/1/form
    - GET: Shows form to edit bouquet

## Bouquet_Flower Details
- Function: [details_bouquets_flower(request, bouquets_flower_id, bouquet_id)](../../../bouquetapp/views/bouquet_flower/bouquets_flower_details.py#L4)
    - This view handels only POST request for bouquets_flower
    - url_ex: bouquetflower/1/1
    - POST: Deleted bouquet/flower relationship