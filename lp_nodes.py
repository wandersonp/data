# -*- coding: utf-8 -*-

# Modules
import hou

# Code
class CustomGeoNodes:

    def __init__(self):
        node = hou.node("/obj")
        self.geoNode = node.createNode("geo") 
    
    def _scatterNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("scatter")

    def _sculptNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("sculpt")

    def _labsSpiral(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("labs::spiral")

    def _nameNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("name")

    def _explodedView(self): 
        if self.geoNode != None:
            node = self.geoNode.createNode("explodedView")

    def _reverse(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("reverse")

    def _twist(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("twist")

    def _quickShade(self): 
        if self.geoNode != None:
            node = self.geoNode.createNode("transform")

    def _delete(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("delete")

    def _transformNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("transform")

    def _2PolyExpand2D(self): 
        if self.geoNode != None:
            node = self.geoNode.createNode("polyExpand2D")

    def _connectAdjacentPieces(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("connect_adjacent_pieces")

    def _jitterNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("jitter")

    def _whiteWaterSource(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("white_water_source")

    def _scriptNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("script_node")

    def _booleanNode(self):
        if self.geoNode != None:
            node = self.geoNode.createNode("boolean")





















