# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

import pickle
from copy import deepcopy


def test_scene_nodes(scene):
    assert hasattr(scene, "nodes")


def test_add_node(scene, node_a):
    assert not scene.nodes

    scene.add_node(node_a)

    assert node_a in scene.nodes


def test_eq(scene):
    copy_scene = deepcopy(scene)
    assert scene == copy_scene


def test_pickable(scene, node_a, node_b, input_port_a, output_port_a):
    input_port_a.connect_to(output_port_a)

    node_a.add_output_port(output_port_a)
    node_b.add_input_port(input_port_a)

    scene.add_node(node_a)
    scene.add_node(node_b)

    obj = pickle.dumps(scene)
    loaded_scene = pickle.loads(obj)

    assert loaded_scene == scene

    assert (
        loaded_scene.nodes[1].inputs["a"]
        in loaded_scene.nodes[0].outputs["a"].connections
    )
