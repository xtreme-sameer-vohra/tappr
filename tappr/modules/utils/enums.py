from enum import Enum


class REGISTRY(str, Enum):
    GCR = "gcr"
    DOCKERHUB = "dockerhub"
    OTHER = "other"


class GITURL(str, Enum):
    GIT_SSH = "git@github.com"
    GIT_HTTPS = "https://github.com"
    GITLAB_VMWARE_SSH = "git@gitlab.eng.vmware.com"
    GITLAB_VMWARE_HTTPS = "https://gitlab.eng.vmware.com"
    OTHER = "other"


class PROJECT(str, Enum):
    APPS_PLUGIN = "apps-plugin"
    SOURCE_CONTROLLER = "source-controller"
    SERVICE_BINDINGS = "service-bindings"
    SPRINT_BOOT_CONVENTION = "sprint-boot-convention"


class OS(str, Enum):
    MAC = "darwin"
    LINUX = "linux"
    WIN = "windows"


class PROFILE(str, Enum):
    FULL = "full"
    FULL_SCAN = "full-scan"
    ITERATE_LOCAL = "iterate-local"
    ITERATE_SLIM = "iterate-slim"
    ITERATE_SCAN = "iterate-scan"
    ITERATE_ESSENTIALS = "iterate-essentials"
    ITERATE_LOCAL_ESSENTIALS = "iterate-local-essentials"
    ITERATE = "iterate"
    BUILD = "build"
    BUILD_SLIM = "build-slim"
    BUILD_ESSENTIALS = "build-essential"
    RUN = "run"
    RUN_LOCAL = "run-local"
    VIEW = "view"


class TEMPLATE(str, Enum):
    TEKTON_GRADLE_TEST = "tekton-gradle-test-pipeline"
    SCAN_POLICY = "scan-policy"


class GKE_RELEASE_CHANNELS(str, Enum):
    RAPID = "RAPID"
    REGULAR = "REGULAR"
    STABLE = "STABLE"
    NONE = "None"
