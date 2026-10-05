"""
状态路径（唯一出处）

「哪些 workflow 学过了、学到了什么」这两个状态集中放在
`comfyui_library/workflows/learning/`，与 workflow 文件放在一起 ——
它们描述的就是这批 workflow，拆到 engine/ 下反而更难找。

为什么用 `learning` 子目录而不是直接放根下：
    WorkflowScanner 用 rglob 递归扫描目录，记录文件若直接放在
    workflows/ 根下，会被当成 workflow 拿去"学习"。
    放进子目录并登记进 SKIPPED_DIR_NAMES，扫描器就会明确跳过。
    （跳过判定用的是集合精确匹配而非下划线前缀，所以目录名不必带 `_`）

**存储格式：Markdown + frontmatter，一个 workflow 一个文件。**

    learning/
      index.md                      汇总索引（表格，一行一个 workflow）
      sd1.5/basic.md                该 workflow 的完整学习记录

选 Markdown 而非 JSON 的理由：
    1. **Agent 直接可读可查**。JSON 要先解析才知道有什么，
       Markdown 打开就是人话，`grep -r "LoraLoader" learning/`
       就能查出「哪些 workflow 用了这个节点」——这是 JSON 做不到的
    2. **git diff 可读**。JSON 每次重写都是整块变更，
       Markdown 只变改动的行
    3. **与知识卡规范一致**。comfyui_library/knowledge/**/*.md
       已有 frontmatter 约定（name/title/category/tags/updated），
       学习记录沿用同一套，不引入第二种格式

**所有需要读写这批状态的模块都从这里取路径，不要在各自文件里硬编码。**
"""

from pathlib import Path
from typing import List


# 仓库根。本文件在 engine/workflow_learning/ 下，上溯两级
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# workflow 样本目录
WORKFLOWS_DIR = PROJECT_ROOT / "comfyui_library" / "workflows"

# # 状态目录
STATE_DIR_NAME = "learning"
STATE_DIR = WORKFLOWS_DIR / STATE_DIR_NAME

# 汇总索引文件
INDEX_PATH = STATE_DIR / "index.md"

# 扫描器必须跳过的目录名
SKIPPED_DIR_NAMES = {STATE_DIR_NAME}

# 记录文件扩展名
RECORD_SUFFIX = ".md"


def relative_to_project(path) -> str:
    """
    转成相对仓库根的 posix 路径

    记录里存绝对路径会在换机器后全部失效，所以统一存相对路径。

    Args:
        path: 任意路径

    Returns:
        相对仓库根的字符串；不在仓库内则原样返回
    """
    try:
        return Path(path).resolve().relative_to(
            PROJECT_ROOT
        ).as_posix()
    except (ValueError, OSError):
        return str(path)


def ensure_state_dir() -> Path:
    """
    确保状态目录存在

    Returns:
        状态目录路径
    """
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    return STATE_DIR


def record_path_for(key: str) -> Path:
    """
    由 workflow 的相对路径推出记录文件路径

    key 是相对 workflows/ 的路径（如 `sd1.5/basic.json`），
    记录落在 `learning/sd1.5/basic.md` ——
    目录结构与源文件镜像，扫目录就能看出哪些 family 学过。

    Args:
        key: workflow 相对路径

    Returns:
        记录文件绝对路径
    """
    relative = str(key).replace("\\", "/")

    if relative.lower().endswith(".json"):
        relative = relative[:-5]
    elif relative.lower().endswith(".png"):
        relative = relative[:-4]

    return STATE_DIR / f"{relative}{RECORD_SUFFIX}"


def index_link_for(key: str) -> str:
    """
    索引表中指向记录文件的相对链接

    Args:
        key: workflow 相对路径

    Returns:
        相对 STATE_DIR 的 posix 链接，如 `sd1.5/basic.md`
    """
    return record_path_for(key).relative_to(
        STATE_DIR
    ).as_posix()
