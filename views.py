import requests
from django.http import HttpResponse


def userdetails(api_url, headers, course_id, user_roles):
    user_data_url = f"{api_url}courses/{course_id}/users"
    response = requests.get(user_data_url, headers=headers, params={"enrollment_type[]": user_roles})

    if response.status_code == 200:
        return response.json()
    return []


def assigndetails(api_url, headers, course_id):
    assignurl = f"{api_url}courses/{course_id}/assignments"
    response = requests.get(assignurl, headers=headers)

    if response.status_code == 200:
        return response.json()
    return []


def status(api_url, headers, course_id, user_id):
    submission_url = f"{api_url}courses/{course_id}/submissions/{user_id}"
    response_submission = requests.get(submission_url, headers=headers)

    if response_submission.status_code == 200:
        submission_data = response_submission.json()
        work= submission_data.get('work')

        if work == 'graded' or work == 'submitted':
            return 'assignment submitted'
        else:
            return 'assignment not submitted'

    return 'assignment not submitted'  # Assume 'Not Submitted' if there's an issue with the API


def index(request):

    api_url = "https://canvas.instructure.com/api/v1/"
    headers = {"Authorization": "Bearer 7~XbJoKFTG5mR6Xh44EharQ5HbET55WSyl5z9xlCsNsSkkoSeVBvpIBTvuTJGIKMkP"}
    course_id = "7983411"
    user_roles = ["student"]

    user_info = userdetails(api_url, headers, course_id, user_roles)
    assignments_data = assigndetails(api_url, headers, course_id)



    result = []

    for user in user_info:
        uid, user_name = user['id'], user['name']
        assignments = []

        for assignment in assignments_data:
            assignment_name = assignment['name']
            submission_status = status(api_url, headers, course_id, uid)
            assignments.append({'Assignment Name': assignment_name, 'Submission Status': submission_status})

        result.append({'Student Name': user_name, 'Assignments': assignments})

    output = " User and course details: \n\n"

    for user in result:
        output += f"{user['Student Name']}\n"


        for assignment in user.get('Assignments', []):
            assignment_name = assignment.get('Assignment Name', 'Name not available')
            submitted_status = assignment.get('Submission Status', 'Not Submitted')
            output += f"   {assignment_name} --> {submitted_status}\n\n"


        output += "\n"

    return HttpResponse(output,content_type="text/plain")
