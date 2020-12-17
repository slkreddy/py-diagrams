from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.k8s.compute import Pod, StatefulSet


with Diagram("Kubernetes Cluster", show=False):
    dns = Route53("dns")
    web = ECS("service")

    with Cluster("Kubernetes Cluster"):
        db_master = Pod("master")
        db_master - [Pod("worker1"),
                     Pod("worker2")]

    dns >> web >> db_master
