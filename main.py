from __future__ import annotations

import os
from typing import Any

from citric import Client
from fastmcp import FastMCP


mcp = FastMCP("LimeSurvey")


# Helper function to create client
def get_client() -> Client:
    return Client(
        url=os.getenv("LIMESURVEY_URL"),
        username=os.getenv("LIMESURVEY_USERNAME"),
        password=os.getenv("LIMESURVEY_PASSWORD"),
    )


# Survey Resources
@mcp.resource("survey://{sid}")
def get_survey(sid: int) -> dict[str, Any]:
    """Get a LimeSurvey survey properties.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_survey_properties(sid)


@mcp.resource("survey://")
def list_surveys() -> list[dict[str, Any]]:
    """List all LimeSurvey surveys.

    Returns:
        A list of LimeSurvey surveys. Each survey is a dictionary with the following keys:
        - sid: The survey ID.
        - gsid: The survey group ID.
        - surveyls_title: The survey title.
        - startdate: The survey start date.
        - expires: The survey expiration date.
        - active: Whether the survey is active.
    """
    with get_client() as client:
        return client.list_surveys()


@mcp.resource("survey-group://")
def list_survey_groups() -> list[dict[str, Any]]:
    """List all LimeSurvey survey groups."""
    with get_client() as client:
        return client.list_survey_groups()


# Question Resources
@mcp.resource("question://{qid}")
def get_question(qid: int) -> dict[str, Any]:
    """Get a LimeSurvey question.

    Args:
        qid: The question ID.
    """
    with get_client() as client:
        return client.get_question_properties(qid)


@mcp.resource("questions://{sid}")
def list_questions(sid: int) -> list[dict[str, Any]]:
    """List all questions in a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.list_questions(sid)


# Group Resources
@mcp.resource("group://{gid}")
def get_group(gid: int) -> dict[str, Any]:
    """Get a LimeSurvey question group.

    Args:
        gid: The group ID.
    """
    with get_client() as client:
        return client.get_group_properties(gid)


@mcp.resource("groups://{sid}")
def list_groups(sid: int) -> list[dict[str, Any]]:
    """List all groups in a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.list_groups(sid)


# Participant Resources
@mcp.resource("participant://{token}/survey/{sid}")
def get_participant(token: str, sid: int) -> dict[str, Any]:
    """Get a LimeSurvey participant.

    Args:
        token: The participant token.
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_participant_properties(token, sid)


@mcp.resource("participants://{sid}")
def list_participants(sid: int) -> list[dict[str, Any]]:
    """List all participants in a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.list_participants(sid)


# Quota Resources
@mcp.resource("quota://{id}")
def get_quota(id: int) -> dict[str, Any]:
    """Get a LimeSurvey quota.

    Args:
        id: The quota ID.
    """
    with get_client() as client:
        return client.get_quota_properties(id)


@mcp.resource("quotas://{sid}")
def list_quotas(sid: int) -> list[dict[str, Any]]:
    """List all quotas in a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.list_quotas(sid)


# Response Resources
@mcp.resource("responses://{sid}")
def get_response_ids(sid: int) -> list[int]:
    """Get all response IDs for a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_response_ids(sid)


# Language Resources
@mcp.resource("language://{lid}")
def get_language(lid: str) -> dict[str, Any]:
    """Get language properties.

    Args:
        lid: The language ID.
    """
    with get_client() as client:
        return client.get_language_properties(lid)


@mcp.resource("language://")
def get_available_languages() -> list[str]:
    """Get available languages."""
    with get_client() as client:
        return client.get_available_languages()


@mcp.resource("language://default")
def get_default_language() -> str:
    """Get default language."""
    with get_client() as client:
        return client.get_default_language()


# Server Resources
@mcp.resource("server://version")
def get_server_version() -> str:
    """Get LimeSurvey server version."""
    with get_client() as client:
        return client.get_server_version()


@mcp.resource("server://db_version")
def get_db_version() -> str:
    """Get LimeSurvey database version."""
    with get_client() as client:
        return client.get_db_version()


@mcp.resource("server://site_name")
def get_site_name() -> str:
    """Get LimeSurvey site name."""
    with get_client() as client:
        return client.get_site_name()


@mcp.resource("server://users")
def list_users() -> list[dict[str, Any]]:
    """List LimeSurvey users."""
    with get_client() as client:
        return client.list_users()


# Field Resources
@mcp.resource("fieldmap://{sid}")
def get_fieldmap(sid: int) -> dict[str, Any]:
    """Get a survey fieldmap.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_fieldmap(sid)


@mcp.resource("summary://{sid}")
def get_summary(sid: int) -> dict[str, Any]:
    """Get a survey summary.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_summary(sid)


# File Resources
@mcp.resource("files://{sid}")
def get_uploaded_files(sid: int) -> dict[str, Any]:
    """Get uploaded files for a survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.get_uploaded_files(sid)


# Tools for operations that modify data
@mcp.tool()
def add_response(sid: int, response: dict) -> str:
    """Add a response to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        response: The response to add.
    """
    with get_client() as client:
        return client.add_response(sid, response)


@mcp.tool()
def add_responses(sid: int, responses: list[dict]) -> str:
    """Add multiple responses to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        responses: The responses to add.
    """
    with get_client() as client:
        return client.add_responses(sid, responses)


@mcp.tool()
def update_response(sid: int, response_id: int, response: dict) -> str:
    """Update a response in a LimeSurvey survey.

    Args:
        sid: The survey ID.
        response_id: The response ID.
        response: The updated response.
    """
    with get_client() as client:
        return client.update_response(sid, response_id, response)


@mcp.tool()
def delete_response(sid: int, response_id: int) -> bool:
    """Delete a response from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        response_id: The response ID.
    """
    with get_client() as client:
        return client.delete_response(sid, response_id)


@mcp.tool()
def save_responses(sid: int, data: dict[str, Any]) -> bool:
    """Save responses for a LimeSurvey survey.

    Args:
        sid: The survey ID.
        data: The response data to save.
    """
    with get_client() as client:
        return client.save_responses(sid, data)


@mcp.tool()
def export_responses(sid: int, file_format: str = "csv") -> str:
    """Export responses from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        file_format: The format to export (csv, json, etc).
    """
    with get_client() as client:
        return client.export_responses(sid, file_format=file_format).decode("utf-8")


@mcp.tool()
def export_statistics(sid: int, document_type: str = "pdf") -> str:
    """Export statistics for a LimeSurvey survey.

    Args:
        sid: The survey ID.
        document_type: The document type (pdf, xls, html).
    """
    with get_client() as client:
        return client.export_statistics(sid, document_type)


@mcp.tool()
def export_timeline(sid: int, start_date: str = None, end_date: str = None) -> str:
    """Export timeline for a LimeSurvey survey.

    Args:
        sid: The survey ID.
        start_date: The start date (YYYY-MM-DD).
        end_date: The end date (YYYY-MM-DD).
    """
    with get_client() as client:
        return client.export_timeline(sid, start_date, end_date)


@mcp.tool()
def add_survey(survey_data: dict[str, Any]) -> int:
    """Add a new LimeSurvey survey.

    Args:
        survey_data: The survey data.
    """
    with get_client() as client:
        return client.add_survey(survey_data)


@mcp.tool()
def copy_survey(sid: int, new_name: str) -> int:
    """Copy a LimeSurvey survey.

    Args:
        sid: The source survey ID.
        new_name: The name for the new survey.
    """
    with get_client() as client:
        return client.copy_survey(sid, new_name)


@mcp.tool()
def delete_survey(sid: int) -> bool:
    """Delete a LimeSurvey survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.delete_survey(sid)


@mcp.tool()
def activate_survey(sid: int) -> bool:
    """Activate a LimeSurvey survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.activate_survey(sid)


@mcp.tool()
def import_survey(survey_file: str, survey_name: str = None) -> int:
    """Import a LimeSurvey survey.

    Args:
        survey_file: The survey file content (base64 encoded).
        survey_name: The name for the imported survey.
    """
    with get_client() as client:
        return client.import_survey(survey_file, survey_name)


@mcp.tool()
def set_survey_properties(sid: int, properties: dict[str, Any]) -> bool:
    """Set LimeSurvey survey properties.

    Args:
        sid: The survey ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_survey_properties(sid, properties)


@mcp.tool()
def add_group(sid: int, group_data: dict[str, Any]) -> int:
    """Add a group to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        group_data: The group data.
    """
    with get_client() as client:
        return client.add_group(sid, group_data)


@mcp.tool()
def delete_group(sid: int, gid: int) -> bool:
    """Delete a group from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        gid: The group ID.
    """
    with get_client() as client:
        return client.delete_group(sid, gid)


@mcp.tool()
def set_group_properties(gid: int, properties: dict[str, Any]) -> bool:
    """Set LimeSurvey group properties.

    Args:
        gid: The group ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_group_properties(gid, properties)


@mcp.tool()
def import_group(sid: int, group_file: str, group_name: str = None) -> int:
    """Import a group to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        group_file: The group file content (base64 encoded).
        group_name: The name for the imported group.
    """
    with get_client() as client:
        return client.import_group(sid, group_file, group_name)


@mcp.tool()
def delete_question(qid: int) -> bool:
    """Delete a question from a LimeSurvey survey.

    Args:
        qid: The question ID.
    """
    with get_client() as client:
        return client.delete_question(qid)


@mcp.tool()
def set_question_properties(qid: int, properties: dict[str, Any]) -> bool:
    """Set LimeSurvey question properties.

    Args:
        qid: The question ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_question_properties(qid, properties)


@mcp.tool()
def import_question(sid: int, gid: int, question_file: str) -> int:
    """Import a question to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        gid: The group ID.
        question_file: The question file content (base64 encoded).
    """
    with get_client() as client:
        return client.import_question(sid, gid, question_file)


@mcp.tool()
def add_language(sid: int, language: str) -> bool:
    """Add a language to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        language: The language code.
    """
    with get_client() as client:
        return client.add_language(sid, language)


@mcp.tool()
def delete_language(sid: int, language: str) -> bool:
    """Delete a language from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        language: The language code.
    """
    with get_client() as client:
        return client.delete_language(sid, language)


@mcp.tool()
def set_language_properties(lid: str, properties: dict[str, Any]) -> bool:
    """Set LimeSurvey language properties.

    Args:
        lid: The language ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_language_properties(lid, properties)


@mcp.tool()
def add_participants(
    sid: int, participant_data: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Add participants to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        participant_data: The participant data.
    """
    with get_client() as client:
        return client.add_participants(sid, participant_data)


@mcp.tool()
def delete_participants(sid: int, tokens: list[str]) -> bool:
    """Delete participants from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        tokens: The participant tokens.
    """
    with get_client() as client:
        return client.delete_participants(sid, tokens)


@mcp.tool()
def invite_participants(sid: int, tokens: list[str] = None) -> dict[str, Any]:
    """Invite participants to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        tokens: The participant tokens. If None, invite all participants.
    """
    with get_client() as client:
        return client.invite_participants(sid, tokens)


@mcp.tool()
def set_participant_properties(
    token: str, sid: int, properties: dict[str, Any]
) -> bool:
    """Set LimeSurvey participant properties.

    Args:
        token: The participant token.
        sid: The survey ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_participant_properties(token, sid, properties)


@mcp.tool()
def import_cpdb_participants(sid: int, attributes: dict[str, Any]) -> dict[str, Any]:
    """Import participants from the central participant database.

    Args:
        sid: The survey ID.
        attributes: The attributes to filter participants.
    """
    with get_client() as client:
        return client.import_cpdb_participants(sid, attributes)


@mcp.tool()
def activate_tokens(sid: int) -> bool:
    """Activate tokens for a LimeSurvey survey.

    Args:
        sid: The survey ID.
    """
    with get_client() as client:
        return client.activate_tokens(sid)


@mcp.tool()
def add_quota(sid: int, quota_data: dict[str, Any]) -> int:
    """Add a quota to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        quota_data: The quota data.
    """
    with get_client() as client:
        return client.add_quota(sid, quota_data)


@mcp.tool()
def delete_quota(id: int) -> bool:
    """Delete a LimeSurvey quota.

    Args:
        id: The quota ID.
    """
    with get_client() as client:
        return client.delete_quota(id)


@mcp.tool()
def set_quota_properties(id: int, properties: dict[str, Any]) -> bool:
    """Set LimeSurvey quota properties.

    Args:
        id: The quota ID.
        properties: The properties to set.
    """
    with get_client() as client:
        return client.set_quota_properties(id, properties)


@mcp.tool()
def upload_file(sid: int, file_content: str, file_name: str) -> dict[str, Any]:
    """Upload a file to a LimeSurvey survey.

    Args:
        sid: The survey ID.
        file_content: The file content (base64 encoded).
        file_name: The file name.
    """
    with get_client() as client:
        return client.upload_file(sid, file_content, file_name)


@mcp.tool()
def download_files(sid: int, file_id: int = None) -> dict[str, Any]:
    """Download files from a LimeSurvey survey.

    Args:
        sid: The survey ID.
        file_id: The file ID. If None, download all files.
    """
    with get_client() as client:
        return client.download_files(sid, file_id)


if __name__ == "__main__":
    mcp.run()
