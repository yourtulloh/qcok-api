from qbittorrentapi._version_support import Version
from qbittorrentapi.app import (
    AppAPIMixIn,
    ApplicationPreferencesDictionary,
    BuildInfoDictionary,
    NetworkInterface,
    NetworkInterfaceAddressList,
    NetworkInterfaceList,
)
from qbittorrentapi.auth import AuthAPIMixIn
from qbittorrentapi.client import Client
from qbittorrentapi.definitions import (
    APINames,
    TorrentState,
    TorrentStates,
    TrackerStatus,
)
from qbittorrentapi.exceptions import (
    APIConnectionError,
    APIError,
    Conflict409Error,
    FileError,
    Forbidden403Error,
    HTTP4XXError,
    HTTP5XXError,
    HTTP400Error,
    HTTP401Error,
    HTTP403Error,
    HTTP404Error,
    HTTP409Error,
    HTTP415Error,
    HTTP500Error,
    HTTPError,
    InternalServerError500Error,
    InvalidRequest400Error,
    LoginFailed,
    MissingRequiredParameters400Error,
    NotFound404Error,
    TorrentFileError,
    TorrentFileNotFoundError,
    TorrentFilePermissionError,
    Unauthorized401Error,
    UnsupportedMediaType415Error,
    UnsupportedQbittorrentVersion,
)
from qbittorrentapi.log import LogAPIMixIn, LogEntry, LogMainList, LogPeer, LogPeersList
from qbittorrentapi.request import Request
from qbittorrentapi.rss import RSSAPIMixIn, RSSitemsDictionary, RSSRulesDictionary
from qbittorrentapi.search import (
    SearchAPIMixIn,
    SearchCategoriesList,
    SearchCategory,
    SearchJobDictionary,
    SearchPlugin,
    SearchPluginsList,
    SearchResultsDictionary,
    SearchStatus,
    SearchStatusesList,
)
from qbittorrentapi.sync import (
    SyncAPIMixIn,
    SyncMainDataDictionary,
    SyncTorrentPeersDictionary,
)
from qbittorrentapi.torrents import (
    Tag,
    TagList,
    TorrentCategoriesDictionary,
    TorrentDictionary,
    TorrentFile,
    TorrentFilesList,
    TorrentInfoList,
    TorrentLimitsDictionary,
    TorrentPieceData,
    TorrentPieceInfoList,
    TorrentPropertiesDictionary,
    TorrentsAddPeersDictionary,
    TorrentsAPIMixIn,
    Tracker,
    TrackersList,
    WebSeed,
    WebSeedsList,
)
from qbittorrentapi.transfer import TransferAPIMixIn, TransferInfoDictionary

__all__ = (
    "APIConnectionError",
    "APIError",
    "APINames",
    "AppAPIMixIn",
    "ApplicationPreferencesDictionary",
    "AuthAPIMixIn",
    "BuildInfoDictionary",
    "Client",
    "Conflict409Error",
    "FileError",
    "Forbidden403Error",
    "HTTP400Error",
    "HTTP401Error",
    "HTTP403Error",
    "HTTP404Error",
    "HTTP409Error",
    "HTTP415Error",
    "HTTP4XXError",
    "HTTP500Error",
    "HTTP5XXError",
    "HTTPError",
    "InternalServerError500Error",
    "InvalidRequest400Error",
    "LogAPIMixIn",
    "LogEntry",
    "LoginFailed",
    "LogMainList",
    "LogPeer",
    "LogPeersList",
    "MissingRequiredParameters400Error",
    "NetworkInterface",
    "NetworkInterfaceList",
    "NetworkInterfaceAddressList",
    "NotFound404Error",
    "Request",
    "RSSAPIMixIn",
    "RSSitemsDictionary",
    "RSSRulesDictionary",
    "SearchAPIMixIn",
    "SearchCategoriesList",
    "SearchCategory",
    "SearchJobDictionary",
    "SearchPlugin",
    "SearchPluginsList",
    "SearchResultsDictionary",
    "SearchStatus",
    "SearchStatus",
    "SearchStatusesList",
    "SyncAPIMixIn",
    "SyncMainDataDictionary",
    "SyncTorrentPeersDictionary",
    "Tag",
    "TagList",
    "TorrentCategoriesDictionary",
    "TorrentDictionary",
    "TorrentFile",
    "TorrentFileError",
    "TorrentFileNotFoundError",
    "TorrentFilePermissionError",
    "TorrentFilesList",
    "TorrentInfoList",
    "TorrentLimitsDictionary",
    "TorrentPieceData",
    "TorrentPieceInfoList",
    "TorrentPropertiesDictionary",
    "TorrentsAddPeersDictionary",
    "TorrentsAPIMixIn",
    "TorrentState",
    "TorrentStates",
    "Tracker",
    "TrackersList",
    "TrackerStatus",
    "TransferAPIMixIn",
    "TransferInfoDictionary",
    "Unauthorized401Error",
    "UnsupportedMediaType415Error",
    "UnsupportedQbittorrentVersion",
    "Version",
    "WebSeed",
    "WebSeedsList",
)
