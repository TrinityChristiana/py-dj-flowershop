# Bouquet Templates

## List Of Bouquets
- Template: [bouquets_list]()
- Template for List of Bouquets page
- Has link to add bouquet
- Each Boquet has a link to their details page
- Takes in list of Bouquet Models

## Bouquets Details
- Template: [bouquets_details]()
- Template for Bouquets Details page
- Takes in single Bouquet Model and list of BouquetFlower Models
- Displays Bouquet Name, Occasion, List of flowers, their name and quantity in the Bouquet, and a button to edit Bouquet

## Bouquets Form
- Template: [bouquets_form]() 
- Template for add and edit Bouquets form page
- Add Bouquet: Form takes in user text input for name and occasion 
    - Action: 'bouquetapp:bouquets'
- Edit Bouquet: Form takes in user text input for occasion
    - Action: 'bouquetapp:bouquet' bouquet.id

