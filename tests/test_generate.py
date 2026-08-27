# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

import xml.etree.ElementTree as ET

from humanmodelgenerator.generate import main


def test_generate_creates_valid_urdf(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    urdf_file_path = main(model_name="test_model")

    assert urdf_file_path.endswith("test_model.urdf")
    assert tmp_path.joinpath("humanModels", "test_model.urdf").exists()

    content = tmp_path.joinpath("humanModels", "test_model.urdf").read_text()
    assert content.strip() != ""

    # Well-formed XML smoke check
    ET.fromstring(content)
