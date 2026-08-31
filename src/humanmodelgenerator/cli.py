# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

"""Interactive/CLI front-end for the human model generation library."""

import argparse
import sys

from .config import DEFAULT_CONFIG, load_config_from_path
from .generate import generate_model


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="hmg-generate")
    parser.add_argument("-n", "--model-name", dest="model_name", help="Name of the generated model")
    parser.add_argument(
        "-c",
        "--config",
        dest="config_path",
        help="Path to a config.py to load (default: built-in defaults)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        help="Directory to write the URDF file to (default: ./humanModels)",
    )
    parser.add_argument(
        "-m",
        "--mesh-package-prefix",
        dest="mesh_package_prefix",
        help=(
            "Package prefix used for mesh filenames in the generated URDF. The final mesh "
            "path directory is <argument>/meshes (default: local absolute path to the built-in meshes)"
        ),
    )
    args = parser.parse_args(argv)

    model_name = args.model_name or input("\n[INPUT] Insert the model name: ")
    config = load_config_from_path(args.config_path) if args.config_path else DEFAULT_CONFIG

    generate_model(
        model_name,
        config=config,
        output_dir=args.output_dir,
        mesh_package_prefix=args.mesh_package_prefix,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
