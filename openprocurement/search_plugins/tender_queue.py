# -*- coding: utf-8 -*-
import os
from logging import getLogger

from openprocurement.search.base_plugin import BasePlugin
from openprocurement.search.utils import get_now, long_version

logger = getLogger(__name__)


class SearchPlugin(BasePlugin):
    __name__ = __name__
    plugin_api_version = 2.0

    config = {
        'tender_queue_file': '',
    }

    def __init__(self, config):
        for k in self.config.keys():
            if k in config:
                self.config[k] = config[k]

    def before_source_items(self, index):
        preload_items = []
        if self.config['tender_queue_file'] and os.path.exists(self.config['tender_queue_file']):
            logger.info("[tender_queue] Found queue file %s", self.config['tender_queue_file'])
            for line in open(self.config['tender_queue_file']):
                line = line.strip()
                if len(line) == 32:
                    preload_items.append({'id': line, 'dateModified': get_now().isoformat(), 'ignore_dateModified': 1})

            os.rename(self.config['tender_queue_file'], self.config['tender_queue_file'] + ".old")
            if preload_items:
                logger.info("[tender_queue] %d tender ids loaded from file", len(preload_items))

        return preload_items