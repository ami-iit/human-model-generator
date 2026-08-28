# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import os
import pathlib
import xml.etree.ElementTree as ET

from humanmodelgenerator.generate import generate_model


def test_generate_creates_valid_urdf(tmp_path):
    urdf_file_path = generate_model("test_model", output_dir=str(tmp_path))

    assert urdf_file_path.endswith("test_model.urdf")
    assert os.path.exists(urdf_file_path)

    content = pathlib.Path(urdf_file_path).read_text()
    assert content.strip() != ""
    ET.fromstring(content)  # raises if not well-formed XML

    # Well-formed XML smoke check
    ET.fromstring(content)
