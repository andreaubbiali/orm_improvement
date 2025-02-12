from django.db import models

class ProductType(models.Model):

    def __init__(self, type=None, description=None, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent constructor
        self.type = type
        self.description = description
    
    type = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    # TODO
    #  optimistic/pessimistic locking
    #  https://www.linkedin.com/pulse/pessimitic-locking-optimistic-django-managing-ho%C3%A0ng-b%C3%B9i-minh-zf6pc/
    # https://django-concurrency.readthedocs.io/en/latest/
    # https://medium.com/@uday12kumar/handling-concurrency-django-way-c65b89a6565d


    """ 
     cosa succede in una nuova app, anche springboot, quando crei un nuovo modello? 
     la gestione della concorrenza è automatica oppure devi aggiungere della configurazione come in Resevo?
     esiste in django una qualche modalità semplice per gestire la concorreenza?
     perchè in resevo c'è la questione dei optimistic lock mentre in tutte le altre applicazioni che ho visto (in sorint) non ho mai avuto tale problema?

     django transaction:
     https://docs.djangoproject.com/en/5.1/topics/db/transactions/


     leggere:
     https://www.baeldung.com/spring-data-jpa-dynamicupdate
       """