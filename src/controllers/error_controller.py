import copy
from ..utils.config import Config
from ..utils.app_error import AppError
from flask import jsonify
from ...src.utils.logging.custom_logger import CustomLogger

config = Config()
logger_instance = CustomLogger()
logger = logger_instance.getLogger()


def error_controller(err):
    logger.error("An error occured: ", err)
    try:
        err.statusCode = err.statusCode or 500
        err.status = err.status or 'error'

        if config.FLASK_ENV == "development":
            return send_error_dev(err)

        elif config.FLASK_ENV == 'production':
            print(err)
            error = copy.copy(err)
            error.message = err.message
            return send_error_prod(err)
    except Exception:
        error = AppError('Something went very wrong!', 500)
        if config.FLASK_ENV == "development":
            return send_error_dev(err)
        elif config.FLASK_ENV == 'production':
            return send_error_prod(err)


def send_error_dev(err):
    return (jsonify({
        "status": err.status,
        "error": err.serialize(),
        "message": err.message,
        "stack": err.stack,
    }), err.statusCode)


def send_error_prod(err):
    if err.isOperational:
        return (jsonify({
            "status": err.status,
            "message": err.message,
        }), err.statusCode)

    else:
        return (jsonify({
            "status": 'error',
            "message": 'Something went very wrong!',
        }), 500)
