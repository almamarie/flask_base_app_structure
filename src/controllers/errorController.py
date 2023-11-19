import copy
from ..utils.config import Config
from ..utils.AppError import AppError
from flask import jsonify
config = Config()


def error_controller(err):
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
