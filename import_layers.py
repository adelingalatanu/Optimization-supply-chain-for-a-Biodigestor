import os
from qgis.core import (
     QgsVectorLayer
)

boundary_protected_area_Sardegna = "E:/layer/prot_Sardegna.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Sardegna,"protected area Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

boundary_protected_area_Abruzzo = "E:/layer/prot_Abruzzo.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Abruzzo,"protected area Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Basilicata = "E:/layer/prot_Basilicata.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Basilicata,"protected area Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Calabria = "E:/layer/prot_Calabria.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Calabria,"protected area Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Campania = "E:/layer/prot_Campania.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Campania,"protected area Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Emilia_Romagna = "E:/layer/prot_Emilia.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Emilia_Romagna,"protected area Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Friuli_Venezia_Giulia = "E:/layer/prot_Friuli.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Friuli_Venezia_Giulia,"protected area Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Lazio = "E:/layer/prot_Lazio.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Lazio,"protected area Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Liguria = "E:/layer/prot_Liguria.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Liguria,"protected area Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Lombardia = "E:/layer/prot_Lombardia.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Lombardia,"protected area Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Marche = "E:/layer/prot_Marche.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Marche,"protected area Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Molise = "E:/layer/prot_Molise.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Molise,"protected area Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Piemonte = "E:/layer/prot_Piemonte.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Piemonte,"protected area Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Puglia = "E:/layer/prot_Puglia.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Puglia,"protected area Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Sicilia = "E:/layer/prot_Sicilia.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Sicilia,"protected area Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Toscana = "E:/layer/prot_Toscana.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Toscana,"protected area Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Trentino_Alto_Adige = "E:/layer/prot_Trentino.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Trentino_Alto_Adige,"protected area Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Umbria = "E:/layer/prot_Umbria.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Umbria,"protected area Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Valle_d_Aosta = "E:/layer/prot_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Valle_d_Aosta,"protected area Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_protected_area_Veneto = "E:/layer/prot_Veneto.dbf"
vlayer = QgsVectorLayer(boundary_protected_area_Veneto,"protected area Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Veneto = "E:/layer/plant_Veneto.dbf"
vlayer = QgsVectorLayer(power_plant_Veneto,"plant Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

power_plant_Trentino_Alto_Adige = "E:/layer/plant_Trentino.dbf"
vlayer = QgsVectorLayer(power_plant_Trentino_Alto_Adige,"plant Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Toscana = "E:/layer/plant_Toscana.dbf"
vlayer = QgsVectorLayer(power_plant_Toscana,"plant Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Sicilia = "E:/layer/plant_Sicilia.dbf"
vlayer = QgsVectorLayer(power_plant_Sicilia,"plant Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Puglia = "E:/layer/plant_Puglia.dbf"
vlayer = QgsVectorLayer(power_plant_Puglia,"plant Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Piemonte = "E:/layer/plant_Piemonte.dbf"
vlayer = QgsVectorLayer(power_plant_Piemonte,"plant Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Marche = "E:/layer/plant_Marche.dbf"
vlayer = QgsVectorLayer(power_plant_Marche,"plant Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Lombardia = "E:/layer/plant_Lombardia.dbf"
vlayer = QgsVectorLayer(power_plant_Lombardia,"plant Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Lazio = "E:/layer/plant_Lazio.dbf"
vlayer = QgsVectorLayer(power_plant_Lazio,"plant Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Friuli_Venezia_Giulia = "E:/layer/plant_Friuli.dbf"
vlayer = QgsVectorLayer(power_plant_Friuli_Venezia_Giulia,"plant Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Emilia_Romagna = "E:/layer/plant_Emilia.dbf"
vlayer = QgsVectorLayer(power_plant_Emilia_Romagna,"plant Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Calabria = "E:/layer/plant_Calabria.dbf"
vlayer = QgsVectorLayer(power_plant_Calabria,"plant Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
power_plant_Abruzzo = "E:/layer/plant_Abruzzo.dbf"
vlayer = QgsVectorLayer(power_plant_Abruzzo,"plant Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Veneto = "E:/layer/ind_Veneto.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Veneto,"industrial Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Valle_d_Aosta = "E:/layer/ind_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Valle_d_Aosta,"industrial Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Umbria = "E:/layer/ind_Umbria.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Umbria,"industrial Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Trentino_Alto_Adige = "E:/layer/ind_Trentino.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Trentino_Alto_Adige,"industrial Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Toscana = "E:/layer/ind_Toscana.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Toscana,"industrial Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Sicilia = "E:/layer/ind_Sicilia.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Sicilia,"industrial Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Sardegna = "E:/layer/ind_Sardegna.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Sardegna,"industrial Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Puglia = "E:/layer/ind_Puglia.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Puglia,"industrial Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Piemonte = "E:/layer/ind_Piemonte.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Piemonte,"industrial Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Molise = "E:/layer/ind_Molise.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Molise,"industrial Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Marche = "E:/layer/ind_Marche.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Marche,"industrial Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Lombardia = "E:/layer/ind_Lombardia.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Lombardia,"industrial Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Liguria = "E:/layer/ind_Liguria.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Liguria,"industrial Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Lazio = "E:/layer/ind_Lazio.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Lazio,"industrial Lazio","ogr")
if not vlayer.isValid():
     print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Friuli_Venezia_Giulia = "E:/layer/ind_Friuli.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Friuli_Venezia_Giulia,"industrial Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Emilia_Romagna = "E:/layer/ind_Emilia.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Emilia_Romagna,"industrial Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Campania = "E:/layer/ind_Campania.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Campania,"industrial Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Calabria= "E:/layer/ind_Calabria.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Calabria,"industrial Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Basilicata = "E:/layer/ind_Basilicata.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Basilicata,"industrial Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_industrial_Abruzzo = "E:/layer/ind_Abruzzo.dbf"
vlayer = QgsVectorLayer(landuse_industrial_Abruzzo,"industrial Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Veneto = "E:/layer/comm_Veneto.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Veneto,"commercial Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Umbria = "E:/layer/comm_Umbria.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Umbria,"commercial Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Trentino_Alto_Adige = "C:/Users/Lenovo/OneDrive/Desktop/layer/comm_Trentino.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Trentino_Alto_Adige,"commercial Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Toscana = "E:/layer/comm_Toscana.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Toscana,"commercial Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Sicilia = "E:/layer/comm_Sicilia.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Sicilia,"commercial Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_commercial_Sardegna = "E:/layer/comm_Sardegna.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Sardegna,"commercial Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Piemonte = "E:/layer/comm_Piemonte.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Piemonte,"commercial Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Molise = "E:/layer/comm_Molise.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Molise,"commercial Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Marche = "E:/layer/comm_Marche.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Marche,"commercial Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Lombardia = "E:/layer/comm_Lombardia.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Lombardia,"commercial Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Liguria = "E:/layer/comm_Liguria.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Liguria,"commercial Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Lazio = "E:/layer/comm_Lazio.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Lazio,"commercial Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Friuli_Venezia_Giulia = "E:/layer/comm_Friuli.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Friuli_Venezia_Giulia ,"commercial Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Emilia_Romagna = "E:/layer/comm_Emilia.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Emilia_Romagna,"commercial Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Campania = "E:/layer/comm_Campania.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Campania,"commercial Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Calabria = "E:/layer/comm_Calabria.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Calabria,"commercial Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Basilicata = "E:/layer/comm_Basilicata.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Basilicata,"commercial Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_commercial_Abruzzo = "E:/layer/comm_Abruzzo.dbf"
vlayer = QgsVectorLayer(landuse_commercial_Abruzzo,"commercial Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_retail_Veneto = "E:/layer/ret_Veneto.dbf"
vlayer = QgsVectorLayer(landuse_retail_Veneto,"retail Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Umbria = "E:/layer/ret_Umbria.dbf"
vlayer = QgsVectorLayer(landuse_retail_Umbria,"retail Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

landuse_retail_Trentino_Alto_Adige = "E:/layer/ret_Trentino.dbf"
vlayer = QgsVectorLayer(landuse_retail_Trentino_Alto_Adige,"retail Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Toscana = "E:/layer/ret_Toscana.dbf"
vlayer = QgsVectorLayer(landuse_retail_Toscana,"retail Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Sicilia = "E:/layer/ret_Sicilia.dbf"
vlayer = QgsVectorLayer(landuse_retail_Sicilia,"retail Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Sardegna = "E:/layer/ret_Sardegna.dbf"
vlayer = QgsVectorLayer(landuse_retail_Sardegna,"retail Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Puglia = "E:/layer/ret_Puglia.dbf"
vlayer = QgsVectorLayer(landuse_retail_Puglia,"retail Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Piemonte = "E:/layer/ret_Piemonte.dbf"
vlayer = QgsVectorLayer(landuse_retail_Piemonte,"retail Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Marche = "E:/layer/ret_Marche.dbf"
vlayer = QgsVectorLayer(landuse_retail_Marche,"retail Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Lombardia = "E:/layer/ret_Lombardia.dbf"
vlayer = QgsVectorLayer(landuse_retail_Lombardia,"retail Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Lazio = "E:/layer/ret_Lazio.dbf"
vlayer = QgsVectorLayer(landuse_retail_Lazio,"retail Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Friuli_Venezia_Giulia = "E:/layer/ret_Friuli.dbf"
vlayer = QgsVectorLayer(landuse_retail_Friuli_Venezia_Giulia,"retail Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Emilia_Romagna = "E:/layer/ret_Emilia_Romagna.dbf"
vlayer = QgsVectorLayer(landuse_retail_Emilia_Romagna,"retail Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Campania = "E:/layer/ret_Campania.dbf"
vlayer = QgsVectorLayer(landuse_retail_Campania,"retail Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Calabria = "E:/layer/ret_Calabria.dbf"
vlayer = QgsVectorLayer(landuse_retail_Calabria,"retail Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Basilicata = "E:/layer/ret_Basilicata.dbf"
vlayer = QgsVectorLayer(landuse_retail_Basilicata,"retail Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_retail_Abruzzo = "E:/layer/ret_Abruzzo.dbf"
vlayer = QgsVectorLayer(landuse_retail_Abruzzo,"retail Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Veneto = "E:/layer/res_Veneto.dbf"
vlayer = QgsVectorLayer(landuse_residential_Veneto,"residential Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Valle_d_Aosta = "E:/layer/res_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(landuse_residential_Valle_d_Aosta,"residential Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Umbria = "E:/layer/res_Umbria.dbf"
vlayer = QgsVectorLayer(landuse_residential_Umbria,"residential Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Trentino_Alto_Adige = "E:/layer/res_Trentino.dbf"
vlayer = QgsVectorLayer(landuse_residential_Trentino_Alto_Adige,"residential Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Toscana = "E:/layer/res_Toscana.dbf"
vlayer = QgsVectorLayer(landuse_residential_Toscana,"residential Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Sicilia = "E:/layer/res_Sicilia.dbf"
vlayer = QgsVectorLayer(landuse_residential_Sicilia,"residential Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Sardegna = "E:/layer/res_Sardegna.dbf"
vlayer = QgsVectorLayer(landuse_residential_Sardegna,"residential Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Puglia = "E:/layer/res_Puglia.dbf"
vlayer = QgsVectorLayer(landuse_residential_Puglia,"residential Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Piemonte = "E:/layer/res_Piemonte.dbf"
vlayer = QgsVectorLayer(landuse_residential_Piemonte,"residential Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Molise = "E:/layer/res_Molise.dbf"
vlayer = QgsVectorLayer(landuse_residential_Molise,"residential Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Marche = "E:/layer/res_Marche.dbf"
vlayer = QgsVectorLayer(landuse_residential_Marche,"residential Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Lombardia = "E:/layer/res_Lombardia.dbf"
vlayer = QgsVectorLayer(landuse_residential_Lombardia,"residential Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Liguria = "E:/layer/res_Liguria.dbf"
vlayer = QgsVectorLayer(landuse_residential_Liguria,"residential Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Lazio = "E:/layer/res_Lazio.dbf"
vlayer = QgsVectorLayer(landuse_residential_Lazio,"residential Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Friuli_Venezia_Giulia = "E:/layer/res_Friuli.dbf"
vlayer = QgsVectorLayer(landuse_residential_Friuli_Venezia_Giulia,"residential Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
     print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Emilia_Romagna = "E:/layer/res_Emilia.dbf"
vlayer = QgsVectorLayer(landuse_residential_Emilia_Romagna,"residential Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Campania = "E:/layer/res_Campania.dbf"
vlayer = QgsVectorLayer(landuse_residential_Campania,"residential Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Calabria = "E:/layer/res_Calabria.dbf"
vlayer = QgsVectorLayer(landuse_residential_Calabria,"residential Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Basilicata = "E:/layer/res_Basilicata.dbf"
vlayer = QgsVectorLayer(landuse_residential_Basilicata,"residential Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
landuse_residential_Abruzzo = "E:/layer/res_Abruzzo.dbf"
vlayer = QgsVectorLayer(landuse_residential_Abruzzo,"residential Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Veneto = "E:/layer/apar_Veneto.dbf"
vlayer = QgsVectorLayer(building_apartments_Veneto,"apartments Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Valle_d_Aosta = "E:/layer/apar_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(building_apartments_Valle_d_Aosta,"apartments Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Umbria = "E:/layer/apar_Umbria.dbf"
vlayer = QgsVectorLayer(building_apartments_Umbria,"apartments Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Trentino_Alto_Adige = "E:/layer/apar_Trentino.dbf"
vlayer = QgsVectorLayer(building_apartments_Trentino_Alto_Adige,"apartments Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Toscana = "E:/layer/apar_Toscana.dbf"
vlayer = QgsVectorLayer(building_apartments_Toscana,"apartments Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Sicilia = "E:/layer/apar_Sicilia.dbf"
vlayer = QgsVectorLayer(building_apartments_Sicilia,"apartments Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Sardegna = "E:/layer/apar_Sardegna.dbf"
vlayer = QgsVectorLayer(building_apartments_Sardegna,"apartments Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Puglia = "E:/layer/apar_Puglia.dbf"
vlayer = QgsVectorLayer(building_apartments_Puglia,"apartments Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Piemonte = "E:/layer/apar_Piemonte.dbf"
vlayer = QgsVectorLayer(building_apartments_Piemonte,"apartments Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Molise = "E:/layer/apar_Molise.dbf"
vlayer = QgsVectorLayer(building_apartments_Molise,"apartments Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Marche = "E:/layer/apar_Marche.dbf"
vlayer = QgsVectorLayer(building_apartments_Marche,"apartments Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Lombardia = "E:/layer/apar_Lombardia.dbf"
vlayer = QgsVectorLayer(building_apartments_Lombardia,"apartments Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Liguria = "E:/layer/apar_Liguria.dbf"
vlayer = QgsVectorLayer(building_apartments_Liguria,"apartments Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Lazio = "E:/layer/apar_Lazio.dbf"
vlayer = QgsVectorLayer(building_apartments_Lazio,"apartments Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Friuli_Venezia_Giulia = "E:/layer/apar_Friuli.dbf"
vlayer = QgsVectorLayer(building_apartments_Friuli_Venezia_Giulia,"apartments Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Emilia_Romagna = "E:/layer/apar_Emilia.dbf"
vlayer = QgsVectorLayer(building_apartments_Emilia_Romagna,"apartments Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Campania = "E:/layer/apar_Campania.dbf"
vlayer = QgsVectorLayer(building_apartments_Campania,"apartments Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Calabria = "E:/layer/apar_Calabria.dbf"
vlayer = QgsVectorLayer(building_apartments_Calabria,"apartments Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Basilicata = "E:/layer/apar_Basilicata.dbf"
vlayer = QgsVectorLayer(building_apartments_Basilicata,"apartments Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_apartments_Abruzzo = "E:/layer/apar_Abruzzo.dbf"
vlayer = QgsVectorLayer(building_apartments_Abruzzo,"apartments Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Veneto = "E:/layer/house_Veneto.dbf"
vlayer = QgsVectorLayer(building_house_Veneto,"house Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Umbria = "E:/layer/house_Umbria.dbf"
vlayer = QgsVectorLayer(building_house_Umbria,"house Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

building_house_Trentino_Alto_Adige = "E:/layer/house_Trentino.dbf"
vlayer = QgsVectorLayer(building_house_Trentino_Alto_Adige,"house Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Toscana = "E:/layer/house_Toscana.dbf"
vlayer = QgsVectorLayer(building_house_Toscana,"house Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Sicilia = "E:/layer/house_Sicilia.dbf"
vlayer = QgsVectorLayer(building_house_Sicilia,"house Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Sardegna = "E:/layer/house_Sardegna.dbf"
vlayer = QgsVectorLayer(building_house_Sardegna,"house Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Puglia = "E:/layer/house_Puglia.dbf"
vlayer = QgsVectorLayer(building_house_Puglia,"house Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Piemonte = "E:/layer/house_Piemonte.dbf"
vlayer = QgsVectorLayer(building_house_Piemonte,"house Piemoente","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Molise = "E:/layer/house_Molise.dbf"
vlayer = QgsVectorLayer(building_house_Molise,"house Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Marche = "E:/layer/house_Marche.dbf"
vlayer = QgsVectorLayer(building_house_Marche,"house Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Lombardia = "E:/layer/house_Lombardia.dbf"
vlayer = QgsVectorLayer(building_house_Lombardia,"house Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Liguria = "E:/layer/house_Liguria.dbf"
vlayer = QgsVectorLayer(building_house_Liguria,"house Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Lazio = "E:/layer/house_Lazio.dbf"
vlayer = QgsVectorLayer(building_house_Lazio,"house Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Friuli_Venezia_Giulia = "E:/layer/house_Friuli.dbf"
vlayer = QgsVectorLayer(building_house_Friuli_Venezia_Giulia,"house Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Emilia_Romagna = "E:/layer/house_Emilia.dbf"
vlayer = QgsVectorLayer(building_house_Emilia_Romagna,"house Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Campania = "E:/layer/house_Campania.dbf"
vlayer = QgsVectorLayer(building_house_Campania,"house Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Calabria = "E:/layer/house_Calabria.dbf"
vlayer = QgsVectorLayer(building_house_Calabria,"house Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Basilicata = "E:/layer/house_Basilicata.dbf"
vlayer = QgsVectorLayer(building_house_Basilicata,"house Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
building_house_Abruzzo = "E:/layer/house_Abruzzo.dbf"
vlayer = QgsVectorLayer(building_house_Abruzzo,"house Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Lazio = "E:/layer/heli_Lazio.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Lazio,"helipad Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Trentino_Alto_Adige = "E:/layer/heli_Trentino.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Trentino_Alto_Adige,"helipad Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Piemonte = "E:/layer/heli_Piemonte.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Piemonte,"helipad Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Marche = "E:/layer/heli_Marche.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Marche,"helipad Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Lombardia = "E:/layer/heli_Lombardia.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Lombardia,"helipad Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_helipad_Abruzzo = "E:/layer/heli_Abruzzo.dbf"
vlayer = QgsVectorLayer(aeroway_helipad_Abruzzo,"helipad Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Veneto = "E:/layer/aero_Veneto.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Veneto,"aerodrome Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Trentino_Alto_Adige = "E:/layer/aero_Trentino.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Trentino_Alto_Adige,"aerodrome Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Toscana = "E:/layer/aero_Toscana.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Toscana,"aerodrome Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Sicilia = "E:/layer/aero_Sicilia.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Sicilia,"aerodrome Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Puglia = "E:/layer/aero_Puglia.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Puglia,"aerodrome Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Marche = "E:/layer/aero_Marche.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Marche,"aerodrome Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Lombardia = "E:/layer/aero_Lombardia.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Lombardia,"aerodrome Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Lazio = "E:/layer/aero_Lazio.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Lazio,"aerodrome Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Friuli_Venezia_Giulia = "E:/layer/aero_Friuli.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Friuli_Venezia_Giulia,"aerodrome Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Emilia_Romagna = "E:/layer/aero_Emilia.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Emilia_Romagna,"aerodrome Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Campania = "E:/layer/aero_Campania.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Campania,"aerodrome Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
aeroway_aerodrome_Abruzzo = "E:/layer/aero_Abruzzo.dbf"
vlayer = QgsVectorLayer(aeroway_aerodrome_Abruzzo,"aerodrome Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Veneto = "E:/layer/wat_Veneto.dbf"
vlayer = QgsVectorLayer(natural_water_Veneto,"natural water Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Calabria = "E:/layer/wat_Calabria.dbf"
vlayer = QgsVectorLayer(natural_water_Calabria,"natural water Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Basilicata = "E:/layer/wat_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_water_Basilicata,"natural water Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Valle_d_Aosta = "E:/layer/wat_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(natural_water_Valle_d_Aosta,"natural water Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Umbria = "E:/layer/wat_Umbria.dbf"
vlayer = QgsVectorLayer(natural_water_Umbria,"natural water Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Trentino_Alto_Adige = "E:/layer/wat_Trentino.dbf"
vlayer = QgsVectorLayer(natural_water_Trentino_Alto_Adige,"natural water Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Toscana = "E:/layer/wat_Toscana.dbf"
vlayer = QgsVectorLayer(natural_water_Toscana,"natural water Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Sicilia = "E:/layer/wat_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_water_Sicilia,"natural water Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Sardegna = "E:/layer/wat_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_water_Sardegna,"natural water Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Puglia = "E:/layer/wat_Puglia.dbf"
vlayer = QgsVectorLayer(natural_water_Puglia,"natural water Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Piemonte = "E:/layer/wat_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_water_Piemonte,"natural water Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Molise = "E:/layer/wat_Molise.dbf"
vlayer = QgsVectorLayer(natural_water_Molise,"natural water Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Marche = "E:/layer/wat_Marche.dbf"
vlayer = QgsVectorLayer(natural_water_Marche,"natural water Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Lombardia = "E:/layer/wat_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_water_Lombardia,"natural water Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Liguria = "E:/layer/wat_Liguria.dbf"
vlayer = QgsVectorLayer(natural_water_Liguria,"natural water Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Lazio = "E:/layer/wat_Lazio.dbf"
vlayer = QgsVectorLayer(natural_water_Lazio,"natural water Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Friuli_Venezia_Giulia = "E:/layer/wat_Friuli.dbf"
vlayer = QgsVectorLayer(natural_water_Friuli_Venezia_Giulia,"natural water Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Emilia_Romagna = "E:/layer/wat_Emilia.dbf"
vlayer = QgsVectorLayer(natural_water_Emilia_Romagna,"natural water Emilia_Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_water_Campania = "E:/layer/wat_Campania.dbf"
vlayer = QgsVectorLayer(natural_water_Campania,"natural water Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Basilicata = "E:/layer/b_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_beach_Basilicata,"natural beach Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Veneto = "E:/layer/b_Veneto.dbf"
vlayer = QgsVectorLayer(natural_beach_Veneto,"natural beach Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Trentino_Alto_Adige = "E:/layer/b_Trentino.dbf"
vlayer = QgsVectorLayer(natural_beach_Trentino_Alto_Adige,"natural beach Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Toscana = "E:/layer/b_Toscana.dbf"
vlayer = QgsVectorLayer(natural_beach_Toscana,"natural beach Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Sicilia = "E:/layer/b_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_beach_Sicilia,"natural beach Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Puglia = "E:/layer/b_Puglia.dbf"
vlayer = QgsVectorLayer(natural_beach_Puglia,"natural beach Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Piemonte = "E:/layer/b_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_beach_Piemonte,"natural beach Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Marche = "E:/layer/b_Marche.dbf"
vlayer = QgsVectorLayer(natural_beach_Marche,"natural beach Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Lombardia = "E:/layer/b_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_beach_Lombardia,"natural beach Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Liguria = "E:/layer/b_Liguria.dbf"
vlayer = QgsVectorLayer(natural_beach_Liguria,"natural beach Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Calabria = "E:/layer/b_Calabria.dbf"
vlayer = QgsVectorLayer(natural_beach_Calabria,"natural beach Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Abruzzo = "E:/layer/b_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_beach_Abruzzo,"natural beach Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Lazio = "E:/layer/b_Lazio.dbf"
vlayer = QgsVectorLayer(natural_beach_Lazio,"natural beach Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Friuli_Venezia_Giulia = "E:/layer/b_Friuli.dbf"
vlayer = QgsVectorLayer(natural_beach_Friuli_Venezia_Giulia,"natural beach Friuli Veenzia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Emilia_Romagna = "E:/layer/b_Emilia.dbf"
vlayer = QgsVectorLayer(natural_beach_Emilia_Romagna,"natural beach Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_beach_Campania = "E:/layer/b_Campania.dbf"
vlayer = QgsVectorLayer(natural_beach_Campania,"natural beach Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Veneto = "E:/layer/nat_Veneto.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Veneto,"national park Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Valle_d_Aosta = "E:/layer/nat_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Valle_d_Aosta,"national park valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Umbria = "E:/layer/nat_Umbria.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Umbria,"national park Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Trentino_Alto_Adige = "E:/layer/nat_Trentino.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Trentino_Alto_Adige,"national park Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Toscana = "E:/layer/nat_Toscana.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Toscana,"national park Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Sardegna = "E:/layer/nat_Sardegna.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Sardegna,"national park Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Puglia = "E:/layer/nat_Puglia.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Puglia,"national park Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Piemonte = "E:/layer/nat_Piemonte.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Piemonte,"national park Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Molise = "E:/layer/nat_Molise.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Molise,"national park Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Marche = "E:/layer/nat_Marche.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Marche,"national park Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Lombardia = "E:/layer/nat_Lombardia.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Lombardia,"national park Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Liguria = "E:/layer/nat_Liguria.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Liguria,"national park Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Lazio = "E:/layer/nat_Lazio.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Lazio,"national park Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Emilia_Romagna = "E:/layer/nat_Emilia.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Emilia_Romagna,"national park Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Campania = "E:/layer/nat_Campania.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Campania,"national park Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Calabria = "E:/layer/nat_Calabria.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Calabria,"national park Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Basilicata = "E:/layer/nat_Basilicata.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Basilicata,"national park Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
boundary_national_park_Abruzzo = "E:/layer/nat_Abruzzo.dbf"
vlayer = QgsVectorLayer(boundary_national_park_Abruzzo,"national park Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Toscana = "E:/layer/wet_Toscana.dbf"
vlayer = QgsVectorLayer(natural_wetland_Toscana,"wetland Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Valle_d_Aosta = "E:/layer/wet_Valle d'Aosta.dbf"
vlayer = QgsVectorLayer(natural_wetland_Valle_d_Aosta,"wetland Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Trentino_Alto_Adige = "E:/layer/wet_Trentino.dbf"
vlayer = QgsVectorLayer(natural_wetland_Trentino_Alto_Adige,"wetland Trentino Alto Adige","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Sicilia = "E:/layer/wet_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_wetland_Sicilia,"wetland Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Sardegna = "E:/layer/wet_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_wetland_Sardegna,"wetland Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Puglia = "E:/layer/wet_Puglia.dbf"
vlayer = QgsVectorLayer(natural_wetland_Puglia,"wetland Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Piemonte = "E:/layer/wet_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_wetland_Piemonte,"wetland Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Umbria = "E:/layer/wet_Umbria.dbf"
vlayer = QgsVectorLayer(natural_wetland_Umbria,"wetland Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Molise = "E:/layer/wet_Molise.dbf"
vlayer = QgsVectorLayer(natural_wetland_Molise,"wetland Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Marche = "E:/layer/wet_Marche.dbf"
vlayer = QgsVectorLayer(natural_wetland_Marche,"wetland Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Veneto = "E:/layer/wet_Veneto.dbf"
vlayer = QgsVectorLayer(natural_wetland_Veneto,"wetland Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Lombardia = "E:/layer/wet_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_wetland_Lombardia,"wetland Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Lazio = "E:/layer/wet_Lazio.dbf"
vlayer = QgsVectorLayer(natural_wetland_Lazio,"wetland Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Friuli_Venezia_Giulia = "E:/layer/wet_Friulia.dbf"
vlayer = QgsVectorLayer(natural_wetland_Toscana,"wetland Friuli_Venezia_Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Emilia_Romagna = "E:/layer/wet_Emilia.dbf"
vlayer = QgsVectorLayer(natural_wetland_Emilia_Romagna,"wetland Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Campania = "E:/layer/wet_Campania.dbf"
vlayer = QgsVectorLayer(natural_wetland_Campania,"wetland Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Calabria = "E:/layer/wet_Calabria.dbf"
vlayer = QgsVectorLayer(natural_wetland_Calabria,"wetland Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wetland_Abruzzo = "E:/layer/wet_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_wetland_Abruzzo,"wetland Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Lombardia = "E:/layer/scrub_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_scrub_Lombardia,"scrub Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Abruzzo = "E:/layer/scrub_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_scrub_Abruzzo,"scrub Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Campania = "E:/layer/scrub_Campania.dbf"
vlayer = QgsVectorLayer(natural_scrub_Campania,"scrub Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Emilia_Romagna = "E:/layer/scrub_Emilia.dbf"
vlayer = QgsVectorLayer(natural_scrub_Emilia_Romagna,"scrub Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Basilicata = "E:/layer/scrub_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_scrub_Basilicata,"scrub Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Emilia_Romagna = "E:/layer/wood_Emilia-Romagna.dbf"
vlayer = QgsVectorLayer(natural_wood_Emilia_Romagna,"wood Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Emilia_Romagna = "E:/layer/scree_Emilia-Romagna.dbf"
vlayer = QgsVectorLayer(natural_scree_Emilia_Romagna,"scree Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Emilia_Romagna = "E:/layer/rock_Emilia-Romagna.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Emilia_Romagna,"rock Emilia Romagna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Campania = "E:/layer/rock_Campania.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Campania,"rock Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Campania = "E:/layer/scree_Campania.dbf"
vlayer = QgsVectorLayer(natural_scree_Campania,"scree Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Campania = "E:/layer/wood_Campania.dbf"
vlayer = QgsVectorLayer(natural_wood_Campania,"wood Campania","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Calabria = "E:/layer/wood_Calabria.dbf"
vlayer = QgsVectorLayer(natural_wood_Calabria,"wood Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Calabria = "E:/layer/rock_Calabria.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Calabria,"rock Calabria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Basilicata = "E:/layer/rock_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Basilicata,"rock Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Basilicata = "E:/layer/scree_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_scree_Basilicata,"scree Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Basilicata = "E:/layer/wood_Basilicata.dbf"
vlayer = QgsVectorLayer(natural_wood_Basilicata,"wood Basilicata","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Abruzzo = "E:/layer/wood_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_wood_Abruzzo,"wood_Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Abruzzo = "E:/layer/scree_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_scree_Abruzzo,"scree_Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Abruzzo = "E:/layer/glacier_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_glacier_Abruzzo,"glacier Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Abruzzo = "E:/layer/rock_Abruzzo.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Abruzzo,"rock Abruzzo","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Lombardia = "E:/layer/wood_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_wood_Lombardia,"wood Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

natural_scree_Lombardia = "E:/layer/sree_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_scree_Lombardia,"scree Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Lombardia = "E:/layer/glacier_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_glacier_Lombardia,"glacier Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Lombardia = "E:/layer/bare_rock_Lombardia.dbf"
vlayer = QgsVectorLayer(natural_glacier_Lombardia,"glacier Lombardia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Friuli_Venezia_Giulia = "E:/layer/wood_Friuli.dbf"
vlayer = QgsVectorLayer(natural_wood_Friuli_Venezia_Giulia,"wood Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Lazio = "E:/layer/wood_Lazio.dbf"
vlayer = QgsVectorLayer(natural_wood_Lazio,"wood Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Marche = "E:/layer/wood_Marche.dbf"
vlayer = QgsVectorLayer(natural_wood_Marche,"wood Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Molise = "E:/layer/wood_Molise.dbf"
vlayer = QgsVectorLayer(natural_wood_Molise,"wood Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Piemonte = "E:/layer/wood_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_wood_Piemonte,"wood Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Puglia = "E:/layer/wood_Puglia.dbf"
vlayer = QgsVectorLayer(natural_wood_Puglia,"wood Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Sardegna = "E:/layer/wood_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_wood_Sardegna,"wood Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Sicilia = "E:/layer/wood_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_wood_Sicilia,"wood Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Toscana = "E:/layer/wood_Friuli.gpkg"
vlayer = QgsVectorLayer(natural_wood_Toscana,"wood Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Trentino = "E:/layer/wood_Trentino.gpkg"
vlayer = QgsVectorLayer(natural_wood_Trentino,"wood Trentino","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Umbria = "E:/layer/wood_Umbria.gpkg"
vlayer = QgsVectorLayer(natural_wood_Umbria,"wood Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Valle_d_Aosta = "E:/layer/wood_Valle d'Aosta.gpkg"
vlayer = QgsVectorLayer(natural_wood_Valle_d_Aosta,"wood Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Veneto = "E:/layer/wood_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_wood_Veneto,"wood Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Friuli_Venezia_Giulia = "E:/layer/rock_Friuli.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Friuli_Venezia_Giulia,"rock Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Lazio = "E:/layer/rock_Lazio.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Lazio,"rock Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Liguria = "E:/layer/rock_Liguria.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Liguria,"rock Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Marche = "E:/layer/rock_Marche.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Marche,"rock Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Molise = "E:/layer/rock_Molise.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Molise,"rock Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Piemonte = "E:/layer/rock_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Piemonte,"rock Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Puglia = "E:/layer/rock_Puglia.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Puglia,"rock Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Sardegna = "E:/layer/rock_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Sardegna,"rock Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Sicilia = "E:/layer/rock_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_bare_rock_Sicilia,"rock Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Friuli_Venezia_Giulia = "E:/layer/scree_Friuli.dbf"
vlayer = QgsVectorLayer(natural_scree_Friuli_Venezia_Giulia,"scree Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Lazio = "E:/layer/scree_Lazio.dbf"
vlayer = QgsVectorLayer(natural_scree_Lazio,"scree Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Liguria = "E:/layer/scree_Liguria.dbf"
vlayer = QgsVectorLayer(natural_scree_Liguria,"scree Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Marche = "E:/layer/scree_Marche.dbf"
vlayer = QgsVectorLayer(natural_scree_Marche,"scree Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Molise = "E:/layer/scree_Molise.dbf"
vlayer = QgsVectorLayer(natural_scree_Molise,"scree Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Piemonte = "E:/layer/scree_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_scree_Piemonte,"scree Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Puglia = "E:/layer/scree_Puglia.dbf"
vlayer = QgsVectorLayer(natural_scree_Puglia,"scree Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Sardegna = "E:/layer/scree_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_scree_Sardegna,"scree Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Sicilia = "E:/layer/scree_Sicilia.dbf"
vlayer = QgsVectorLayer(natural_scree_Sicilia,"scree Sicilia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Lazio = "E:/layer/scrub_Lazio.dbf"
vlayer = QgsVectorLayer(natural_scrub_Lazio,"scrub Lazio","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Friuli_Venezia_Giulia = "E:/layer/scrub_Friuli.dbf"
vlayer = QgsVectorLayer(natural_scrub_Friuli_Venezia_Giulia,"scrub Friuli Venezia Giulia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Liguria = "E:/layer/scrub_Liguria.dbf"
vlayer = QgsVectorLayer(natural_scrub_Liguria,"scrub Liguria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Marche = "E:/layer/scrub_Marche.dbf"
vlayer = QgsVectorLayer(natural_scrub_Marche,"scrub Marche","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Molise = "E:/layer/scrub_Molise.dbf"
vlayer = QgsVectorLayer(natural_scrub_Molise,"scrub Molise","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Piemonte = "E:/layer/scrub_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_scrub_Piemonte,"scrub Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Puglia = "E:/layer/scrub_Puglia.dbf"
vlayer = QgsVectorLayer(natural_scrub_Puglia,"scrub Puglia","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Sardegna = "E:/layer/scrub_Sardegna.dbf"
vlayer = QgsVectorLayer(natural_scrub_Sardegna,"scrub Sardegna","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Piemonte = "E:/layer/glacier_Piemonte.dbf"
vlayer = QgsVectorLayer(natural_glacier_Piemonte,"glacier_Piemonte","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Trentino = "E:/layer/glacier_Trentino.gpkg"
vlayer = QgsVectorLayer(natural_glacier_Trentino,"glacier_Trentino","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Valle_d_Aosta = "E:/layer/glacier_Valle d'Aosta.gpkg"
vlayer = QgsVectorLayer(natural_wood_Veneto,"glacier Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_glacier_Veneto = "E:/layer/glacier_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_glacier_Veneto,"glacier Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_wood_Veneto = "E:/layer/wood_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_wood_Veneto,"wood Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Toscana = "E:/layer/rock_Toscana.gpkg"
vlayer = QgsVectorLayer(natural_bare_rock_Toscana,"wood Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Trentino = "E:/layer/rock_Trentino.gpkg"
vlayer = QgsVectorLayer(natural_bare_rock_Trentino,"wood Trentino","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Umbria = "E:/layer/rock_Umbria.gpkg"
vlayer = QgsVectorLayer(natural_bare_rock_Umbria,"wood Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Valle_d_Aosta = "E:/layer/rock_Valle d'Aosta.gpkg"
vlayer = QgsVectorLayer(natural_bare_rock_Valle_d_Aosta,"wood Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_bare_rock_Veneto = "E:/layer/rock_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_bare_rock_Veneto,"wood Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Toscana = "E:/layer/scree_Toscana.gpkg"
vlayer = QgsVectorLayer(natural_scree_Toscana,"scree Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Trentino = "E:/layer/scree_Trentino.gpkg"
vlayer = QgsVectorLayer(natural_scree_Trentino,"scree Trentino","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Umbria = "E:/layer/scree_Umbria.gpkg"
vlayer = QgsVectorLayer(natural_scree_Umbria,"scree Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Valle_d_Aosta = "E:/layer/scree_Valle d'Aosta.gpkg"
vlayer = QgsVectorLayer(natural_scree_Valle_d_Aosta,"scree Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scree_Veneto = "E:/layer/scree_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_scree_Veneto,"scree Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Toscana = "E:/layer/scrub_Toscana.gpkg"
vlayer = QgsVectorLayer(natural_scrub_Toscana,"scrub Toscana","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Trentino = "E:/layer/scrub_Trentino.gpkg"
vlayer = QgsVectorLayer(natural_scrub_Trentino,"scrub Trentino","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Umbria = "E:/layer/scrub_Umbria.gpkg"
vlayer = QgsVectorLayer(natural_scrub_Umbria,"scrub Umbria","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Valle_d_Aosta = "E:/layer/scrub_valle d'Aosta.gpkg"
vlayer = QgsVectorLayer(natural_scrub_Valle_d_Aosta,"scrub Valle d'Aosta","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    
natural_scrub_Veneto = "E:/layer/scrub_Veneto.gpkg"
vlayer = QgsVectorLayer(natural_scrub_Veneto,"scrub Veneto","ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)