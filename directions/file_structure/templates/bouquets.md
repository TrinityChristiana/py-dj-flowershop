# Bouquet Templates Documentation

## List Of Bouquets
- Template: [bouquets_list](../../../bouquetapp/templates/bouquets/bouquets_list.html)
- Template for List of Bouquets page
- Has link to add bouquet
- Each Boquet has a link to their details page
- Takes in list of Bouquet Models

## Bouquets Details
- Template: [bouquets_details](../../../bouquetapp/templates/bouquets/bouquets_details.html)
- Template for Bouquets Details page
- Takes in single Bouquet Model and list of BouquetFlower Models
- Displays Bouquet Name, Occasion, List of flowers, their name and quantity in the Bouquet, delete button to remove flower from a bouquet, and a button to edit Bouquet

## Bouquets Form
- Template: [bouquets_form](../../../bouquetapp/templates/bouquets/bouquets_form.html) 
- Template for add and edit Bouquets form page
- Add Bouquet: Form takes in user text input for name and occasion 
    - Action: 'bouquetapp:bouquets'
- Edit Bouquet: Form takes in user text input for occasion
    - Action: 'bouquetapp:bouquet' bouquet.id

