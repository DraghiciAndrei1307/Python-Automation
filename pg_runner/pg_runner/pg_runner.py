
"""
 This module was created to run simple PostgreSQL management procedures
"""


from os_runner import OsRunner


class PgRunner:

    def __init__(self):
        self.os_runner = OsRunner()

    def check_postgresql_status(self, version):
        """
        This method checks if the cluster is running or not.
        """

        return self.os_runner.run_cmd(
            command='systemctl status '
                    f'postgresql-{version}'
        )

    def start_pg(self, version):
        """
        This method starts the cluster.
        """

        if self.check_postgresql_status(version):
            return self.os_runner.run_cmd(
                command=f'systemctl start postgresql-{version}'
            )

    def stop_pg(self, version):
        """
        This method stops the cluster.
        """

        return self.os_runner.run_cmd(
            command=f'systemctl stop postgresql-{version}'
        )

    def backup_pg(self):
        """
        This method performs database backup.
        """

        return self.os_runner.run_cmd(
            command='sudo -u postgres pgbackrest '
                    '--stanza=demo '
                    '--type=full '
                    '--log-level-console=info backup'
        )

    def backup_info(self):
        """
        This method checks the backup history.
        """

        return self.os_runner.run_cmd(
            command='sudo -u postgres pgbackrest info'
        )

    def check_stanza(self):
        """
        This method checks the pgbackrest stanza.
        """
        return self.os_runner.run_cmd(
            command='sudo -u postgres pgbackrest '
                    '--stanza=demo '
                    '--log-level-console=info '
                    'check'
        )
