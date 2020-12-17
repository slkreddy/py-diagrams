from diagrams import  Diagram, Cluster
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, ReplicaSet
from diagrams.k8s.network import Service

with Diagram(name="Kuberenetes"):

 with Cluster("Pod Cluster"):
   pods= [
  	Pod("Microservice-One"),
       	Pod("Microservice-Two"),
       	Pod("Microservice-One")]

 Service("Load Balancer") >> ReplicaSet("Replicaset") >> pods

