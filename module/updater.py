import json
from urllib import error, request
import requests
from module.logger import logger
from module.config.config import AzurLaneConfig

class Update(object):

    def __init__(self, config):
        """
        Args:
            config(AzurLaneConfig):
        """
        self.config = config

    def check_update(self):
        main_commits = 'https://api.github.com/repos/LmeSzinc/AzurLaneAutoScript/commits/master'
        fork_commits = 'https://api.github.com/repos/whoamikyo/AzurLaneAutoScript/commits/master'

        # LmeSzinc commits
        l = requests.get(main_commits)
        main_commit_info = json.loads(l.content)

        # Whoamikyo fork commits
        w = requests.get(fork_commits)
        fork_commit_info = json.loads(w.content)

        _file = open('version.txt', 'r')
        local_version = _file.readline()

        if self.config.UPDATE_CHECK:

            try:
                with request.urlopen("https://raw.githubusercontent.com/LmeSzinc/AzurLaneAutoScript/master/version.txt") as m:
                    _m = m.read().decode('utf-8')
                    main_version = _m.splitlines()[1]
            except error.HTTPError as e:
                logger.error("Couldn't check for updates, {}.".format(e))

            else:

                try:
                    with request.urlopen("https://raw.githubusercontent.com/whoamikyo/AzurLaneAutoScript/master/version.txt") as f:
                        _f = f.read().decode('utf-8')
                        fork_version = _f.splitlines()[1]
                except error.HTTPError as e:
                    logger.error("Couldn't check for updates, {}.".format(e))

                if main_version != fork_version:
                    logger.warning("Current Version: " + local_version)
                    logger.warning("Current LmeSzinc version: " + main_version)
                    logger.warning("Current whoamikyo version: " + fork_version)
                    logger.warning('A new update is available, please run Easy_Install-V2.bat or check github')

                else:
                    logger.info('ALAS is up to date')
                    logger.info('Latest commit from\n%s - %s' % (main_commit_info['commit']['author']['name'], main_commit_info['commit']['message']))
                    logger.info('Latest commit from\n%s - %s' % (fork_commit_info['commit']['author']['name'], fork_commit_info['commit']['message']))

                    return True







