# Models

## Bouquet_Flower **Intermediary Table**
- Model: [BouquetFlower]()
```
flower = models.ForeignKey("Flower", on_delete=models.CASCADE)
bouquet = models.ForeignKey("Bouquet", on_delete=models.CASCADE)
quantity = models.IntegerField()
```

## Bouquet
- Model: [Bouquet]()
- \_\_str\_\_: "name (occasion)"
```
name = models.CharField(max_length=100)
occasion = models.CharField(max_length=100)
flowers = models.ManyToManyField("Flower", through='BouquetFlower')
```

## Flower
- Model: [Flower]()
- \_\_str\_\_: "name (binomial_name)"
```
name = models.CharField(max_length=100)
    binomial_name = models.CharField(max_length=100)
    longevity_in_days = models.IntegerField()
    bouquets = models.ManyToManyField("Bouquet", through='BouquetFlower')
```

## Model Factory
- Function: [model_factory(model_type)]()
- Details: Takes in Model and iterates over it to create data representation in sql execution. 
- `conn.row_factory = model_factory(Model)`