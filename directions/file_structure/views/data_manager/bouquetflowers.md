# BouquetFlowers Manager

## Get Related Relationships
- Function: [get_relations(bouquet_id)](../../../../bouquetapp/views/data_manager/bouquetflowers/get_relations.py)
    - Grabs the relationships in the database that has the passed in bboquet id
    - Uses the BouquetFlower model to represent data
    - => List BouquetFlower classes

## Remove Relationship
- Function: [remove_relation(bouquet_flower_id)](../../../../bouquetapp/views/data_manager/bouquetflowers/remove_relation.py)
    - Deletes bouquetapp_bouquetflower relationship at passed in id
    - => None