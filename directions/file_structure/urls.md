# URL Paths

## Home Page 
- Path: "/"
- Shows: List of Bouquets
- View: [list_bouquets]()
- Name: bouquets

## Bouquets Details
- Path: "bouquet/<int:bouquet_id>"
<!-- - Shows:  -->
- View: [details_bouquets]()
- Name: bouquet

## Add Bouquets
- Path: "bouquet/form"
<!-- - Shows:  -->
- View: [add_bouquets]()
- Name: bouquet_form

## Edit Bouquets 
- Path: "bouquet/<int:bouquet_id>/form"
<!-- - Shows:  -->
- View: [edit_bouquets]()
- Name: bouquet_edit
