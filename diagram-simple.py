# diagram-simple.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from diagrams.k8s.compute import Pod, StatefulSet


with Diagram("diagram-simple", show=False):
 (Pod("GUI") >>  ELB("lb")) >> EC2("web") >> RDS("userdb")
