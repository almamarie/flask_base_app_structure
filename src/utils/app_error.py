
class AppError(Exception):
    def __init__(self, message, statusCode: int) -> None:
        super().__init__(message)
        self.message = self.args[0]  # or  message
        self.statusCode = statusCode
        self.status = "fail" if "${statusCode}".startswith("4") else "error"
        self.isOperational = True
        self.stack = "TODO: Capturing stack trace not implemented"
        # TODO: figure out how to capture stack trace

    def serialize(self):
        return {"statusCode": self.statusCode,
                "status": self.status,
                "isOperational": self.isOperational,
                }
