import os
from qgis.core import (
     QgsVectorLayer
)

boundary_protected_area_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Sardegna.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Sardegna,"protected area Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

boundary_protected_area_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Abruzzo.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Abruzzo,"protected area Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Basilicata.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Basilicata,"protected area Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Calabria.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Calabria,"protected area Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Campania.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Campania,"protected area Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Emilia.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Emilia_Romagna,"protected area Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Friuli.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Friuli_Venezia_Giulia,"protected area Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Lazio.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Lazio,"protected area Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Liguria.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Liguria,"protected area Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Lombardia.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Lombardia,"protected area Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Marche.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Marche,"protected area Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Molise.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Molise,"protected area Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Piemonte.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Piemonte,"protected area Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Puglia.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Puglia,"protected area Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Sicilia.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Sicilia,"protected area Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Toscana.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Toscana,"protected area Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Trentino.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Trentino_Alto_Adige,"protected area Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Umbria.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Umbria,"protected area Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Valle_d_Aosta,"protected area Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/prot_Veneto.shp"
vlayer = QgsVectorLayer(boundary_protected_area_Veneto,"protected area Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Veneto.shp"
vlayer = QgsVectorLayer(power_plant_Veneto,"plant Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

power_plant_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Trentino.shp"
vlayer = QgsVectorLayer(power_plant_Trentino_Alto_Adige,"plant Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Toscana.shp"
vlayer = QgsVectorLayer(power_plant_Toscana,"plant Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Sicilia.shp"
vlayer = QgsVectorLayer(power_plant_Sicilia,"plant Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Puglia.shp"
vlayer = QgsVectorLayer(power_plant_Puglia,"plant Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Piemonte.shp"
vlayer = QgsVectorLayer(power_plant_Piemonte,"plant Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Marche.shp"
vlayer = QgsVectorLayer(power_plant_Marche,"plant Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Lombardia.shp"
vlayer = QgsVectorLayer(power_plant_Lombardia,"plant Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Lazio.shp"
vlayer = QgsVectorLayer(power_plant_Lazio,"plant Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Friuli.shp"
vlayer = QgsVectorLayer(power_plant_Friuli_Venezia_Giulia,"plant Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Emilia.shp"
vlayer = QgsVectorLayer(power_plant_Emilia_Romagna,"plant Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Calabria.shp"
vlayer = QgsVectorLayer(power_plant_Calabria,"plant Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/plant_Abruzzo.shp"
vlayer = QgsVectorLayer(power_plant_Abruzzo,"plant Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Veneto.shp"
vlayer = QgsVectorLayer(landuse_industrial_Veneto,"industrial Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(landuse_industrial_Valle_d_Aosta,"industrial Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Umbria.shp"
vlayer = QgsVectorLayer(landuse_industrial_Umbria,"industrial Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Trentino.shp"
vlayer = QgsVectorLayer(landuse_industrial_Trentino_Alto_Adige,"industrial Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Toscana.shp"
vlayer = QgsVectorLayer(landuse_industrial_Toscana,"industrial Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Sicilia.shp"
vlayer = QgsVectorLayer(landuse_industrial_Sicilia,"industrial Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Sardegna.shp"
vlayer = QgsVectorLayer(landuse_industrial_Sardegna,"industrial Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Puglia.shp"
vlayer = QgsVectorLayer(landuse_industrial_Puglia,"industrial Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Piemonte.shp"
vlayer = QgsVectorLayer(landuse_industrial_Piemonte,"industrial Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Molise.shp"
vlayer = QgsVectorLayer(landuse_industrial_Molise,"industrial Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Marche.shp"
vlayer = QgsVectorLayer(landuse_industrial_Marche,"industrial Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Lombardia.shp"
vlayer = QgsVectorLayer(landuse_industrial_Lombardia,"industrial Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Liguria.shp"
vlayer = QgsVectorLayer(landuse_industrial_Liguria,"industrial Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Lazio.shp"
vlayer = QgsVectorLayer(landuse_industrial_Lazio,"industrial Lazio","ogr")
if not vlayer.isValid():
     print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Friuli.shp"
vlayer = QgsVectorLayer(landuse_industrial_Friuli_Venezia_Giulia,"industrial Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Emilia.shp"
vlayer = QgsVectorLayer(landuse_industrial_Emilia_Romagna,"industrial Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Campania.shp"
vlayer = QgsVectorLayer(landuse_industrial_Campania,"industrial Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Calabria= "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Calabria.shp"
vlayer = QgsVectorLayer(landuse_industrial_Calabria,"industrial Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Basilicata.shp"
vlayer = QgsVectorLayer(landuse_industrial_Basilicata,"industrial Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/ind_Abruzzo.shp"
vlayer = QgsVectorLayer(landuse_industrial_Abruzzo,"industrial Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Veneto.shp"
vlayer = QgsVectorLayer(landuse_commercial_Veneto,"commercial Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Umbria.shp"
vlayer = QgsVectorLayer(landuse_commercial_Umbria,"commercial Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Trentino.shp"
vlayer = QgsVectorLayer(landuse_commercial_Trentino_Alto_Adige,"commercial Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Toscana.shp"
vlayer = QgsVectorLayer(landuse_commercial_Toscana,"commercial Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Sicilia.shp"
vlayer = QgsVectorLayer(landuse_commercial_Sicilia,"commercial Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_commercial_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Sardegna.shp"
vlayer = QgsVectorLayer(landuse_commercial_Sardegna,"commercial Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Piemonte.shp"
vlayer = QgsVectorLayer(landuse_commercial_Piemonte,"commercial Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Molise.shp"
vlayer = QgsVectorLayer(landuse_commercial_Molise,"commercial Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Marche.shp"
vlayer = QgsVectorLayer(landuse_commercial_Marche,"commercial Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Lombardia.shp"
vlayer = QgsVectorLayer(landuse_commercial_Lombardia,"commercial Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Liguria.shp"
vlayer = QgsVectorLayer(landuse_commercial_Liguria,"commercial Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Lazio.shp"
vlayer = QgsVectorLayer(landuse_commercial_Lazio,"commercial Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Friuli.shp"
vlayer = QgsVectorLayer(landuse_commercial_Friuli_Venezia_Giulia ,"commercial Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Emilia.shp"
vlayer = QgsVectorLayer(landuse_commercial_Emilia_Romagna,"commercial Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Campania.shp"
vlayer = QgsVectorLayer(landuse_commercial_Campania,"commercial Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Calabria.shp"
vlayer = QgsVectorLayer(landuse_commercial_Calabria,"commercial Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Basilicata.shp"
vlayer = QgsVectorLayer(landuse_commercial_Basilicata,"commercial Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Abruzzo.shp"
vlayer = QgsVectorLayer(landuse_commercial_Abruzzo,"commercial Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_retail_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Veneto.shp"
vlayer = QgsVectorLayer(landuse_retail_Veneto,"retail Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Umbria.shp"
vlayer = QgsVectorLayer(landuse_retail_Umbria,"retail Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_retail_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Trentino.shp"
vlayer = QgsVectorLayer(landuse_retail_Trentino_Alto_Adige,"retail Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Toscana.shp"
vlayer = QgsVectorLayer(landuse_retail_Toscana,"retail Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Sicilia.shp"
vlayer = QgsVectorLayer(landuse_retail_Sicilia,"retail Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Sardegna.shp"
vlayer = QgsVectorLayer(landuse_retail_Sardegna,"retail Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Puglia.shp"
vlayer = QgsVectorLayer(landuse_retail_Puglia,"retail Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Piemonte.shp"
vlayer = QgsVectorLayer(landuse_retail_Piemonte,"retail Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Marche.shp"
vlayer = QgsVectorLayer(landuse_retail_Marche,"retail Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Lombardia.shp"
vlayer = QgsVectorLayer(landuse_retail_Lombardia,"retail Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Lazio.shp"
vlayer = QgsVectorLayer(landuse_retail_Lazio,"retail Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Friuli.shp"
vlayer = QgsVectorLayer(landuse_retail_Friuli_Venezia_Giulia,"retail Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Emilia_Romagna.shp"
vlayer = QgsVectorLayer(landuse_retail_Emilia_Romagna,"retail Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Campania.shp"
vlayer = QgsVectorLayer(landuse_retail_Campania,"retail Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Calabria.shp"
vlayer = QgsVectorLayer(landuse_retail_Calabria,"retail Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Basilicata.shp"
vlayer = QgsVectorLayer(landuse_retail_Basilicata,"retail Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/ret_Abruzzo.shp"
vlayer = QgsVectorLayer(landuse_retail_Abruzzo,"retail Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Veneto.shp"
vlayer = QgsVectorLayer(landuse_residential_Veneto,"residential Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(landuse_residential_Valle_d_Aosta,"residential Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Umbria.shp"
vlayer = QgsVectorLayer(landuse_residential_Umbria,"residential Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Trentino.shp"
vlayer = QgsVectorLayer(landuse_residential_Trentino_Alto_Adige,"residential Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Toscana.shp"
vlayer = QgsVectorLayer(landuse_residential_Toscana,"residential Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Sicilia.shp"
vlayer = QgsVectorLayer(landuse_residential_Sicilia,"residential Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Sardegna.shp"
vlayer = QgsVectorLayer(landuse_residential_Sardegna,"residential Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Puglia.shp"
vlayer = QgsVectorLayer(landuse_residential_Puglia,"residential Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Piemonte.shp"
vlayer = QgsVectorLayer(landuse_residential_Piemonte,"residential Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Molise.shp"
vlayer = QgsVectorLayer(landuse_residential_Molise,"residential Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Marche.shp"
vlayer = QgsVectorLayer(landuse_residential_Marche,"residential Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Lombardia.shp"
vlayer = QgsVectorLayer(landuse_residential_Lombardia,"residential Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Liguria.shp"
vlayer = QgsVectorLayer(landuse_residential_Liguria,"residential Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Lazio.shp"
vlayer = QgsVectorLayer(landuse_residential_Lazio,"residential Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Friuli.shp"
vlayer = QgsVectorLayer(landuse_residential_Friuli_Venezia_Giulia,"residential Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
     print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Emilia.shp"
vlayer = QgsVectorLayer(landuse_residential_Emilia_Romagna,"residential Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Campania.shp"
vlayer = QgsVectorLayer(landuse_residential_Campania,"residential Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Calabria.shp"
vlayer = QgsVectorLayer(landuse_residential_Calabria,"residential Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Basilicata.shp"
vlayer = QgsVectorLayer(landuse_residential_Basilicata,"residential Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/res_Abruzzo.shp"
vlayer = QgsVectorLayer(landuse_residential_Abruzzo,"residential Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Veneto.shp"
vlayer = QgsVectorLayer(building_apartments_Veneto,"apartments Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(building_apartments_Valle_d_Aosta,"apartments Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Umbria.shp"
vlayer = QgsVectorLayer(building_apartments_Umbria,"apartments Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Trentino.shp"
vlayer = QgsVectorLayer(building_apartments_Trentino_Alto_Adige,"apartments Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Toscana.shp"
vlayer = QgsVectorLayer(building_apartments_Toscana,"apartments Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Sicilia.shp"
vlayer = QgsVectorLayer(building_apartments_Sicilia,"apartments Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Sardegna.shp"
vlayer = QgsVectorLayer(building_apartments_Sardegna,"apartments Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Puglia.shp"
vlayer = QgsVectorLayer(building_apartments_Puglia,"apartments Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Piemonte.shp"
vlayer = QgsVectorLayer(building_apartments_Piemonte,"apartments Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Molise.shp"
vlayer = QgsVectorLayer(building_apartments_Molise,"apartments Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Marche.shp"
vlayer = QgsVectorLayer(building_apartments_Marche,"apartments Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Lombardia.shp"
vlayer = QgsVectorLayer(building_apartments_Lombardia,"apartments Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Liguria.shp"
vlayer = QgsVectorLayer(building_apartments_Liguria,"apartments Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Lazio.shp"
vlayer = QgsVectorLayer(building_apartments_Lazio,"apartments Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Friuli.shp"
vlayer = QgsVectorLayer(building_apartments_Friuli_Venezia_Giulia,"apartments Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Emilia.shp"
vlayer = QgsVectorLayer(building_apartments_Emilia_Romagna,"apartments Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Campania.shp"
vlayer = QgsVectorLayer(building_apartments_Campania,"apartments Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Calabria.shp"
vlayer = QgsVectorLayer(building_apartments_Calabria,"apartments Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Basilicata.shp"
vlayer = QgsVectorLayer(building_apartments_Basilicata,"apartments Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/apar_Abruzzo.shp"
vlayer = QgsVectorLayer(building_apartments_Abruzzo,"apartments Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Veneto.shp"
vlayer = QgsVectorLayer(building_house_Veneto,"house Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Umbria.shp"
vlayer = QgsVectorLayer(building_house_Umbria,"house Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

building_house_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Trentino.shp"
vlayer = QgsVectorLayer(building_house_Trentino_Alto_Adige,"house Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Toscana.shp"
vlayer = QgsVectorLayer(building_house_Toscana,"house Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Sicilia.shp"
vlayer = QgsVectorLayer(building_house_Sicilia,"house Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Sardegna.shp"
vlayer = QgsVectorLayer(building_house_Sardegna,"house Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Puglia.shp"
vlayer = QgsVectorLayer(building_house_Puglia,"house Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Piemonte.shp"
vlayer = QgsVectorLayer(building_house_Piemonte,"house Piemoente","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Molise.shp"
vlayer = QgsVectorLayer(building_house_Molise,"house Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Marche.shp"
vlayer = QgsVectorLayer(building_house_Marche,"house Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Lombardia.shp"
vlayer = QgsVectorLayer(building_house_Lombardia,"house Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Liguria.shp"
vlayer = QgsVectorLayer(building_house_Liguria,"house Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Lazio.shp"
vlayer = QgsVectorLayer(building_house_Lazio,"house Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Friuli.shp"
vlayer = QgsVectorLayer(building_house_Friuli_Venezia_Giulia,"house Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Emilia.shp"
vlayer = QgsVectorLayer(building_house_Emilia_Romagna,"house Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Campania.shp"
vlayer = QgsVectorLayer(building_house_Campania,"house Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Calabria.shp"
vlayer = QgsVectorLayer(building_house_Calabria,"house Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Basilicata.shp"
vlayer = QgsVectorLayer(building_house_Basilicata,"house Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/house_Abruzzo.shp"
vlayer = QgsVectorLayer(building_house_Abruzzo,"house Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Lazio.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Lazio,"helipad Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Trentino.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Trentino_Alto_Adige,"helipad Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Piemonte.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Piemonte,"helipad Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Marche.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Marche,"helipad Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Lombardia.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Lombardia,"helipad Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/heli_Abruzzo.shp"
vlayer = QgsVectorLayer(aeroway_helipad_Abruzzo,"helipad Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Veneto.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Veneto,"aerodrome Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Trentino.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Trentino_Alto_Adige,"aerodrome Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Toscana.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Toscana,"aerodrome Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Sicilia.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Sicilia,"aerodrome Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Puglia.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Puglia,"aerodrome Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Marche.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Marche,"aerodrome Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Lombardia.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Lombardia,"aerodrome Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Lazio.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Lazio,"aerodrome Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Friuli.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Friuli_Venezia_Giulia,"aerodrome Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Emilia.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Emilia_Romagna,"aerodrome Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Campania.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Campania,"aerodrome Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/aero_Abruzzo.shp"
vlayer = QgsVectorLayer(aeroway_aerodrome_Abruzzo,"aerodrome Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Veneto.shp"
vlayer = QgsVectorLayer(natural_water_Veneto,"natural water Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Calabria.shp"
vlayer = QgsVectorLayer(natural_water_Calabria,"natural water Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Basilicata.shp"
vlayer = QgsVectorLayer(natural_water_Basilicata,"natural water Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(natural_water_Valle_d_Aosta,"natural water Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Umbria.shp"
vlayer = QgsVectorLayer(natural_water_Umbria,"natural water Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Trentino.shp"
vlayer = QgsVectorLayer(natural_water_Trentino_Alto_Adige,"natural water Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Toscana.shp"
vlayer = QgsVectorLayer(natural_water_Toscana,"natural water Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Sicilia.shp"
vlayer = QgsVectorLayer(natural_water_Sicilia,"natural water Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Sardegna.shp"
vlayer = QgsVectorLayer(natural_water_Sardegna,"natural water Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Puglia.shp"
vlayer = QgsVectorLayer(natural_water_Puglia,"natural water Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Piemonte.shp"
vlayer = QgsVectorLayer(natural_water_Piemonte,"natural water Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Molise.shp"
vlayer = QgsVectorLayer(natural_water_Molise,"natural water Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Marche.shp"
vlayer = QgsVectorLayer(natural_water_Marche,"natural water Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Lombardia.shp"
vlayer = QgsVectorLayer(natural_water_Lombardia,"natural water Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Liguria.shp"
vlayer = QgsVectorLayer(natural_water_Liguria,"natural water Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Lazio.shp"
vlayer = QgsVectorLayer(natural_water_Lazio,"natural water Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Friuli.shp"
vlayer = QgsVectorLayer(natural_water_Friuli_Venezia_Giulia,"natural water Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Emilia.shp"
vlayer = QgsVectorLayer(natural_water_Emilia_Romagna,"natural water Emilia_Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/wat_Campania.shp"
vlayer = QgsVectorLayer(natural_water_Campania,"natural water Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Basilicata.shp"
vlayer = QgsVectorLayer(natural_beach_Basilicata,"natural beach Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Veneto.shp"
vlayer = QgsVectorLayer(natural_beach_Veneto,"natural beach Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Trentino.shp"
vlayer = QgsVectorLayer(natural_beach_Trentino_Alto_Adige,"natural beach Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Toscana.shp"
vlayer = QgsVectorLayer(natural_beach_Toscana,"natural beach Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Sicilia.shp"
vlayer = QgsVectorLayer(natural_beach_Sicilia,"natural beach Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Puglia.shp"
vlayer = QgsVectorLayer(natural_beach_Puglia,"natural beach Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Piemonte.shp"
vlayer = QgsVectorLayer(natural_beach_Piemonte,"natural beach Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Marche.shp"
vlayer = QgsVectorLayer(natural_beach_Marche,"natural beach Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Lombardia.shp"
vlayer = QgsVectorLayer(natural_beach_Lombardia,"natural beach Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Liguria.shp"
vlayer = QgsVectorLayer(natural_beach_Liguria,"natural beach Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Calabria.shp"
vlayer = QgsVectorLayer(natural_beach_Calabria,"natural beach Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_beach_Abruzzo,"natural beach Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Lazio.shp"
vlayer = QgsVectorLayer(natural_beach_Lazio,"natural beach Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Friuli.shp"
vlayer = QgsVectorLayer(natural_beach_Friuli_Venezia_Giulia,"natural beach Friuli Veenzia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Emilia.shp"
vlayer = QgsVectorLayer(natural_beach_Emilia_Romagna,"natural beach Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/b_Campania.shp"
vlayer = QgsVectorLayer(natural_beach_Campania,"natural beach Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Veneto.shp"
vlayer = QgsVectorLayer(boundary_national_park_Veneto,"national park Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(boundary_national_park_Valle_d_Aosta,"national park valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Umbria.shp"
vlayer = QgsVectorLayer(boundary_national_park_Umbria,"national park Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Trentino.shp"
vlayer = QgsVectorLayer(boundary_national_park_Trentino_Alto_Adige,"national park Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Toscana.shp"
vlayer = QgsVectorLayer(boundary_national_park_Toscana,"national park Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Sardegna.shp"
vlayer = QgsVectorLayer(boundary_national_park_Sardegna,"national park Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Puglia.shp"
vlayer = QgsVectorLayer(boundary_national_park_Puglia,"national park Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Piemonte.shp"
vlayer = QgsVectorLayer(boundary_national_park_Piemonte,"national park Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Molise.shp"
vlayer = QgsVectorLayer(boundary_national_park_Molise,"national park Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Marche.shp"
vlayer = QgsVectorLayer(boundary_national_park_Marche,"national park Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Lombardia.shp"
vlayer = QgsVectorLayer(boundary_national_park_Lombardia,"national park Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Liguria = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Liguria.shp"
vlayer = QgsVectorLayer(boundary_national_park_Liguria,"national park Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Lazio.shp"
vlayer = QgsVectorLayer(boundary_national_park_Lazio,"national park Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Emilia.shp"
vlayer = QgsVectorLayer(boundary_national_park_Emilia_Romagna,"national park Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Campania.shp"
vlayer = QgsVectorLayer(boundary_national_park_Campania,"national park Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Calabria.shp"
vlayer = QgsVectorLayer(boundary_national_park_Calabria,"national park Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Basilicata.shp"
vlayer = QgsVectorLayer(boundary_national_park_Basilicata,"national park Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/nat_Abruzzo.shp"
vlayer = QgsVectorLayer(boundary_national_park_Abruzzo,"national park Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Toscana = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Toscana.shp"
vlayer = QgsVectorLayer(natural_wetland_Toscana,"wetland Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Valle_d_Aosta = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Valle d'Aosta.shp"
vlayer = QgsVectorLayer(natural_wetland_Valle_d_Aosta,"wetland Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Trentino.shp"
vlayer = QgsVectorLayer(natural_wetland_Trentino_Alto_Adige,"wetland Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Sicilia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Sicilia.shp"
vlayer = QgsVectorLayer(natural_wetland_Sicilia,"wetland Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Sardegna = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Sardegna.shp"
vlayer = QgsVectorLayer(natural_wetland_Sardegna,"wetland Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Puglia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Puglia.shp"
vlayer = QgsVectorLayer(natural_wetland_Puglia,"wetland Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Piemonte = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Piemonte.shp"
vlayer = QgsVectorLayer(natural_wetland_Piemonte,"wetland Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Umbria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Umbria.shp"
vlayer = QgsVectorLayer(natural_wetland_Umbria,"wetland Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Molise = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Molise.shp"
vlayer = QgsVectorLayer(natural_wetland_Molise,"wetland Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Marche = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Marche.shp"
vlayer = QgsVectorLayer(natural_wetland_Marche,"wetland Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Veneto = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Veneto.shp"
vlayer = QgsVectorLayer(natural_wetland_Veneto,"wetland Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Lombardia.shp"
vlayer = QgsVectorLayer(natural_wetland_Lombardia,"wetland Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Lazio = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Lazio.shp"
vlayer = QgsVectorLayer(natural_wetland_Lazio,"wetland Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Friuli_Venezia_Giulia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Friulia.shp"
vlayer = QgsVectorLayer(natural_wetland_Toscana,"wetland Friuli_Venezia_Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Emilia.shp"
vlayer = QgsVectorLayer(natural_wetland_Emilia_Romagna,"wetland Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Campania.shp"
vlayer = QgsVectorLayer(natural_wetland_Campania,"wetland Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Calabria.shp"
vlayer = QgsVectorLayer(natural_wetland_Calabria,"wetland Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/wet_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_wetland_Abruzzo,"wetland Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/scrub_Lombardia.shp"
vlayer = QgsVectorLayer(natural_scrub_Lombardia,"scrub Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/scrub_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_scrub_Abruzzo,"scrub Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/scrub_Campania.shp"
vlayer = QgsVectorLayer(natural_scrub_Campania,"scrub Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/scrub_Emilia.shp"
vlayer = QgsVectorLayer(natural_scrub_Emilia_Romagna,"scrub Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/scrub_Basilicata.shp"
vlayer = QgsVectorLayer(natural_scrub_Basilicata,"scrub Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Emilia-Romagna.shp"
vlayer = QgsVectorLayer(natural_wood_Emilia_Romagna,"wood Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/scree_Emilia-Romagna.shp"
vlayer = QgsVectorLayer(natural_scree_Emilia_Romagna,"scree Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Emilia_Romagna = "C:/Users/Lenovo/OneDrive/Desktop/layer/rock_Emilia-Romagna.shp"
vlayer = QgsVectorLayer(natural_bare_rock_Emilia_Romagna,"rock Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/rock_Campania.shp"
vlayer = QgsVectorLayer(natural_bare_rock_Campania,"rock Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/scree_Campania.shp"
vlayer = QgsVectorLayer(natural_scree_Campania,"scree Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Campania = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Campania.shp"
vlayer = QgsVectorLayer(natural_wood_Campania,"wood Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Calabria.shp"
vlayer = QgsVectorLayer(natural_wood_Calabria,"wood Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Calabria = "C:/Users/Lenovo/OneDrive/Desktop/layer/rock_Calabria.shp"
vlayer = QgsVectorLayer(natural_bare_rock_Calabria,"rock Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/rock_Basilicata.shp"
vlayer = QgsVectorLayer(natural_bare_rock_Basilicata,"rock Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/scree_Basilicata.shp"
vlayer = QgsVectorLayer(natural_scree_Basilicata,"scree Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Basilicata = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Basilicata.shp"
vlayer = QgsVectorLayer(natural_wood_Basilicata,"wood Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_wood_Abruzzo,"wood_Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/scree_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_scree_Abruzzo,"scree_Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/glacier_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_glacier_Abruzzo,"glacier Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Abruzzo = "C:/Users/Lenovo/OneDrive/Desktop/layer/rock_Abruzzo.shp"
vlayer = QgsVectorLayer(natural_bare_rock_Abruzzo,"rock Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/wood_Lombardia.shp"
vlayer = QgsVectorLayer(natural_wood_Lombardia,"wood Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

natural_scree_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/sree_Lombardia.shp"
vlayer = QgsVectorLayer(natural_scree_Lombardia,"scree Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/glacier_Lombardia.shp"
vlayer = QgsVectorLayer(natural_glacier_Lombardia,"glacier Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Lombardia = "C:/Users/Lenovo/OneDrive/Desktop/layer/bare_rock_Lombardia.shp"
vlayer = QgsVectorLayer(natural_glacier_Lombardia,"glacier Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)