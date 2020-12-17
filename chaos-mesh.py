from diagrams.k8s.infra import Node
from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, ReplicaSet
from diagrams.k8s.controlplane import Kubelet
from diagrams.k8s.group import Namespace
from diagrams.k8s.infra import Node
from diagrams.k8s.network import Service
from diagrams.k8s.chaos import ChaosMesh
from diagrams.k8s.ecosystem import ExternalDns
from diagrams.onprem.monitoring import Grafana,  Prometheus
from diagrams.programming.language import Java
from diagrams.programming.framework import Spring
from diagrams.generic.device import Mobile, Tablet
from diagrams.programming.framework import Angular



with Diagram(name="Chaos Mesh  Diagram (github.com+ slkreddy +py-diagrams)", show=False):
  svc = Service("Load Balancer") 
  dns = ExternalDns("Ext DNS") 
 
  with Cluster("Pod Cluster"):
         pods= [
            Spring("Microservice-One"),
            Pod("Microservice-Two"),
            Pod("Microservice-One")]

  Mobile("Mobile User") >> dns
  Angular("Desktop GUI") >> dns
  dns >>  svc  >> ReplicaSet("Replicaset") >> pods >> ChaosMesh("Chaos Mesh") >> Grafana("Monitoring") >> Prometheus("Metrics")
