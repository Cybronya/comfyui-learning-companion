---
name: unknown_workflow_video_sampler_clip_130
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.40825
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, KSampler, LoadImage, ModelSamplingSD3, SetNode, SimpleMath+, Text Multiline, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy int]
problems: [Steps较低可能导致细节不足]
missing: [Evaluate Strings, SimpleMath+, Text Multiline, easy convertAnything, easy int]
members: [视频生成/图生视频/1976881257567207426.json, 视频生成/文生视频/1976881257567207426.json, 视频生成/文生视频/1968175638647549954.json, 视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1976881257567207426.json、视频生成/文生视频/1976881257567207426.json、视频生成/文生视频/1968175638647549954.json、视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Evaluate Strings` —— 3/4 个有
- `easy convertAnything` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Evaluate Strings、SimpleMath+、Text Multiline、easy convertAnything、easy int
