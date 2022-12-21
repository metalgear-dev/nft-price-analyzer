import os
from logging import basicConfig, INFO, error
from logging.handlers import TimedRotatingFileHandler
import psycopg2


class PostgresHandler():
    def __init__(self, config) -> None:
        self.init_log(config)
        self.connect(config)

    def init_log(self, config):
        logpath = config['logo']['path']
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        follower_path = os.path.join(
            config['logo']['path'],
            'block_model_construct')
        if not os.path.exists(follower_path):
            os.mkdir(follower_path)
        self.log_path = follower_path

        logname = config['logo']['filename']

        # set rotate log files
        file_handler = TimedRotatingFileHandler(
            os.path.join(
                follower_path,
                logname),
            when='D',
            interval=1,
            backupCount=7,
            encoding='utf8')
        file_handler.suffix = "%Y%m%d%H00"
        basicConfig(
            level=INFO,
            format='Detector %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=(
                file_handler,
            ),
        )

    def connect(self, config):
        try:
            host = config['mysql']['host']
            db = config['mysql']['db']
            user = config['mysql']['user']
            pwd = config['mysql']['password']
            port = config['mysql']['port']
            self.conn = psycopg2.connect(
                host=host, database=db, user=user, password=pwd, port=port)
            self.cursor = self.conn.cursor()

        except Exception as e:
            error("While connecting to postgresql: {0} ...".format(e))
