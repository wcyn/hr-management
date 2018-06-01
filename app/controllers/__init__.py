
def format_error_message(error_data, status_code=400, message=None):
    error = {'error': {'details':error_data, 'message': message}}
    return error, status_code