node_list = []
node_list = ops('FBX/*')
for node in node_list:
    if type(node) is not nullCOMP:
        node_list.remove(node)
print(node_list)
for node in node_list:
    [x.destroy() for x in node.ops('*')]

    nodeGeometry = node.create(sphereSOP, 'nodeGeometry')
    geometryTransform = node.create(transformSOP, 'geometryTransform')
    nullOut = node.create(nullSOP, 'nullOut')

    nodeGeometry.par.type = 1
    geometryTransform.par.scale = 8
    
    geometryTransform.nodeX = 200
    nullOut.nodeX = 400

    nodeGeometry.outputConnectors[0].connect(geometryTransform.inputConnectors[0])
    geometryTransform.outputConnectors[0].connect(nullOut)

    nullOut.display = True
    nullOut.render = True


