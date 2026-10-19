from atlassian import Jira, Confluence
from typing import Any, Dict, Optional
from ..configs import config


class JiraIssueClient:
    """
    CRUD client for Jira issues using atlassian-python-api.

    Jira Cloud:
        username = Atlassian account email
        api_token = Atlassian API token
    """

    def __init__(
            self,
            jira_url: str,
            username: str,
            api_token: str,
            cloud: bool = True
    ):
        self.jira = Jira(
            url=jira_url,
            username=username,
            password=api_token,
            cloud=cloud
        )

    def create_issue(
            self,
            project_key: str,
            summary: str,
            description: str,
            issue_type: str = "Task",
            extra_fields: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a Jira issue.

        Returns:
            Jira response containing the issue key and ID.
        """
        fields = {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": description,
            "assignee": {
                "accountId": "615857bb289a54006aee4fa0",
            },
            "issuetype": {
                "name": issue_type
            }
        }

        if extra_fields:
            fields.update(extra_fields)

        return self.jira.create_issue(fields=fields)

    def get_issue(
            self,
            issue_key: str
    ) -> Dict[str, Any]:
        response = self.jira.issue(
            issue_key,
            fields="summary,description,status,issuetype,project,assignee,priority"
        )

        if not isinstance(response, dict):
            raise RuntimeError(
                f"Unexpected Jira response for {issue_key}: {response}"
            )

        if "fields" not in response:
            error_messages = response.get("errorMessages", [])
            errors = response.get("errors", {})

            raise RuntimeError(
                f"Unable to retrieve Jira issue {issue_key}. "
                f"Messages: {error_messages}; Errors: {errors}"
            )

        return response

    def update_issue(
            self,
            issue_key: str,
            summary: Optional[str] = None,
            description: Optional[str] = None,
            extra_fields: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Update an existing Jira issue.
        """
        fields = {}

        if summary is not None:
            fields["summary"] = summary

        if description is not None:
            fields["description"] = description

        if extra_fields:
            fields.update(extra_fields)

        if not fields:
            raise ValueError("At least one field is required for update")

        return self.jira.issue_update(
            issue_key,
            fields=fields
        )

    def delete_issue(
            self,
            issue_key: str,
            recursive: bool = False
    ) -> Any:
        """
        Delete a Jira issue.
        """
        return self.jira.issue_delete(
            issue_key,
            recursive=recursive
        )

    def search_issues(
            self,
            jql: str,
            start: int = 0,
            limit: int = 50,
            fields: Optional[list[str]] = None
    ) -> Dict[str, Any]:
        """
        Search issues using JQL.
        """
        return self.jira.jql(
            jql=jql,
            start=start,
            limit=limit,
            fields=fields
        )

    def find_user(
            self,
            query: str,
            limit: int = 50
    ) -> list[dict]:
        """
        Search Jira Cloud users by display name or email.
        """
        response = self.jira.get(
            "rest/api/3/user/search",
            params={
                "query": query,
                "maxResults": limit
            }
        )

        if not isinstance(response, list):
            raise RuntimeError(f"User search failed: {response}")

        return response

_client = JiraIssueClient(
    jira_url="https://navinsworkspace-14765653.atlassian.net",
    username=config.ATLASSIAN_USERNAME,
    api_token=config.ATLASSIAN_TOKEN,
    cloud=True
)

def get_task():
    return _client.search_issues(
        'project = KAN AND assignee = "615857bb289a54006aee4fa0" ORDER BY created DESC',
        fields=["summary", "status", "assignee"]
    )
