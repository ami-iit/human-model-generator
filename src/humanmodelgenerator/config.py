# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

"""Typed configuration for the human model generation library."""

import dataclasses
import importlib.util
import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Config:
    H: float = 1.665
    m: float = 59.0

    OPT_CHECK_CONSISTENCY_MODEL: bool = True
    OPT_VISUALIZZATION_MODEL: bool = False
    OPT_VISUALIZZATION_MEASUREOFCONTROL: bool = False
    OPT_VISUALIZATION_MESH: bool = True
    OPT_VISUALIZATION_MUSCLES: bool = True
    OPT_VISUALIZATION_SPINALCORD: bool = True

    OPT_COLOR_LINK_MESH: list = field(default_factory=lambda: [0.9922, 0.8667, 0.7922, 1.0])
    OPT_COLOR_MUSCLE_MESH: list = field(default_factory=lambda: [0.9922, 0.8667, 0.7922, 1.0])
    OPT_COLOR_SPINALCORD_MESH: list = field(default_factory=lambda: [0.9922, 0.8667, 0.7922, 1.0])


DEFAULT_CONFIG = Config()


def load_config_from_path(path: str) -> Config:
    """Build a Config by reading matching field names from an arbitrary .py file."""
    module_name = f"humanmodelgenerator._user_config_{os.path.basename(path).rsplit('.', 1)[0]}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load config file: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    overrides = {
        f.name: getattr(module, f.name)
        for f in dataclasses.fields(Config)
        if hasattr(module, f.name)
    }
    return dataclasses.replace(DEFAULT_CONFIG, **overrides)
