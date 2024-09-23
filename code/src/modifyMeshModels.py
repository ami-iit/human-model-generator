# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

from urchin import URDF, Link, Visual, Geometry, Mesh, Material

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
            scalingParam[link]["Y"], scalingParam[link]["Z"] = scalingParam[link]["Z"], scalingParam[link]["Y"]

    return scalingParam



def createScalingParamMesh(scalingParam, meshLinksName, mesh_name_mapping):
    scalingParamMesh = {}

    for meshLink in meshLinksName:
        key = mesh_name_mapping.get(meshLink)
        scalingParamMesh[meshLink] = scalingParam[key]

    return scalingParamMesh


def update_robot_with_mesh_and_muscles(
    scalingParamMesh, map_link_to_muscles, mesh_folder, robot
):

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
                        filename=f"{mesh_folder}\{link_name}.stl",
                        scale=[scale["X"], scale["Y"], scale["Z"]],
                        combine=False,
                    )
                ),
                origin=original_origin,
                material=Material(name="color"),
            )
            link.visuals = []  
            link.visuals.append(visual)  

        if link_name in map_link_to_muscles:
            muscles = map_link_to_muscles[link_name]
            for muscle in muscles:
                muscle_scale = scalingParamMesh[link_name]
                muscle_visual = Visual(
                    name=muscle,
                    geometry=Geometry(
                        mesh=Mesh(
                            filename=f"{mesh_folder}\{muscle}.stl",
                            scale=[
                                muscle_scale["X"],
                                muscle_scale["Y"],
                                muscle_scale["Z"],
                            ],
                            combine=False,
                        )
                    ),
                    origin=original_origin,
                    material=Material(name="muscle"),
                )
                link.visuals.append(
                    muscle_visual
                )  

    return robot
