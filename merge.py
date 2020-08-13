from collections import namedtuple


def merge(*records):
    
    # :param records: (varargs list of namedtuple) The Patient details.
    # return: (namedtuple) named Patient, containing details from all records, in entry order.

    Patient = namedtuple('Patient', (PersonalDetails._fields + Complexion._fields))
    patient = Patient(*personal_details, *complexion)
    return patient


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth='06-04-1972')

Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color='Blue', hair_color='Black')

print(merge(personal_details, complexion))