---
name: unknown_workflow_video_sampler_clip_211
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.461
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, KSampler, LoadImage, ModelSamplingSD3, SetNode, SimpleMath+, Text Multiline, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.2 rapid all-in-one，最简单使用，极速生成_1968175638647549954.json, 视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json, 视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_211

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 rapid all-in-one，最简单使用，极速生成_1968175638647549954.json、视频生成/文生视频/Wan2.2 rapid mega v6工作流，文生视频图生视频all-in-one_1976881257567207426.json、视频生成/文生视频/Wan2.2-AIO-生视频_1982663725121445889.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Evaluate Strings` —— 2/3 个有
- `easy convertAnything` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
