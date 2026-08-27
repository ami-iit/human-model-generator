# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from urchin import URDF, Link, Visual, Geometry, Mesh, Material
import numpy as np
import os


def getScalingParam(linkDimensions, linkDimensions_norm):
    scalingParam = {}

    for key in linkDimensions:
        if key in linkDimensions_norm:
            scalingParam[key] = {}
            for dimension in ["X", "Y", "Z"]:
                norm_value = linkDimensions_norm[key].get(dimension, 0)
                link_value = linkDimensions[key].get(dimension, 0)
                scalingParam[key][dimension] = link_value / norm_value

    links_to_invert = ["Shoulder", "UpperArm", "ForeArm"]

    for link in links_to_invert:
        if link in scalingParam:
            scalingParam[link]["Y"], scalingParam[link]["Z"] = (
                scalingParam[link]["Z"],
                scalingParam[link]["Y"],
            )

    return scalingParam


def createScalingParamMesh(scalingParam, meshLinksName, mesh_name_mapping):
    scalingParamMesh = {}

    for meshLink in meshLinksName:
        key = mesh_name_mapping.get(meshLink)
        scalingParamMesh[meshLink] = scalingParam[key]

    return scalingParamMesh



def updateRobotWithMuscles(
    scalingParamMesh,
    map_link_to_muscles,
    mesh_folder,
    robot,
    OPT_COLOR_MUSCLE_MESH,
):

    robot.materials.clear()

    for link in robot.links:
        link_name = link.name
        if link_name in map_link_to_muscles:
            original_visual = link.visuals[0]
            original_origin = original_visual.origin
            muscles = map_link_to_muscles[link_name]
            for muscle in muscles:
                muscle_scale = scalingParamMesh[link_name]
                muscle_visual = Visual(
                    name=muscle,
                    geometry=Geometry(
                        mesh=Mesh(
                            filename=os.path.join(mesh_folder, f"{muscle}.stl"),
                            scale=[
                                muscle_scale["X"],
                                muscle_scale["Y"],
                                muscle_scale["Z"],
                            ],
                            combine=False,
                        )
                    ),
                    origin=original_origin,
                    material=Material(name="muscle", color=OPT_COLOR_MUSCLE_MESH),
                )
                link.visuals.append(muscle_visual)

    return robot

def updateRobotWithMesh(
    scalingParamMesh,
    mesh_folder,
    robot,
    OPT_COLOR_LINK_MESH,
):

    robot.materials.clear()

    for link in robot.links:
        link_name = link.name

        if link_name in scalingParamMesh:
            scale = scalingParamMesh[link_name]
            original_visual = link.visuals[0]
            original_origin = original_visual.origin

            visual = Visual(
                name=link_name,
                geometry=Geometry(
                    mesh=Mesh(
                        filename=os.path.join(mesh_folder, f"{link_name}.stl"),
                        scale=[scale["X"], scale["Y"], scale["Z"]],
                        combine=False,
                    )
                ),
                origin=original_origin,
                material=Material(name="Link", color=OPT_COLOR_LINK_MESH),
            )
            link.visuals = []
            link.visuals.append(visual)
            
    return robot


def updateRobotWithBones(
    scalingParamMesh,
    map_link_to_spinal_cord,
    URDF_MESHES_FILE_PATH,
    robot,
    OPT_COLOR_BONES_MESH,
):
    robot.materials.clear()

    for link in robot.links:
        link_name = link.name
        
        if link_name in map_link_to_spinal_cord:
            bone = map_link_to_spinal_cord.get(link_name)
            bone_scale = scalingParamMesh[link_name]
            original_visual = link.visuals[0]
            original_origin = original_visual.origin
            
            bone_visual = Visual(
                name=bone,
                geometry=Geometry(
                    mesh=Mesh(
                        filename=os.path.join(URDF_MESHES_FILE_PATH, f"{bone}.stl"),
                        scale=[bone_scale["X"], bone_scale["Y"], bone_scale["Z"]],
                        combine=False,
                    )
                ),
                origin=original_origin,
                material=Material(name="bone", color=OPT_COLOR_BONES_MESH),
            )
            link.visuals.append(bone_visual)
            # link.visuals.pop(0)
            
    
    return robot