# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

"""REANA Workflow Controller flask configuration."""

import os

SHARED_VOLUME_PATH = os.getenv('SHARED_VOLUME_PATH', '/reana')
"""Path to the mounted REANA shared volume."""

SQLALCHEMY_DATABASE_URI = 'sqlite:////reana/default/default.db'
"""SQLAlchemy database location"""

SQLALCHEMY_BINDS = {
    'alice': 'sqlite:///{path}'.format(
        path=os.path.join(SHARED_VOLUME_PATH, 'alice/alice.db')),
    'atlas': 'sqlite:///{path}'.format(
        path=os.path.join(SHARED_VOLUME_PATH, 'atlas/atlas.db')),
    'cms': 'sqlite:///{path}'.format(
        path=os.path.join(SHARED_VOLUME_PATH, 'cms/cms.db')),
    'lhcb': 'sqlite:///{path}'.format(
        path=os.path.join(SHARED_VOLUME_PATH, 'lhcb/lhcb.db')),
}
"""Organization databases"""

SQLALCHEMY_TRACK_MODIFICATIONS = False
"""Track modifications flag."""
