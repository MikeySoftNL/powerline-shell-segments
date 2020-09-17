from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 8
    USERNAME_BG = 15
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 8  # dark grey
    PATH_FG = 7  # light grey
    CWD_FG = 15  # white
    SEPARATOR_FG = 7

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 1   # red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 8
    AWS_PROFILE_BG = 0

    AWS_CRED_VALID_FG = 8
    AWS_CRED_VALID_BG = 2
    AWS_CRED_EXP_FG = 8
    AWS_CRED_EXP_BG = 11

    AZ_PREFIX_FG = 0
    AZ_PREFIX_BG = 7

    EKS_BG = 8
    EKS_FG = 7

    ENV_FG = 8
    ENV_BG = 6

    KB_FG = 8
    KBUP_BG = 2
    KBDOWN_BG = 11

    LINUX_FG = 7
    LINUX_BG = 0

    TIME_FG = 8
    TIME_BG = 7
