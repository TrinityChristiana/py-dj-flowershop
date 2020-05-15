# Flower Shop Django Application

Created: 05-15-20 | Modified:
---

- Instructions to setup project for your machine [here](directions/boiler-setup.md)
- Requirements for this project [here](directions/requirements.md)

## Features

### View List of Bouquet
1. At the root URL of the application (`/`), a list of all the bouquets are shown in alphabetical order.

### Adding a Bouquet
1. Above the list of bouquets, there's a link to "Add a Bouquet" that presents a form to add a new bouquet by providing the name and occasion. When the form is submitted, the user is directed to `/` and can now see the newly added bouquet in the list.

### Viewing Bouquet Details
1.Each bouquet on the lsit page has a link to view the details of the bouquet. When the user clicks on this link, they can view the name of the bouquet, the occasion, the names of the many flowers that make up that bouquet and the quantity of each flower needed for that bouquet.

### Editing a Bouquet
1. Using the edit button at the bottom of the bouquet details page. When the user clicks on the button, they are presented with a form that lets them edit only the occasion of the bouquet. 


<!-- ### Deleting a Flower from a Bouquet
1. Add a DELETE button next to each flower listed on the details page for a bouquet. When the user clicks this button, the flower should be removed from that bouquet. **This action should not delete the flower itself!** -->