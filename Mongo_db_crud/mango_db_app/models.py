from django.db import models

class PlacementDetails(models.Model):


    work_order_no = models.CharField(primary_key=True,max_length=100)
    client = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'placement_details'

