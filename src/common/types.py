from dataclasses import dataclass, field


@dataclass
class BrowserStorage:
    group_name: str = "default"
    cookies: list[dict] = field(default_factory=lambda: [])
    local_storage: list[dict] = field(default_factory=lambda: [])


@dataclass
class Attachment:
    filename: str
    mimetype: str
    content: str
