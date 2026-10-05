r"""
Learning Scheduler 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_learning_scheduler

-X utf8 必须加，否则中文输出乱码。
"""

import sys
import json
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.learning_scheduler import (
    LearningScheduler,
    LearningTask,
    TaskQueue,
    PriorityCalculator,
    SchedulerState,
    ScheduleStore,
    create_scheduler,
    STATUS_PENDING,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_ABANDONED,
)


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def sample_workflow(nodes, **params):
    return {
        "nodes": [
            {"id": i, "type": n, "widgets_values": []}
            for i, n in enumerate(nodes, 1)
        ],
        "links": [],
    }


BASE = ["CheckpointLoaderSimple", "CLIPTextEncode",
        "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"]


def build_fake_store(root):
    """
    构造一个空的 LearningStore 替身（只提供调度器用到的接口）
    """
    class FakeStore:
        def __init__(self):
            self.root = str(root)
            self.written = []
            self.records = []

        def exists(self, key, content_hash=None):
            return False

        def completed_records(self):
            return self.records

        def write(self, record):
            self.written.append(record)
            self.records.append(record)
            return f"{self.root}/{record.key}.md"

    return FakeStore()


def build_fake_learner(fail_keys=()):
    """
    构造一个假的 WorkflowLearner
    """
    from engine.workflow_learning import LearningRecord

    class FakeLearner:
        def __init__(self):
            self.calls = []

        def learn(self, path, key=""):
            self.calls.append(key)

            if key in fail_keys:
                return LearningRecord(
                    workflow_name=Path(path).stem,
                    file_path=str(path), key=key,
                    status="failed", error="模拟失败",
                )

            return LearningRecord(
                workflow_name=Path(path).stem,
                file_path=str(path), key=key,
                nodes=BASE, covered_nodes=BASE,
            )

    return FakeLearner()


def make_scheduler(tmp, store=None, learner=None, max_retries=3):
    from engine.workflow_learning import WorkflowScanner

    store = store or build_fake_store(Path(tmp) / "state")

    return LearningScheduler(
        scanner=WorkflowScanner(),
        store=store,
        learner=learner,
        queue=TaskQueue(max_retries=max_retries),
        schedule_store=ScheduleStore(str(Path(tmp) / "queue.md")),
    )


# ============================================================
# A. 优先级
# ============================================================

def test_priority_content_over_filename():
    """测试内容信号主导排序，文件名只作 tie-break"""
    print("=" * 60)
    print("测试 A1：优先级以内容为主")
    print("=" * 60)

    known_cards = {"CheckpointLoaderSimple", "CLIPTextEncode",
                   "EmptyLatentImage", "KSampler", "VAEDecode",
                   "SaveImage"}

    calc = PriorityCalculator(known_node_types=known_cards)

    # 名字里全是关键词但结构简单
    fancy_name = calc.calculate(
        {"name": "sdxl_controlnet_lora_final"},
        nodes=["KSampler"],
    )
    # 名字平平但结构复杂、且有一堆没卡的节点
    plain_name = calc.calculate(
        {"name": "a"},
        nodes=BASE + ["WanVideoSampler", "VHS_VideoCombine",
                      "IPAdapterApply", "FaceDetailer"],
    )

    print(f"  sdxl_controlnet_lora_final（1 节点）: {fancy_name['score']}")
    print(f"    理由: {fancy_name['reasons']}")
    print(f"  a（10 节点，4 个缺卡）: {plain_name['score']}")
    print(f"    理由: {plain_name['reasons']}")

    assert plain_name["score"] > fancy_name["score"], \
        "结构复杂 + 缺口大的应排在前面，与文件名无关"
    assert plain_name["unknown_node_count"] == 4
    # 缺卡节点是主要加分项
    assert any("缺知识卡" in r for r in plain_name["reasons"])

    print("内容主导排序正确 [OK]\n")


def test_priority_reasons_explainable():
    """测试排序理由可解释（调度必须可调试）"""
    print("=" * 60)
    print("测试 A2：排序理由")
    print("=" * 60)

    calc = PriorityCalculator(known_node_types={"KSampler"})

    scored = calc.calculate(
        {"name": "controlnet_test"},
        nodes=["KSampler", "IPAdapterApply", "LoraLoader"],
        retry_count=2,
        content_changed=True,
    )

    print(f"  分数 {scored['score']}")
    for r in scored["reasons"]:
        print(f"    - {r}")

    joined = " ".join(scored["reasons"])
    assert "节点" in joined
    assert "缺知识卡" in joined
    assert "曾失败 2 次" in joined
    assert "内容已变更" in joined
    assert "文件名含 controlnet" in joined
    # 文件名应被标为弱信号
    assert any("弱信号" in r for r in scored["reasons"])

    print("理由可解释 [OK]\n")


def test_priority_novelty():
    """测试新颖度"""
    print("=" * 60)
    print("测试 A3：新颖度")
    print("=" * 60)

    calc = PriorityCalculator(known_node_types=set(BASE))

    scored = calc.calculate(
        {"name": "x"}, nodes=BASE + ["BrandNewNode"]
    )
    print(f"  含 1 个未见节点: {scored['score']} 分")
    print(f"  理由: {scored['reasons']}")
    assert any("未见过" in r for r in scored["reasons"])

    # 全部见过则无新颖度加分
    seen_all = calc.calculate({"name": "x"}, nodes=BASE)
    assert not any("未见过" in r for r in seen_all["reasons"])

    print("新颖度正确 [OK]\n")


# ============================================================
# B. 队列
# ============================================================

def test_queue_ordering_and_dedup():
    """测试队列排序与去重"""
    print("=" * 60)
    print("测试 B1：队列排序去重")
    print("=" * 60)

    queue = TaskQueue()
    low = queue.add(LearningTask(
        workflow_path="a.json", workflow_name="a", key="a.json",
        priority=5,
    ))
    high = queue.add(LearningTask(
        workflow_path="b.json", workflow_name="b", key="b.json",
        priority=50,
    ))

    print(f"  队列: {[(t.key, t.priority) for t in queue]}")
    assert queue.get_next() is high, "优先级高的先出队"
    assert len(queue) == 2

    # 同 key 重复加入应更新而非追加
    again = queue.add(LearningTask(
        workflow_path="a.json", workflow_name="a", key="a.json",
        priority=99,
    ))
    print(f"  重复加入 a.json 后: {[(t.key, t.priority) for t in queue]}")
    assert len(queue) == 2, "同 key 不应重复入队"
    assert again is low, "应返回已存在的那条"
    assert low.priority == 99, "优先级应被更新"

    # 同分时保持加入顺序（稳定）
    queue2 = TaskQueue()
    first = queue2.add(LearningTask(workflow_path="1", workflow_name="1",
                                   key="1", priority=10))
    second = queue2.add(LearningTask(workflow_path="2", workflow_name="2",
                                    key="2", priority=10))
    print(f"  同分顺序: {queue2.get_next().key}")
    assert queue2.get_next().key == "1", "同分应按加入顺序，可复现"

    print("排序与去重正确 [OK]\n")


def test_queue_reset():
    """测试 reset（设计稿里没有，会累积重复任务）"""
    print("=" * 60)
    print("测试 B2：队列重置")
    print("=" * 60)

    queue = TaskQueue()
    queue.add(LearningTask(workflow_path="a", workflow_name="a", key="a"))
    queue.reset()
    assert len(queue) == 0

    print("重置正确 [OK]\n")


def test_retry_isolation():
    """测试重试上限（无限重试 = 调度器死锁）"""
    print("=" * 60)
    print("测试 B3：重试上限")
    print("=" * 60)

    queue = TaskQueue(max_retries=2)
    task = queue.add(LearningTask(
        workflow_path="bad.json", workflow_name="bad", key="bad.json",
    ))

    print(f"  初始: {task.status}, retry={task.retry_count}")

    queue.pop_next()
    queue.fail(task, "JSON 解析失败")
    print(f"  第 1 次失败: {task.status}, retry={task.retry_count}")
    assert task.status == STATUS_FAILED

    queue.pop_next()
    queue.fail(task, "JSON 解析失败")
    print(f"  第 2 次失败: {task.status}, retry={task.retry_count}")
    assert task.status == STATUS_ABANDONED, "用尽重试应转 abandoned"

    # abandoned 不再参与调度，否则队列永远卡住
    assert queue.get_next() is None, "放弃的任务不该再被取出"
    assert queue.runnable_count() == 0

    reasons = queue.abandoned_reasons()
    print(f"  放弃原因: {reasons}")
    assert "bad.json" in reasons
    assert "JSON" in reasons["bad.json"]

    print("重试隔离正确 [OK]\n")


def test_queue_progress():
    """测试进度统计"""
    print("=" * 60)
    print("测试 B4：进度统计")
    print("=" * 60)

    queue = TaskQueue()
    for i, status in enumerate([
        "completed", "completed", "skipped",
        "failed", "abandoned", "pending",
    ]):
        queue.add(LearningTask(
            workflow_path=f"{i}", workflow_name=str(i), key=str(i),
            status=status,
        ))

    stats = queue.progress()
    print(f"  统计: {stats}")

    assert stats["total"] == 6
    assert stats["completed"] == 2
    assert stats["skipped"] == 1
    assert stats["failed"] == 1
    assert stats["abandoned"] == 1
    assert stats["pending"] == 1
    # done 含 completed + skipped
    assert stats["done"] == 3
    assert abs(stats["percent"] - 50.0) < 0.1

    print("进度统计正确 [OK]\n")


# ============================================================
# C. 调度器
# ============================================================

def test_build_schedule_skips_learned():
    """测试跳过已学 + 内容变更触发重学"""
    print("=" * 60)
    print("测试 C1：跳过已学")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        for name in ["a", "b"]:
            write_json(wf_dir / f"{name}.json", sample_workflow(BASE))

        store = build_fake_store(Path(tmp) / "state")

        # a.json 已学且内容未变
        store.exists = lambda key, h=None: key == "a.json"

        scheduler = make_scheduler(tmp, store=store)

        plan = scheduler.plan(str(wf_dir))
        keys = [p["key"] for p in plan]

        print(f"  计划: {keys}")
        assert "a.json" not in keys, "已学应跳过"
        assert "b.json" in keys, "未学应入队"

        # 内容指纹变了 → 应重新入队
        store.exists = lambda key, h=None: False
        plan2 = scheduler.plan(str(wf_dir))
        assert len(plan2) == 2, "内容变更应触发重学"

    print("跳过已学正确 [OK]\n")


def test_plan_shape():
    """测试学习计划输出（对应设计稿第十节）"""
    print("=" * 60)
    print("测试 C2：学习计划输出")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        write_json(wf_dir / "a.json", sample_workflow(BASE))
        write_json(wf_dir / "b_controlnet.json",
                   sample_workflow(BASE + ["ControlNetApply"]))
        write_json(wf_dir / "c_sdxl.json",
                   sample_workflow(BASE + ["ControlNetApply",
                                           "LoraLoader"]))

        scheduler = make_scheduler(tmp)
        plan = scheduler.plan(str(wf_dir))

        print()
        for item in plan:
            print(f"  {item['key']}: priority={item['priority']} "
                  f"status={item['status']}")
            for r in item["reasons"]:
                print(f"      - {r}")
        print()

        assert len(plan) == 3
        # 优先级降序
        priorities = [p["priority"] for p in plan]
        assert priorities == sorted(priorities, reverse=True), \
            f"应按优先级降序: {priorities}"
        # 节点最多的排最前
        assert plan[0]["key"] == "c_sdxl.json", \
            f"节点最多的应排最前，实际 {plan[0]['key']}"
        # 每项都带理由
        assert all(p["reasons"] for p in plan)
        # 状态统一为 pending
        assert all(p["status"] == STATUS_PENDING for p in plan)

    print("计划输出正确 [OK]\n")


def test_run_executes_and_records():
    """测试执行循环（设计稿里缺失的部分）"""
    print("=" * 60)
    print("测试 C3：执行循环")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        for name in ["a", "b", "c"]:
            write_json(wf_dir / f"{name}.json", sample_workflow(BASE))

        store = build_fake_store(Path(tmp) / "state")
        learner = build_fake_learner(fail_keys=("c.json",))
        scheduler = make_scheduler(tmp, store=store, learner=learner)

        state = scheduler.run(str(wf_dir))

        print(f"  {state.summary()}")
        print(f"  成功率: {state.success_rate:.0%}")
        print(f"  learner 调用: {learner.calls}")
        print(f"  记录落盘: {[r.key for r in store.written]}")

        assert state.total_tasks == 3
        assert state.completed == 2, f"应完成 2 个，实际 {state.completed}"
        assert state.failed == 1, f"应失败 1 个，实际 {state.failed}"
        assert len(learner.calls) == 3, "每个任务都该被执行一次"
        assert len(store.written) == 2, "成功的应落 LearningStore"
        assert state.elapsed_ms > 0

    print("执行循环正确 [OK]\n")


def test_error_isolation():
    """测试单个任务异常不中断整批"""
    print("=" * 60)
    print("测试 C4：异常隔离")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        for name in ["a", "b", "c"]:
            write_json(wf_dir / f"{name}.json", sample_workflow(BASE))

        learner = build_fake_learner()

        # 让 a 直接抛异常（模拟文件被占用、内存错误等）
        original = learner.learn
        def flaky(path, key=""):
            if key == "a.json":
                raise PermissionError("文件被占用")
            return original(path, key=key)

        learner.learn = flaky

        store = build_fake_store(Path(tmp) / "state")
        scheduler = make_scheduler(tmp, store=store, learner=learner)

        state = scheduler.run(str(wf_dir))

        print(f"  {state.summary()}")
        print(f"  失败: {state.failed_keys}")
        print(f"  完成: {state.completed_keys}")
        print(f"  learner 实际调用: {learner.calls}")

        # 关键：a 炸了不影响 b、c
        assert state.completed == 2, \
            f"异常不应影响其他任务，实际完成 {state.completed}"
        assert "a.json" in state.failed_keys
        # flaky 在 a 上先抛异常，不会进入 original，所以 calls 只有 b、c
        assert len(learner.calls) == 2, \
            f"a 抛异常前未记录，实际 {learner.calls}"
        assert learner.calls == ["b.json", "c.json"]

        # a 的错误信息应被保留，供下次 run 重试与排查
        failed_task = scheduler.queue.find("a.json")
        assert failed_task is not None
        assert "PermissionError" in failed_task.last_error, \
            f"异常信息应保留: {failed_task.last_error!r}"
        assert failed_task.retry_count == 1

    print("异常隔离正确 [OK]\n")


def test_store_markdown_roundtrip():
    """测试队列 Markdown 落盘与读回（续跑依赖它）"""
    print("=" * 60)
    print("测试 C5：队列落盘与续跑")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        queue_file = str(Path(tmp) / "queue.md")

        queue = TaskQueue(max_retries=2)
        done = queue.add(LearningTask(
            workflow_path="a.json", workflow_name="a", key="sd1.5/a.json",
            priority=30, node_count=7, unknown_node_count=1,
        ))
        queue.complete(done, "ok")

        failed = queue.add(LearningTask(
            workflow_path="b.json", workflow_name="b",
            key="flux/b.json", priority=50,
            node_count=9, unknown_node_count=4,
        ))
        queue.fail(failed, "JSON 解析失败")

        pending = queue.add(LearningTask(
            workflow_path="c.json", workflow_name="c",
            key="sdxl/c.json", priority=20, node_count=6,
        ))

        state = SchedulerState.from_queue(queue)
        store = ScheduleStore(queue_file)
        path = store.save(queue.tasks, state, folder="comfyui_library/workflows")

        assert Path(path).exists()
        text = Path(path).read_text(encoding="utf-8")
        print()
        print("\n".join(text.split("\n")[:26]))
        print()

        assert text.startswith("---")
        assert "sd1.5/a.json" in text
        assert "JSON 解析失败" in text
        assert "失败待重试" in text, "待重试任务应单独说明"

        # 重试用尽的应进「需要人工处理」
        queue.fail(failed, "JSON 解析失败")
        state2 = SchedulerState.from_queue(queue)
        text2 = ScheduleStore(queue_file).render(queue.tasks, state2)
        assert "需要人工处理" in text2
        assert "已放弃" in text2

        # 读回
        loaded = store.load()
        print(f"  读回 {len(loaded)} 个任务:")
        for t in loaded:
            print(f"    {t.key}: p={t.priority} {t.status} "
                  f"retry={t.retry_count} err={t.last_error!r}")

        assert len(loaded) == 3
        by_key = {t.key: t for t in loaded}

        assert by_key["sd1.5/a.json"].status == "completed"
        assert by_key["sd1.5/a.json"].node_count == 7
        # 关键：重试次数与错误必须恢复，否则续跑会无限重试
        assert by_key["flux/b.json"].status == "failed"
        assert by_key["flux/b.json"].retry_count == 1, \
            f"重试次数应恢复，实际 {by_key['flux/b.json'].retry_count}"
        assert "JSON" in by_key["flux/b.json"].last_error
        assert by_key["sdxl/c.json"].status == "pending"

        # frontmatter 整体统计
        meta = store.load_meta()
        print(f"  frontmatter: {meta}")
        assert meta["total"] == "3"
        assert meta["failed"] == "1"

    print("落盘与读回正确 [OK]\n")


def test_retry_across_runs():
    """测试重试发生在多次 run 之间（一次 run 只过一遍）"""
    print("=" * 60)
    print("测试 C5b：跨次重试")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        write_json(wf_dir / "bad.json", sample_workflow(BASE))

        store = build_fake_store(Path(tmp) / "state")
        # 永远失败
        learner = build_fake_learner(fail_keys=("bad.json",))
        scheduler = make_scheduler(
            tmp, store=store, learner=learner, max_retries=2
        )

        # 第 1 次 run：只尝试一次，retry=1，保持 failed
        scheduler.run(str(wf_dir))
        task = scheduler.queue.find("bad.json")
        print(f"  run1: {task.status} retry={task.retry_count}")
        assert task.status == "failed", \
            "一次 run 内不该把重试耗尽"
        assert task.retry_count == 1

        # 第 2 次 run：再试一次，用尽后转 abandoned
        scheduler.run(str(wf_dir))
        print(f"  run2: {task.status} retry={task.retry_count}")
        assert task.retry_count == 2
        assert task.status == "abandoned", \
            f"重试用尽应转 abandoned，实际 {task.status}"

        # 第 3 次 run：abandoned 不再被调度
        learner.calls.clear()
        scheduler.run(str(wf_dir))
        print(f"  run3 后 learner 调用: {learner.calls}")
        assert learner.calls == [], "abandoned 不该再被尝试"

    print("跨次重试正确 [OK]\n")


def test_run_without_learner():
    """测试未注入 learner 时只能建计划"""
    print("=" * 60)
    print("测试 C6：缺 learner")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        write_json(wf_dir / "a.json", sample_workflow(BASE))

        scheduler = make_scheduler(tmp, learner=None)

        # 建计划可以
        plan = scheduler.plan(str(wf_dir))
        assert len(plan) == 1

        # 执行应明确报错
        try:
            scheduler.run(str(wf_dir))
            raise AssertionError("未注入 learner 应报错")
        except RuntimeError as e:
            print(f"  捕获: {e}")

    print("缺 learner 处理正确 [OK]\n")


def test_render_plan_and_progress():
    """测试可读输出"""
    print("=" * 60)
    print("测试 C7：可读输出")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        wf_dir = Path(tmp) / "workflows"
        write_json(wf_dir / "a.json", sample_workflow(BASE))
        write_json(
            wf_dir / "b.json",
            sample_workflow(BASE + ["IPAdapterApply", "FaceDetailer"]),
        )

        scheduler = make_scheduler(tmp)
        text = scheduler.render_plan(str(wf_dir))
        print(text)

        assert "学习计划" in text
        assert "a.json" in text and "b.json" in text
        assert "节点" in text, "应展示排序理由"

        progress = scheduler.progress()
        assert progress.total_tasks == 2
        print(f"\n  {progress.summary()}")
        print(f"  空队列: {LearningScheduler.render_plan.__doc__ is not None}")

    print("可读输出正确 [OK]\n")


def test_empty_directory():
    """测试空目录与全已学"""
    print("=" * 60)
    print("测试 C8：空目录")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        empty = Path(tmp) / "empty"
        empty.mkdir()

        scheduler = make_scheduler(tmp)
        plan = scheduler.plan(str(empty))
        assert plan == []

        text = scheduler.render_plan(str(empty))
        print(f"  {text}")
        assert "没有待学习" in text

        # 不存在的目录也不该崩
        plan2 = scheduler.plan(str(Path(tmp) / "nope"))
        assert plan2 == []

    print("空目录处理正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Learning Scheduler 模块测试")
    print("=" * 60 + "\n")

    test_priority_content_over_filename()
    test_priority_reasons_explainable()
    test_priority_novelty()

    test_queue_ordering_and_dedup()
    test_queue_reset()
    test_retry_isolation()
    test_queue_progress()

    test_build_schedule_skips_learned()
    test_plan_shape()
    test_run_executes_and_records()
    test_error_isolation()
    test_store_markdown_roundtrip()
    test_retry_across_runs()
    test_run_without_learner()
    test_render_plan_and_progress()
    test_empty_directory()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
