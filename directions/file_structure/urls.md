# URL Paths

## Home Page 
- Path: "/"
- Shows: List of Bouquets
- View: [list_bouquets](../../bouquetapp/views/bouquets/bouquets_list.py#L4)
- Name: bouquets

## Bouquets Details
- Path: "bouquet/\<int:bouquet_id>"
- Shows: Name, Occasion, Flowers, Edit Button, Remove Flowers Button.
- View: [details_bouquets](../../bouquetapp/views/bouquets/bouquets_details.py#L4)
- Name: bouquet

## Add Bouquets
- Path: "bouquet/form"
- Shows: Form with name and occasion inputs
- View: [add_bouquets](../../bouquetapp/views/bouquets/bouquets_form.py#L4)
- Name: bouquet_form

## Edit Bouquets 
- Path: "bouquet/\<int:bouquet_id>/form"
- Shows: Form with occasion input
- View: [edit_bouquets](../../bouquetapp/views/bouquets/bouquets_form.py#L15)
- Name: bouquet_edit

## Delete Flower from Bouquet
- Path: "bouquetflower/\<int:bouquet_id>/\<int:bouquets_flower_id>"
- Shows: Form with occasion input
- View: [details_bouquets_flower](../../bouquetapp/views/bouquet_flower/bouquets_flower_details.py#L4)
- Name: bouquetflower