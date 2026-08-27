#!/usr/bin/env python3
# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

"""Convert a v1.0.2 human model URDF to the v2.0.0 hand/finger structure.

The script keeps the input model unchanged except for adding the hand/finger
links and joints introduced in v2.0.0.
"""

from __future__ import annotations

import argparse
import copy
import os
import xml.etree.ElementTree as ET


RIGHT_PREFIX = "r_hand_"
LEFT_PREFIX = "l_hand_"
REQUIRED_HAND_LINKS = {"RightHand", "LeftHand"}
DEFAULT_HAND_DIMS = {"X": 0.085, "Y": 0.17982, "Z": 0.025}
MESH_PACKAGE_PREFIX = "package://human-gazebo/meshesSpinalCord"


FINGER_LENGTH_FACTORS = {
    "index_1": 0.45 * 0.92,
    "index_2": 0.33 * 0.92,
    "index_3": 0.22 * 0.92,
    "middle_1": 0.45,
    "middle_2": 0.33,
    "middle_3": 0.22,
    "ring_1": 0.45 * 0.94,
    "ring_2": 0.33 * 0.94,
    "ring_3": 0.22 * 0.94,
    "pinkie_1": 0.45 * 0.75,
    "pinkie_2": 0.33 * 0.75,
    "pinkie_3": 0.22 * 0.75,
    "thumb_1": 0.20 * 0.70,
    "thumb_2": 0.40 * 0.70,
    "thumb_3": 0.40 * 0.70,
}


FINGER_CHAIN_TOTAL_FACTORS = {
    "index": 0.92,
    "middle": 1.00,
    "ring": 0.94,
    "pinkie": 0.75,
    "thumb": 0.70,
}


def _has_existing_fingers(root: ET.Element) -> bool:
    for link in root.findall("link"):
        name = link.get("name", "")
        if name.startswith(RIGHT_PREFIX) or name.startswith(LEFT_PREFIX):
            return True

    for joint in root.findall("joint"):
        name = joint.get("name", "")
        if name.startswith("r_") or name.startswith("l_"):
            return True

    return False


def _default_template_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    code_root = os.path.dirname(here)
    return os.path.join(code_root, "models", "humanModelTemplate", "humanModelTemplate.urdf")


def _clean_template_text(raw_text: str) -> str:
    # The template URDF includes visual separators with '#' that are not XML.
    cleaned_lines = []
    for line in raw_text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def _load_xml_root(file_path: str, allow_hash_separators: bool = False) -> ET.Element:
    with open(file_path, "r", encoding="utf-8") as stream:
        text = stream.read()

    if allow_hash_separators:
        text = _clean_template_text(text)

    return ET.fromstring(text)


def _extract_finger_elements(template_root: ET.Element) -> tuple[list[ET.Element], list[ET.Element]]:
    finger_links = []
    finger_link_names = set()

    for link in template_root.findall("link"):
        name = link.get("name", "")
        if name.startswith(RIGHT_PREFIX) or name.startswith(LEFT_PREFIX):
            finger_links.append(copy.deepcopy(link))
            finger_link_names.add(name)

    finger_joints = []
    for joint in template_root.findall("joint"):
        parent_elem = joint.find("parent")
        child_elem = joint.find("child")
        parent = parent_elem.get("link") if parent_elem is not None else None
        child = child_elem.get("link") if child_elem is not None else None

        if child in finger_link_names or parent in finger_link_names:
            finger_joints.append(copy.deepcopy(joint))

    return finger_links, finger_joints


def _existing_names(root: ET.Element, tag: str) -> set[str]:
    names = set()
    for elem in root.findall(tag):
        name = elem.get("name")
        if name:
            names.add(name)
    return names


def _find_element_by_name(root: ET.Element, tag: str, name: str) -> ET.Element | None:
    for elem in root.findall(tag):
        if elem.get("name") == name:
            return elem
    return None


def _parse_xyz(text: str | None) -> list[float] | None:
    if not text:
        return None
    parts = text.strip().split()
    if len(parts) != 3:
        return None
    try:
        return [float(parts[0]), float(parts[1]), float(parts[2])]
    except ValueError:
        return None


def _format_xyz(values: list[float]) -> str:
    return " ".join(f"{value:.10g}" for value in values)


def _set_origin_xyz(parent: ET.Element, xyz: list[float]) -> None:
    origin = parent.find("origin")
    if origin is None:
        origin = ET.SubElement(parent, "origin")
        origin.set("rpy", "0 0 0")
    origin.set("xyz", _format_xyz(xyz))


def _update_box_size(link: ET.Element, x_size: float, y_size: float, z_size: float) -> None:
    size_text = f"{x_size:.10g} {y_size:.10g} {z_size:.10g}"
    for section_name in ("visual", "collision"):
        section = link.find(section_name)
        if section is None:
            continue

        geometry = section.find("geometry")
        if geometry is None:
            continue

        box = geometry.find("box")
        if box is None:
            box = ET.SubElement(geometry, "box")
        box.set("size", size_text)


def _update_collision_box_size(link: ET.Element, x_size: float, y_size: float, z_size: float) -> None:
    size_text = f"{x_size:.10g} {y_size:.10g} {z_size:.10g}"
    collision = link.find("collision")
    if collision is None:
        collision = ET.SubElement(link, "collision")
        _set_origin_xyz(collision, [0.0, 0.0, 0.0])

    geometry = collision.find("geometry")
    if geometry is None:
        geometry = ET.SubElement(collision, "geometry")

    # Collision uses simple box geometry for stable physics.
    for mesh in list(geometry.findall("mesh")):
        geometry.remove(mesh)

    box = geometry.find("box")
    if box is None:
        box = ET.SubElement(geometry, "box")
    box.set("size", size_text)


def _ensure_visual_mesh(link: ET.Element, mesh_package_prefix: str) -> None:
    name = link.get("name", "")
    if not name:
        return

    visual = link.find("visual")
    if visual is None:
        visual = ET.SubElement(link, "visual")
        _set_origin_xyz(visual, [0.0, 0.0, 0.0])

    geometry = visual.find("geometry")
    if geometry is None:
        geometry = ET.SubElement(visual, "geometry")

    # URDF visual geometry should contain a single primitive/mesh.
    for box in list(geometry.findall("box")):
        geometry.remove(box)
    for cylinder in list(geometry.findall("cylinder")):
        geometry.remove(cylinder)
    for sphere in list(geometry.findall("sphere")):
        geometry.remove(sphere)

    mesh = geometry.find("mesh")
    if mesh is None:
        mesh = ET.SubElement(geometry, "mesh")

    mesh.set("filename", f"{mesh_package_prefix}/meshes/{name}.stl")
    mesh.set("scale", "1. 1. 1.")


def _infer_hand_dimensions(input_root: ET.Element) -> dict[str, float]:
    dims = dict(DEFAULT_HAND_DIMS)

    right_hand = _find_element_by_name(input_root, "link", "RightHand")
    if right_hand is not None:
        for section_name in ("visual", "collision"):
            section = right_hand.find(section_name)
            if section is None:
                continue
            box = section.find("geometry/box")
            if box is None:
                continue
            size = _parse_xyz(box.get("size"))
            if size is not None:
                dims["X"], dims["Y"], dims["Z"] = size
                return dims

    def maybe_set_from_joint(joint_name: str, x_factor: float | None, y_factor: float | None, z_factor: float | None) -> None:
        joint = _find_element_by_name(input_root, "joint", joint_name)
        if joint is None:
            return
        origin = joint.find("origin")
        if origin is None:
            return
        xyz = _parse_xyz(origin.get("xyz"))
        if xyz is None:
            return
        if x_factor is not None and abs(xyz[0]) > 0:
            dims["X"] = abs(xyz[0]) * x_factor
        if y_factor is not None and abs(xyz[1]) > 0:
            dims["Y"] = abs(xyz[1]) * y_factor
        if z_factor is not None and abs(xyz[2]) > 0:
            dims["Z"] = abs(xyz[2]) * z_factor

    # Derived from scaleMuscleJoint formulas used by main.
    maybe_set_from_joint("jRightFlexCarp_RH", x_factor=5.0, y_factor=2.0, z_factor=2.0)
    maybe_set_from_joint("jLeftFlexCarp_LH", x_factor=5.0, y_factor=2.0, z_factor=2.0)
    maybe_set_from_joint("jRightExtCarp_RH", x_factor=5.0, y_factor=2.0, z_factor=2.0)

    # Fallback for hand length from hand COM joint.
    maybe_set_from_joint("jRightHandCOM", x_factor=None, y_factor=2.0, z_factor=None)
    maybe_set_from_joint("jLeftHandCOM", x_factor=None, y_factor=2.0, z_factor=None)

    return dims


def _finger_link_dimensions(hand_dims: dict[str, float]) -> dict[str, dict[str, float]]:
    palm_ratio = 0.45
    palm_length = palm_ratio * hand_dims["Y"]
    finger_reach = hand_dims["Y"] - palm_length

    dimensions = {}
    for finger_key, factor in FINGER_LENGTH_FACTORS.items():
        length_y = factor * finger_reach
        if "thumb" in finger_key:
            x_size = 0.22 * hand_dims["X"]
        elif "pinkie" in finger_key:
            x_size = 0.17 * hand_dims["X"]
        else:
            x_size = 0.19 * hand_dims["X"]
        z_size = 0.55 * hand_dims["Z"]
        dimensions[finger_key] = {"X": x_size, "Y": length_y, "Z": z_size}

    return dimensions


def _apply_finger_link_scaling(link: ET.Element, hand_dims: dict[str, float], mesh_package_prefix: str) -> None:
    name = link.get("name", "")
    if name.startswith(RIGHT_PREFIX):
        finger_key = name[len(RIGHT_PREFIX):]
        sign_y = -1.0
    elif name.startswith(LEFT_PREFIX):
        finger_key = name[len(LEFT_PREFIX):]
        sign_y = 1.0
    else:
        return

    dims = _finger_link_dimensions(hand_dims).get(finger_key)
    if dims is None:
        return

    _ensure_visual_mesh(link, mesh_package_prefix)

    y_offset = sign_y * dims["Y"] / 2.0
    _update_collision_box_size(link, dims["X"], dims["Y"], dims["Z"])

    inertial = link.find("inertial")
    if inertial is not None:
        _set_origin_xyz(inertial, [0.0, y_offset, 0.0])
    for section_name in ("visual", "collision"):
        section = link.find(section_name)
        if section is not None:
            _set_origin_xyz(section, [0.0, y_offset, 0.0])


def _finger_joint_origins(hand_dims: dict[str, float]) -> dict[str, list[float]]:
    palm_ratio = 0.45
    palm_length = palm_ratio * hand_dims["Y"]
    finger_reach = hand_dims["Y"] - palm_length

    joint_xyz = {}

    def set_side(prefix: str, sign_y: float, sign_x: float) -> None:
        hand_x = hand_dims["X"]
        hand_z = hand_dims["Z"]

        index_len = FINGER_CHAIN_TOTAL_FACTORS["index"] * finger_reach
        middle_len = FINGER_CHAIN_TOTAL_FACTORS["middle"] * finger_reach
        ring_len = FINGER_CHAIN_TOTAL_FACTORS["ring"] * finger_reach
        pinkie_len = FINGER_CHAIN_TOTAL_FACTORS["pinkie"] * finger_reach
        thumb_len = FINGER_CHAIN_TOTAL_FACTORS["thumb"] * finger_reach

        joint_xyz[f"{prefix}_index_add"] = [sign_x * 0.40 * hand_x, sign_y * palm_length, 0.0]
        joint_xyz[f"{prefix}_middle_add"] = [sign_x * 0.13 * hand_x, sign_y * palm_length, 0.0]
        joint_xyz[f"{prefix}_ring_add"] = [sign_x * -0.13 * hand_x, sign_y * palm_length, 0.0]
        joint_xyz[f"{prefix}_pinkie_add"] = [sign_x * -0.40 * hand_x, sign_y * palm_length, 0.0]
        joint_xyz[f"{prefix}_thumb_add"] = [sign_x * 0.46 * hand_x, sign_y * (0.10 * palm_length), 0.02 * hand_z]

        joint_xyz[f"{prefix}_index_prox"] = [0.0, sign_y * (0.45 * index_len), 0.0]
        joint_xyz[f"{prefix}_index_dist"] = [0.0, sign_y * (0.33 * index_len), 0.0]
        joint_xyz[f"{prefix}_middle_prox"] = [0.0, sign_y * (0.45 * middle_len), 0.0]
        joint_xyz[f"{prefix}_middle_dist"] = [0.0, sign_y * (0.33 * middle_len), 0.0]
        joint_xyz[f"{prefix}_ring_prox"] = [0.0, sign_y * (0.45 * ring_len), 0.0]
        joint_xyz[f"{prefix}_ring_dist"] = [0.0, sign_y * (0.33 * ring_len), 0.0]
        joint_xyz[f"{prefix}_pinkie_prox"] = [0.0, sign_y * (0.45 * pinkie_len), 0.0]
        joint_xyz[f"{prefix}_pinkie_dist"] = [0.0, sign_y * (0.33 * pinkie_len), 0.0]
        joint_xyz[f"{prefix}_thumb_prox"] = [0.0, sign_y * (0.20 * thumb_len), 0.0]
        joint_xyz[f"{prefix}_thumb_dist"] = [0.0, sign_y * (0.40 * thumb_len), 0.0]

    set_side("r", sign_y=-1.0, sign_x=1.0)
    set_side("l", sign_y=1.0, sign_x=1.0)
    return joint_xyz


def _apply_hand_link_scaling(input_root: ET.Element, hand_dims: dict[str, float]) -> None:
    palm_ratio = 0.45
    palm_length = palm_ratio * hand_dims["Y"]

    for hand_name, sign_y in (("RightHand", -1.0), ("LeftHand", 1.0)):
        hand_link = _find_element_by_name(input_root, "link", hand_name)
        if hand_link is None:
            continue

        y_offset = sign_y * palm_length / 2.0
        _update_box_size(hand_link, hand_dims["X"], palm_length, hand_dims["Z"])

        inertial = hand_link.find("inertial")
        if inertial is not None:
            _set_origin_xyz(inertial, [0.0, y_offset, 0.0])
        for section_name in ("visual", "collision"):
            section = hand_link.find(section_name)
            if section is not None:
                _set_origin_xyz(section, [0.0, y_offset, 0.0])

    # Keep the hand COM joints consistent with the resized palm.
    right_hand_com = _find_element_by_name(input_root, "joint", "jRightHandCOM")
    if right_hand_com is not None:
        _set_origin_xyz(right_hand_com, [0.0, -palm_length / 2.0, 0.0])

    left_hand_com = _find_element_by_name(input_root, "joint", "jLeftHandCOM")
    if left_hand_com is not None:
        _set_origin_xyz(left_hand_com, [0.0, palm_length / 2.0, 0.0])


def _apply_finger_joint_scaling(joint: ET.Element, hand_dims: dict[str, float]) -> None:
    name = joint.get("name", "")
    joint_positions = _finger_joint_origins(hand_dims)
    xyz = joint_positions.get(name)
    if xyz is None:
        return
    _set_origin_xyz(joint, xyz)


def _append_before_robot_end(original_text: str, xml_block: str) -> str:
    closing_tag = "</robot>"
    end_idx = original_text.rfind(closing_tag)
    if end_idx < 0:
        raise ValueError("Input URDF does not contain closing </robot> tag.")

    prefix = original_text[:end_idx].rstrip()
    suffix = original_text[end_idx:]
    return f"{prefix}\n\n{xml_block}\n{suffix}\n"


def convert_model(
    input_urdf: str,
    output_urdf: str,
    template_urdf: str,
    mesh_package_prefix: str = MESH_PACKAGE_PREFIX,
) -> tuple[int, int] | None:
    with open(input_urdf, "r", encoding="utf-8") as stream:
        input_text = stream.read()

    input_root = ET.fromstring(input_text)
    template_root = _load_xml_root(template_urdf, allow_hash_separators=True)

    input_links = _existing_names(input_root, "link")
    missing_required = REQUIRED_HAND_LINKS.difference(input_links)
    if missing_required:
        missing_str = ", ".join(sorted(missing_required))
        raise ValueError(
            "Input URDF does not contain required hand link(s): "
            f"{missing_str}."
        )

    if _has_existing_fingers(input_root):
        return None

    hand_dims = _infer_hand_dimensions(input_root)
    _apply_hand_link_scaling(input_root, hand_dims)

    finger_links, finger_joints = _extract_finger_elements(template_root)

    existing_link_names = _existing_names(input_root, "link")
    added_links = 0
    added_link_xml = []
    for link in finger_links:
        name = link.get("name")
        if name not in existing_link_names:
            _apply_finger_link_scaling(link, hand_dims, mesh_package_prefix)
            added_link_xml.append(ET.tostring(link, encoding="unicode"))
            existing_link_names.add(name)
            added_links += 1

    existing_joint_names = _existing_names(input_root, "joint")
    added_joints = 0
    added_joint_xml = []
    for joint in finger_joints:
        name = joint.get("name")

        parent_elem = joint.find("parent")
        child_elem = joint.find("child")
        parent = parent_elem.get("link") if parent_elem is not None else None
        child = child_elem.get("link") if child_elem is not None else None

        if name in existing_joint_names:
            continue
        if parent not in existing_link_names or child not in existing_link_names:
            continue

        _apply_finger_joint_scaling(joint, hand_dims)
        added_joint_xml.append(ET.tostring(joint, encoding="unicode"))
        existing_joint_names.add(name)
        added_joints += 1

    xml_blocks = []
    if added_link_xml:
        xml_blocks.append("  <!-- Added by convert_model_to_add_fingers.py: finger links -->")
        xml_blocks.extend(f"  {item}" for item in added_link_xml)
    if added_joint_xml:
        xml_blocks.append("  <!-- Added by convert_model_to_add_fingers.py: finger joints -->")
        xml_blocks.extend(f"  {item}" for item in added_joint_xml)

    core_tree = ET.ElementTree(input_root)
    ET.indent(core_tree, space="  ")
    serialized_core = ET.tostring(input_root, encoding="unicode")

    output_text = serialized_core
    if xml_blocks:
        output_text = _append_before_robot_end(serialized_core, "\n".join(xml_blocks))

    with open(output_urdf, "w", encoding="utf-8") as stream:
        stream.write(output_text)

    return added_links, added_joints


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a v1.0.2 URDF model to v2.0.0 by adding only the new "
            "hand/finger links and joints."
        )
    )
    parser.add_argument(
        "input_urdf",
        help="Path to the input URDF (v1.0.2 model).",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_urdf",
        default=None,
        help="Path to the output URDF. Default: <input_name>_fingers.urdf",
    )
    parser.add_argument(
        "-t",
        "--template",
        dest="template_urdf",
        default=_default_template_path(),
        help="Path to the v2.0.0 template URDF.",
    )
    parser.add_argument(
        "-m",
        "--mesh-package-prefix",
        dest="mesh_package_prefix",
        default=MESH_PACKAGE_PREFIX,
        help=(
            "Package prefix used for finger mesh filenames. The final mesh "
            "path directory is <--mesh-package-prefix>/meshes."
        ),
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    input_urdf = os.path.abspath(args.input_urdf)
    output_urdf = args.output_urdf
    if output_urdf is None:
        base, ext = os.path.splitext(input_urdf)
        output_urdf = f"{base}_fingers{ext or '.urdf'}"
    output_urdf = os.path.abspath(output_urdf)
    template_urdf = os.path.abspath(args.template_urdf)

    if not os.path.isfile(input_urdf):
        raise FileNotFoundError(f"Input URDF not found: {input_urdf}")
    if not os.path.isfile(template_urdf):
        raise FileNotFoundError(f"Template URDF not found: {template_urdf}")

    result = convert_model(
        input_urdf=input_urdf,
        output_urdf=output_urdf,
        template_urdf=template_urdf,
        mesh_package_prefix=args.mesh_package_prefix,
    )

    if result is None:
        print("[OUTPUT] Input already contains finger links/joints. No changes applied.")
        print("[OUTPUT] No output file has been generated.")
        return

    added_links, added_joints = result

    print("[OUTPUT] Conversion completed.")
    print(f"[OUTPUT] Added finger links: {added_links}")
    print(f"[OUTPUT] Added finger joints: {added_joints}")
    print(f"[OUTPUT] Saved converted URDF: {output_urdf}")


if __name__ == "__main__":
    main()
