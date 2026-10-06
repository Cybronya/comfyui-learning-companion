r"""
LearningRecord → WorkflowDatabase 写入桥

「workflow_learning 学到了什么」与「database 存了什么」之间的翻译层。

分工（谁动谁的存储）：
    LearningStore（Markdown）  人读的学习记录，grep 友好，仍是记录正身
    WorkflowDatabase（JSON）   机器查询层：调度器判「学没学」、
                              归纳引擎取结构化经验，都走这里
    本桥                        每次写记录后把 LearningRecord 镜像进库

状态映射（LearningRecord.status → WorkflowRecord.status）：
    completed → learned       库的词汇是「已学习」
    failed / stale → 原样     都是「需要重学」的信号
    skipped → 不镜像          skip 不是一次学习结果，写进库反而
                              会把真实状态顶掉

「已学」的判定（is_learned）三条规则，少了哪条都会重蹈覆辙：
    1. 库里没有这条 → 返回 None（调用方回退查 Markdown，不猜）
    2. status 不是 learned → False（失败的文件必须能被重试）
    3. content_hash 对不上 → False（改了参数必须重学 ——
       registry.exists(name) 只看文件名的老坑，见 scheduler 模块头注释）
"""

from typing import Optional

from comfyui_library.database import WorkflowDatabase, WorkflowRecord

from .learning_record import (
    LearningRecord,
    STATUS_COMPLETED,
    STATUS_SKIPPED,
)

#: 库里的「已学习」状态值（completed 的镜像）
STATUS_LEARNED = "learned"

#: LearningRecord.status → WorkflowRecord.status
_STATUS_MAP = {
    STATUS_COMPLETED: STATUS_LEARNED,
}


def workflow_record_of(record: LearningRecord) -> WorkflowRecord:
    """
    把一条学习记录翻译成数据库的 WorkflowRecord
    """
    return WorkflowRecord(
        id=record.key,
        name=record.workflow_name,
        file_path=record.file_path,
        status=_STATUS_MAP.get(record.status, record.status),
        workflow_type=record.workflow_type,
        nodes=list(record.nodes),
        patterns=list(record.patterns),
        report=record.report_path,
        content_hash=record.content_hash,
    )


def experience_args_of(record: LearningRecord) -> dict:
    """
    把学习记录翻译成 ExperienceRepository.add 的关键字参数

    content 给人读（发现 + 问题摘要），data 给机器读
    （LearningRecord.to_dict() 全量结构化载荷）。
    """
    summary = list(record.discoveries)
    if record.error:
        summary.append(f"失败原因：{record.error}")
    issues = list(record.diagnostic_issues)
    if issues:
        summary.append("诊断：" + "；".join(issues[:4]))

    tags = [
        t for t in (record.workflow_type, record.source_kind) if t
    ]

    return {
        "content": "\n".join(summary),
        "tags": tags,
        "data": record.to_dict(),
    }


def sync_record(
    record: LearningRecord,
    database: WorkflowDatabase,
    verbose: bool = False,
) -> bool:
    # 单条镜像内也批量：WorkflowRepository.add 会对每个节点
    # register 一次，逐条落盘时 200 节点 = 200 次全量写 21MB
    prev = database.auto_save
    database.auto_save = False
    try:
        result = _sync_record_impl(record, database, verbose)
    finally:
        # 只有调用方没进批量模式时才在本条结束时落盘；
        # learn_folder / sync_all 会在整批结束后统一 save
        if prev:
            database.save()
        database.auto_save = prev
    return result


def _sync_record_impl(
    record: LearningRecord,
    database: WorkflowDatabase,
    verbose: bool = False,
) -> bool:
    """
    把一条学习记录镜像进数据库（workflow 记录 + 经验载荷）

    库写入失败只打印、不抛 —— 镜像是附加产物，
    不能让 Markdown 记录已经写成功的学习半途而废。

    Returns:
        是否镜像成功
    """
    if record.status == STATUS_SKIPPED:
        return False

    try:
        database.workflows.add(workflow_record_of(record))

        args = experience_args_of(record)
        database.experiences.add(record.key, **args)

        if verbose:
            print(f"  已同步到数据库：{record.key}")
        return True
    except Exception as e:
        print(f"同步学习记录到数据库失败（{record.key}）: {e}")
        return False


def sync_all(
    store,
    database: WorkflowDatabase,
    verbose: bool = False,
) -> dict:
    """
    全量镜像：把 LearningStore 的全部记录补进数据库

    用于存量记录的迁移（数据库是后建的，Markdown 记录先存在）。
    幂等：重复跑只是覆盖同 id 记录。

    Returns:
        {"synced": 成功条数, "skipped": 跳过条数, "failed": 失败条数}
    """
    synced = skipped = failed = 0

    # 批量迁移同理：关逐条落盘（库 20MB+ 时逐条全量写是主要瓶颈），
    # 结束统一 save 一次；异常也要落盘，不能丢整批
    database.auto_save = False
    try:
        for record in store.all_records():
            if record.status == STATUS_SKIPPED:
                skipped += 1
                continue
            if sync_record(record, database, verbose=verbose):
                synced += 1
            else:
                failed += 1
    finally:
        database.save()
        database.auto_save = True

    return {"synced": synced, "skipped": skipped, "failed": failed}


def is_learned(
    database: WorkflowDatabase,
    key: str,
    content_hash: str = "",
) -> Optional[bool]:
    """
    查库判断是否已学习

    Returns:
        True    已学且内容未变
        False   库里有记录但状态不是 learned，或内容指纹变了
        None    库里没有这条（或未接数据库）—— 调用方回退查 Markdown
    """
    if database is None:
        return None

    record = database.workflows.get(key)
    if record is None:
        return None

    if record.get("status") != STATUS_LEARNED:
        return False

    previous = record.get("content_hash", "")
    if previous and content_hash and previous != content_hash:
        return False

    return True
