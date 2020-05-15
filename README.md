# Flower Shop Django Application

Created: 05-15-20 | Modified:
---

- Instructions to setup project for your machine [here](directions/boiler-setup.md)
- Requirements for this project [here](directions/requirements.md)

## Features

### List of bouquets
1. At the root URL of the application (`/`), a list of all the bouquets are shown in alphabetical order.

### Adding a bouquet
1. Above the list of bouquets, provide a link that presents the user with a form to add a new bouquet by providing the name and occasion. When the form is submitted, the user should be directed to `/` and should see the newly added bouquet in the list.

### Viewing bouquet details
1. Add a link to view the details of each bouquet for every item on the list of bouquets. When the user clicks on this link, they should see the name of the bouquet, the occasion, the names of the many flowers that make up that bouquet and the quantity of each flower needed for that bouquet.

### Deleting a flower from a bouquet
1. Add a DELETE button next to each flower listed on the details page for a bouquet. When the user clicks this button, the flower should be removed from that bouquet. **This action should not delete the flower itself!**

### Editing a bouquet
1. Add an EDIT button at the bottom of the bouquet details page. When the user clicks on the button, they should be presented with a form that lets them edit only the occasion of the bouquet. 
