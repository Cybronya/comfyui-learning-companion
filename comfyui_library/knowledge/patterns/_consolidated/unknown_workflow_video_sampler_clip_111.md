---
name: unknown_workflow_video_sampler_clip_111
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8614
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2010908567217381378.json, 视频生成/图生视频/1950706525243396097.json, 视频生成/图生视频/1951969446145544194.json, 视频生成/图生视频/1951895309616099329.json, 视频生成/文生视频/1951970286314926081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2010908567217381378.json、视频生成/图生视频/1950706525243396097.json、视频生成/图生视频/1951969446145544194.json、视频生成/图生视频/1951895309616099329.json、视频生成/文生视频/1951970286314926081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 4/5 个有
- `EmptyHunyuanLatentVideo` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `WanImageToVideo` —— 3/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `WanVideoTeaCacheKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 5 | 0% |
| 采样算法 | sa_solver | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 sa_solver，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
