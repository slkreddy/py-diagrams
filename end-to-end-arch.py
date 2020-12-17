from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

from diagrams.k8s.infra import Node
from diagrams.k8s.network import Ing, Ingress
from diagrams.k8s.compute import Pod, StatefulSet



with Diagram(name="Programmatically created  Architecture Diagram (github.com+ slkreddy +py-diagrams)", show=False):
    
   
    ingress = Ingress("ingress")
    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("Pod Cluster"):
         pods= [
            Pod("Microservice-One"),
            Pod("Microservice-Two"),
            Pod("Microservice-One")]


    with Cluster("Sessions HA"):
        master = Redis("session")
        master - Edge(color="brown", style="dashed") - Redis("replica") << Edge(label="collect") << metrics
        pods  >> Edge(color="brown") >> master

    with Cluster("Database HA"):
        master = PostgreSQL("users")
        master - Edge(color="brown", style="dotted") - PostgreSQL("slave") << Edge(label="collect") << metrics
        pods  >> Edge(color="black") >> master


    ingress >> Edge(color="darkgreen") << pods >> Edge(color="darkorange") 
