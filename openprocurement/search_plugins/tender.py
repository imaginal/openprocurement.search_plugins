# -*- coding: utf-8 -*-
import os
from logging import getLogger

from openprocurement.search.base_plugin import BasePlugin
from openprocurement.search.utils import get_now

logger = getLogger(__name__)



class SearchPlugin(BasePlugin):
    __name__ = __name__
    plugin_api_version = 2.0

    plugin_config = {
    }

    def __init__(self, config):
        pass

    def before_source_items(self, index):
        return
