---
name: unknown_workflow_video_sampler_clip_37
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.938167
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1953283354574712834.json, 视频生成/图生视频/1950706525243396097.json, 视频生成/图生视频/1950686610079830017.json, 视频生成/图生视频/1951804301834440706.json, 视频生成/图生视频/1991844034222288897.json, 视频生成/图生视频/2043858986851639297.json, 视频生成/图生视频/2043862678724157442.json, 视频生成/文生视频/1950654567312740354.json, 视频生成/文生视频/1954771341195960322.json, 视频生成/文生视频/1951460131294883841.json, 视频生成/文生视频/1952571860477259777.json, 视频生成/文生视频/1951496649069768705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1953283354574712834.json、视频生成/图生视频/1950706525243396097.json、视频生成/图生视频/1950686610079830017.json、视频生成/图生视频/1951804301834440706.json、视频生成/图生视频/1991844034222288897.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `ModelSamplingSD3` —— 11/12 个有
- `WanImageToVideo` —— 11/12 个有
- `EmptyHunyuanLatentVideo` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `LoraLoader` —— 4/12 个有
- `PrimitiveInt` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `Int` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `Primitive integer [Crystools]` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `easy textSwitch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 12 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 12 | 2% |
| 采样算法 | sa_solver | - | 12 | 92% |
| 调度器 | beta | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，12 个样本，取值分散，一致性仅 2%
- 采样算法 最常用 sa_solver，12 个样本，一致性 92%
- 调度器 最常用 beta，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（18/12 个样本）：Steps较低可能导致细节不足
