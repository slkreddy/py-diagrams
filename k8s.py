from diagrams.k8s.infra import Node
from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, ReplicaSet
from diagrams.k8s.controlplane import Kubelet
from diagrams.k8s.group import Namespace
from diagrams.k8s.infra import Node
from diagrams.k8s.network import Service

with Diagram(name="Programmatically created Kubernetes Arch Diagram (github.com+ slkreddy +py-diagrams)", show=False):
  ns = Namespace("slkreddy-namespace")
  
  with Cluster("Pod Cluster"):
         pods= [
            Pod("Microservice-One"),
            Pod("Microservice-Two"),
            Pod("Microservice-One")]

  Service("Load Balancer") >> ReplicaSet("Replicaset") >> pods







