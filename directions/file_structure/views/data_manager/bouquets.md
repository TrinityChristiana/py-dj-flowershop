# Bouquets Manager

## Add Bouquet
- Function: [add_bouquet(form_data)]()
    - Takes in form data
    - Runs INSERT sql query to add new bouquet to database,
    - needs form_data["name"], form_data["occasion"]
    - => id of created bouquet
    
## Get all Bouquets
- Function: [get_all_bouquets()]()
    - Grabs all of the bouquets in the database
    - Uses the Bouquet model to represent data
    - Sql query grabs all bouquets in order alphabetically
    - => list of Bouquet classes
    
## Get single Bouquet 
- Function: [get_bouquet(bouquet_id)]()
    - Grabs the bouquet in the database that matches the passes bouquet id
    - Uses the Bouquet model to represent data
    - => Single Bouquet classes
    
## Update Bouquet

