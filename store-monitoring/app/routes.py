from flask import Blueprint, jsonify, request
import uuid
from .services import generate_report, check_report_status

bp = Blueprint('main', __name__)

@bp.route('/trigger_report', methods=['POST'])
def trigger_report():
    """
    Endpoint to trigger the generation of a report.

    This endpoint generates a unique report ID and initiates the report generation process.
    Returns the report ID in the response.

    ---
    tags:
      - Reports
    responses:
      200:
        description: The report ID is returned if the report is successfully triggered.
        content:
          application/json:
            schema:
              type: object
              properties:
                report_id:
                  type: string
                  example: "b7d62af4-3909-4e1b-9457-aa6c62ade19b"
    """
    report_id = str(uuid.uuid4())
    generate_report(report_id)
    return jsonify({"report_id": report_id}), 200

@bp.route('/get_report', methods=['GET'])
def get_report():
    """
    Endpoint to retrieve the status of a report.

    This endpoint checks the status of a report using the provided report ID.
    If the report is still being processed, it returns a "Running" status.
    If the report is complete, it returns a "Complete" status along with the report data.

    ---
    tags:
      - Reports
    parameters:
      - in: query
        name: report_id
        schema:
          type: string
        required: true
        description: The ID of the report whose status is to be retrieved.
    responses:
      200:
        description: The status of the report along with the data if completed.
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: "Running"
                data:
                  type: object
                  example: {"key": "value"}
    """
    report_id = request.args.get('report_id')
    status, data = check_report_status(report_id)
    if status == "Running":
        return jsonify({"status": "Running"}), 200
    else:
        return jsonify({"status": "Complete", "data": data}), 200
