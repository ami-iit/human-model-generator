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
    # Scorrere i link del robot
    for link in robot.links:
        link_name = link.name

        # Verifica se il link esiste in scalingParamMesh e applica la scala
        if link_name in scalingParamMesh:
            scale = scalingParamMesh[link_name]
            # Cerca se esiste una visualizzazione precedente e copia l'origin
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
            link.visuals = []  # Pulire eventuali visualizzazioni esistenti
            link.visuals.append(visual)  # Aggiungere la nuova visualizzazione

        # Verifica se ci sono muscoli associati al link in map_link_to_muscles
        if link_name in map_link_to_muscles:
            muscles = map_link_to_muscles[link_name]
            for muscle in muscles:
                # Aggiungi la visualizzazione per i muscoli
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
                )  # Aggiungere la visualizzazione del muscolo

    return robot
