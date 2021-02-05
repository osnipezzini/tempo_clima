def generate_response(status, message, content_name=False, content=False):
    response = {"status": status, "message": message}

    if content_name and content:
        response[content_name] = content

    return response
