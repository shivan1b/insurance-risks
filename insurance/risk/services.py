from .models import RiskField


def get_type_map():
    '''
    Returns a dictionary containing a map of field type codes and their human
    readable values.
    '''
    type_map = dict()
    context = dict()
    for ftype in RiskField.FTYPE:
        context[ftype.value[1]] = list()
        type_map[ftype.value[0]] = ftype.value[1]

    return context, type_map


def get_risk_data_for_context(risk):
    '''
    Returns a dictionary of lists containing the type of field as the key and
    field names as the values of list.
    '''
    riskfield_qs = RiskField.objects.filter(risk=risk)
    context, type_map = get_type_map()

    for rf in riskfield_qs:
        rtype = type_map[rf.ftype]
        context[rtype].append(rf.name)

    return context
