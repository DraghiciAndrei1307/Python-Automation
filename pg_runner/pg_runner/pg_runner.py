
"""
 This module was created to run simple PostgreSQL management procedures
"""

import os
from os_runner import OsRunner
import logging


class PgRunner:

    def __init__(self):
        self.os_runner = OsRunner()
        self.become_password = os.environ.get('BECOME_PASSWORD')

        # configure logging
        self.logging_path = os.environ.get('LOGGING_PATH')
        self.logger = logging.getLogger('pg_runner')
        self.logger.setLevel(logging.DEBUG)

        # clear existing handlers (avoid duplicates)
        self.logger.handlers.clear()

        # create console handler
        self.console_handler = logging.StreamHandler()

        # define and set formatter
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s: %(name)s: %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # set formatter
        self.console_handler.setFormatter(formatter)

        # add handler to logger
        self.logger.addHandler(self.console_handler)

        # configure file handler

        if self.logging_path:
            # create FileHandler
            self.file_handler = logging.FileHandler(self.logging_path)
            # set the same formatter for the FileHandler
            self.file_handler.setFormatter(formatter)
            # add the new FileHandler to the logger
            self.logger.addHandler(self.file_handler)


    def check_postgresql_status(self, version):
        """
        This method checks if the cluster is running or not.
        """

        result = self.os_runner.run_cmd(
            input_command='sudo -S systemctl status '
                    f'postgresql-{version}',
            input_data=f"{self.become_password}\n"
        )

        if 'Active: active (running)' in result['stdout']:
            self.logger.info(f"PostgreSQL 14 database server is ACTIVE.")
        else:
            self.logger.info(f"PostgreSQL 14 database server is INACTIVE.")

    def start_pg(self, version):
        """
        This method starts the cluster.
        """

        result = self.os_runner.run_cmd(
            input_command=f'sudo -S systemctl start postgresql-{version}',
            input_data=f"{self.become_password}\n"
        )

        if result['success']:
            self.logger.info(f"PostgreSQL 14 database server is UP and RUNNING.")
        else:
            self.logger.error(f"PostgreSQL 14 database encountered an error: {result['stderr']}")

    def stop_pg(self, version):
        """
        This method stops the cluster.
        """

        result = self.os_runner.run_cmd(
            input_command=f'sudo -S systemctl stop postgresql-{version}',
            input_data=f"{self.become_password}\n"
        )

        if result['success']:
            self.logger.info(f"PostgreSQL 14 database server is STOPPED.")
        else:
            self.logger.error(f"PostgreSQL 14 database encountered an error: {result['stderr']}")

    def backup_pg(self):
        """
        This method performs database backup.
        """

        result = self.os_runner.run_cmd(
            input_command='sudo -S -u postgres pgbackrest '
                    '--stanza=demo '
                    '--type=full '
                    '--log-level-console=info backup',
            input_data=f"{self.become_password}\n"
        )

        if result['success']:
            self.logger.info(f"PostgreSQL backup_pg: {result['stdout']}")
            print(result['stdout'])
        else:
            self.logger.error(f"PostgreSQL backup_pg: {result['stderr']}")
            print(result['stderr'])

    def backup_info(self):
        """
        This method checks the backup history.
        """

        result = self.os_runner.run_cmd(
            input_command='sudo -S -u postgres pgbackrest info',
            input_data=f"{self.become_password}\n"
        )

        if result['success']:
            self.logger.info(f"PostgreSQL backup_info: {result['stdout']}")
            print(result['stdout'])
        else:
            self.logger.error(f"PostgreSQL backup_info: {result['stderr']}")
            print(result['stderr'])

    def check_stanza(self):
        """
        This method checks the pgbackrest stanza.
        """
        result = self.os_runner.run_cmd(
            input_command='sudo -S -u postgres pgbackrest '
                    '--stanza=demo '
                    '--log-level-console=info '
                    'check',
            input_data=f"{self.become_password}\n"
        )

        if result['success']:
            self.logger.info(f"PostgreSQL check_stanza: {result['stdout']}")
            print(result['stdout'])
        else:
            self.logger.error(f"PostgreSQL check_stanza: {result['stderr']}")
            print(result['stderr'])
