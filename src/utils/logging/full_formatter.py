import logging


class FullFormatter(logging.Formatter):
    def format(self, record):
        timestamp = record.asctime
        levelname = record.levelname
        source = record.name
        message = record.message
        context = record.exc_info
        tags = record.tags

        return f"""
            Timestamp: {timestamp}
            Level: {levelname}
            Source: {source}
            Message: {message}
            Context: {context}
            Tags: {tags}
            """
