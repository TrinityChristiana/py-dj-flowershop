# Bouquets Manager

## Add Bouquet
- Function: [add_bouquet(form_data)]()
    - Takes in form data
    - Runs INSERT sql query to add new bouquet to database,
    - needs form_data["name"], form_data["occasion"]
    - => id of created bouquet
    
## Get all Bouquets
- Function: [get_all_bouquets()]()
    - Runs SELECT * sql query to grab all of the bouquets in the database
    - Uses the Bouquet model to represent data
    - Sql query grabs all bouquets in order alphabetically
    - => list of Bouquet classes
    
## Get single Bouquet 
- Function: [get_bouquet(bouquet_id)]()
    - Runs SELECT * sql query to grab the bouquet in the database that matches the passes bouquet id
    - Uses the Bouquet model to represent data
    - => Single Bouquet classes
    
## Update Bouquet
- Function: [update_bouquet(form_data, bouquet_id)]()
    - Runs UPDATE sql query on passed in bouquet_id using the passed in form_data information as values
    - needs form_data["occasion"]
    - => NONE
    
