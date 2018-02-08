from .base import C


def create_risk(**kwargs):
    return C('risk', 'Risk', **kwargs)


def create_riskfield(**kwargs):
    return C('risk', 'RiskField', **kwargs)
