---
name: unknown_workflow_video_sampler_clip_77
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.831714
common_nodes: [CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1950716655997489154.json, 视频生成/图生视频/1986735841529819137.json, 视频生成/图生视频/1986737706749390849.json, 视频生成/图生视频/2009175166516989953.json, 视频生成/图生视频/1956058743224061953.json, 视频生成/图生视频/1951969446145544194.json, 视频生成/图生视频/1951895309616099329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1950716655997489154.json、视频生成/图生视频/1986735841529819137.json、视频生成/图生视频/1986737706749390849.json、视频生成/图生视频/2009175166516989953.json、视频生成/图生视频/1956058743224061953.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `MathExpression|pysssss` —— 5/7 个有
- `CLIPVisionEncode` —— 4/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `CheckpointLoaderSimple` —— 4/7 个有
- `Primitive integer [Crystools]` —— 4/7 个有
- `CLIPLoader` —— 3/7 个有
- `UNETLoader` —— 3/7 个有
- `VAELoader` —— 3/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `Video_Upscale_With_Model` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | sa_solver | - | 7 | 86% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
