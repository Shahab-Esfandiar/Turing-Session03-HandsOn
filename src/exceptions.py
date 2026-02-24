class EmailRouterBaseException(Exception):
    pass

class MissingConfigurationError(EmailRouterBaseException):
    pass

class LLMAnalysisError(EmailRouterBaseException):
    pass