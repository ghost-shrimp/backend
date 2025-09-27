from enum import Enum


class TaskStatus(str, Enum):
    open = "open"
    draft = "draft"
    closed = "closed"


class ApplicationStatus(str, Enum):
    accepted = "accepted"
    denied = "denied"
    waiting = "waiting"


class UserRole(str, Enum):
    user = "user"
    admin = "admin"
