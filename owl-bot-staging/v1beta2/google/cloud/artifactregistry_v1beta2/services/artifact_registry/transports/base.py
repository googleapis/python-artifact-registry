# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.artifactregistry_v1beta2.types import apt_artifact
from google.cloud.artifactregistry_v1beta2.types import file
from google.cloud.artifactregistry_v1beta2.types import package
from google.cloud.artifactregistry_v1beta2.types import repository
from google.cloud.artifactregistry_v1beta2.types import repository as gda_repository
from google.cloud.artifactregistry_v1beta2.types import settings
from google.cloud.artifactregistry_v1beta2.types import tag
from google.cloud.artifactregistry_v1beta2.types import tag as gda_tag
from google.cloud.artifactregistry_v1beta2.types import version
from google.cloud.artifactregistry_v1beta2.types import yum_artifact
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-artifact-registry',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class ArtifactRegistryTransport(abc.ABC):
    """Abstract transport class for ArtifactRegistry."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/cloud-platform.read-only',
    )

    DEFAULT_HOST: str = 'artifactregistry.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.import_apt_artifacts: gapic_v1.method.wrap_method(
                self.import_apt_artifacts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_yum_artifacts: gapic_v1.method.wrap_method(
                self.import_yum_artifacts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_repositories: gapic_v1.method.wrap_method(
                self.list_repositories,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_repository: gapic_v1.method.wrap_method(
                self.get_repository,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_repository: gapic_v1.method.wrap_method(
                self.create_repository,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.update_repository: gapic_v1.method.wrap_method(
                self.update_repository,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_repository: gapic_v1.method.wrap_method(
                self.delete_repository,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_packages: gapic_v1.method.wrap_method(
                self.list_packages,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_package: gapic_v1.method.wrap_method(
                self.get_package,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_package: gapic_v1.method.wrap_method(
                self.delete_package,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_versions: gapic_v1.method.wrap_method(
                self.list_versions,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_version: gapic_v1.method.wrap_method(
                self.get_version,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_version: gapic_v1.method.wrap_method(
                self.delete_version,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_files: gapic_v1.method.wrap_method(
                self.list_files,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_file: gapic_v1.method.wrap_method(
                self.get_file,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_tags: gapic_v1.method.wrap_method(
                self.list_tags,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_tag: gapic_v1.method.wrap_method(
                self.get_tag,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_tag: gapic_v1.method.wrap_method(
                self.create_tag,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.update_tag: gapic_v1.method.wrap_method(
                self.update_tag,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_tag: gapic_v1.method.wrap_method(
                self.delete_tag,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_project_settings: gapic_v1.method.wrap_method(
                self.get_project_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_project_settings: gapic_v1.method.wrap_method(
                self.update_project_settings,
                default_timeout=None,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def import_apt_artifacts(self) -> Callable[
            [apt_artifact.ImportAptArtifactsRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def import_yum_artifacts(self) -> Callable[
            [yum_artifact.ImportYumArtifactsRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_repositories(self) -> Callable[
            [repository.ListRepositoriesRequest],
            Union[
                repository.ListRepositoriesResponse,
                Awaitable[repository.ListRepositoriesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_repository(self) -> Callable[
            [repository.GetRepositoryRequest],
            Union[
                repository.Repository,
                Awaitable[repository.Repository]
            ]]:
        raise NotImplementedError()

    @property
    def create_repository(self) -> Callable[
            [gda_repository.CreateRepositoryRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_repository(self) -> Callable[
            [gda_repository.UpdateRepositoryRequest],
            Union[
                gda_repository.Repository,
                Awaitable[gda_repository.Repository]
            ]]:
        raise NotImplementedError()

    @property
    def delete_repository(self) -> Callable[
            [repository.DeleteRepositoryRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_packages(self) -> Callable[
            [package.ListPackagesRequest],
            Union[
                package.ListPackagesResponse,
                Awaitable[package.ListPackagesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_package(self) -> Callable[
            [package.GetPackageRequest],
            Union[
                package.Package,
                Awaitable[package.Package]
            ]]:
        raise NotImplementedError()

    @property
    def delete_package(self) -> Callable[
            [package.DeletePackageRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_versions(self) -> Callable[
            [version.ListVersionsRequest],
            Union[
                version.ListVersionsResponse,
                Awaitable[version.ListVersionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_version(self) -> Callable[
            [version.GetVersionRequest],
            Union[
                version.Version,
                Awaitable[version.Version]
            ]]:
        raise NotImplementedError()

    @property
    def delete_version(self) -> Callable[
            [version.DeleteVersionRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_files(self) -> Callable[
            [file.ListFilesRequest],
            Union[
                file.ListFilesResponse,
                Awaitable[file.ListFilesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_file(self) -> Callable[
            [file.GetFileRequest],
            Union[
                file.File,
                Awaitable[file.File]
            ]]:
        raise NotImplementedError()

    @property
    def list_tags(self) -> Callable[
            [tag.ListTagsRequest],
            Union[
                tag.ListTagsResponse,
                Awaitable[tag.ListTagsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_tag(self) -> Callable[
            [tag.GetTagRequest],
            Union[
                tag.Tag,
                Awaitable[tag.Tag]
            ]]:
        raise NotImplementedError()

    @property
    def create_tag(self) -> Callable[
            [gda_tag.CreateTagRequest],
            Union[
                gda_tag.Tag,
                Awaitable[gda_tag.Tag]
            ]]:
        raise NotImplementedError()

    @property
    def update_tag(self) -> Callable[
            [gda_tag.UpdateTagRequest],
            Union[
                gda_tag.Tag,
                Awaitable[gda_tag.Tag]
            ]]:
        raise NotImplementedError()

    @property
    def delete_tag(self) -> Callable[
            [tag.DeleteTagRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def set_iam_policy(self) -> Callable[
            [iam_policy_pb2.SetIamPolicyRequest],
            Union[
                policy_pb2.Policy,
                Awaitable[policy_pb2.Policy]
            ]]:
        raise NotImplementedError()

    @property
    def get_iam_policy(self) -> Callable[
            [iam_policy_pb2.GetIamPolicyRequest],
            Union[
                policy_pb2.Policy,
                Awaitable[policy_pb2.Policy]
            ]]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(self) -> Callable[
            [iam_policy_pb2.TestIamPermissionsRequest],
            Union[
                iam_policy_pb2.TestIamPermissionsResponse,
                Awaitable[iam_policy_pb2.TestIamPermissionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_project_settings(self) -> Callable[
            [settings.GetProjectSettingsRequest],
            Union[
                settings.ProjectSettings,
                Awaitable[settings.ProjectSettings]
            ]]:
        raise NotImplementedError()

    @property
    def update_project_settings(self) -> Callable[
            [settings.UpdateProjectSettingsRequest],
            Union[
                settings.ProjectSettings,
                Awaitable[settings.ProjectSettings]
            ]]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'ArtifactRegistryTransport',
)
