# Workflow 学习记录

本目录是「哪些 workflow 学过了、学到了什么」的**唯一存放位置**，
由 `engine/workflow_learning/` 读写。路径常量集中在
`engine/workflow_learning/paths.py`。

## 存储格式：一个 workflow 一个 Markdown 文件

```
learning/
├── index.md                      汇总索引（表格，一行一个 workflow，带链接）
└── sd1.5/
    ├── basic.md                  该 workflow 的完整学习记录
    ├── lora.md
    └── text-to-image-workflow.md
```

目录结构与源文件镜像 —— 扫一眼就知道哪些 family 学过。

单个记录长这样：

```markdown
---
key: sd1.5/basic.json
name: basic
type: Text To Image
status: completed
hash: a95cceecfb5d5225
coverage: 1
learned_at: 2026-10-06 01:23:19
nodes: [CheckpointLoaderSimple, CLIPTextEncode, KSampler, ...]
patterns: [text_to_image]
missing: []
---

# sd1.5/basic.json

## 结构
**生成流程**：Model → Condition → Latent → Sampling → Decode → Output
...
```

`---` 之间是 frontmatter（机器查），下面是正文（人读）。

## 为什么用 Markdown 而不是 JSON

1. **Agent 直接可查**。JSON 要先解析才知道里面有什么；
   Markdown 打开就是人话，还能直接 grep：

   ```bash
   grep -rl "LoraLoader" comfyui_library/workflows/learning/
   # → sd1.5/lora.md   一眼看出哪些 workflow 用了这个节点

   grep -rl "体检发现的问题" comfyui_library/workflows/learning/
   # → 参数有问题的 workflow
   ```

2. **git diff 可读**。JSON 每次重写都是整块变更，Markdown 只变改动的行。

3. **与知识卡规范一致**。`comfyui_library/knowledge/**/*.md` 已经在用
   frontmatter（`name/title/category/tags/updated`），学习记录沿用同一套，
   不引入第二种格式。

原先的 `registry.json` + `experience.json` + `reports/*.md` **三份已合并**：
它们描述的是同一件事却分散在不同格式，「已学过了吗」和「学到了什么」可能不一致。
现在「文件存在」即「已学过」，没有第二种可能。

## 扫描器为什么跳过本目录

`WorkflowScanner` 递归扫描时会**主动跳过本目录**（登记在
`paths.SKIPPED_DIR_NAMES` 里）。否则 `index.md` 和各条记录
会被当成 workflow 拿去"学习"，然后把自己写进记录，形成无限循环。

跳过判定用的是**集合精确匹配**，不是下划线前缀 ——
所以本目录名不必带 `_` 前缀。

## 怎么用

```python
from engine.workflow_learning import create_batch_learner

batch = create_batch_learner(
    analyzer=..., retriever=..., parser=...,
    diagnostics=..., explorer=..., gap_detector=...,
)
batch.learn_folder()      # 不传路径 = 学 comfyui_library/workflows/
```

幂等：重复执行，未变更的文件会跳过。

```python
batch.learn_folder(force=True)     # 强制全部重学
batch.registry.remove("sd1.5/basic.json")   # 忘记学过 → 删记录
batch.pending()                    # 哪些还没学 / 需重学
batch.store.node_frequency()       # 节点频次（供 knowledge_evolution 挖模式）
```

## 关键行为

- **自动重学**：记录里存内容指纹（sha256 前 16 位），
  改了 workflow 参数后指纹变化，下次运行自动重学
- **清理失效记录**：文件被删除后 `prune_missing` 会清掉对应记录与空目录
- **失败的记录不算已学**：`status: failed` 的条目下次会被重试
- **路径全相对**：记录里存 `comfyui_library/workflows/sd1.5/basic.json`，
  换机器 / 改盘符不会失效

## 维护提醒

- 本目录内容**要提交进 git**（`.gitignore` 已放行 `comfyui_library/`），
  它是跨会话的项目记忆，不是缓存
- 手改记录时注意 `hash` 字段：留空则跳过指纹比对，只按「文件是否存在」判断
- 正文里的结论来自 analyzer / diagnostics 的确定性计算，
  不含 LLM 生成内容，可放心调整格式
- `index.md` 是自动生成的汇总表，改了会被下次运行覆盖
