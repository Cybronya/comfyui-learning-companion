---
name: unknown_workflow_video_sampler_clip_184
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.768667
common_nodes: [AILab_MiniCPM_4_V_Advanced, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetImageRangeFromBatch, KSampler, MathExpression|pysssss, ModelSamplingSD3, Primitive integer [Crystools], PrimitiveInt, PrimitiveStringMultiline, Text Concatenate, VAEDecode, VHS_VideoCombine, WanImageToVideo, easy clearCacheAll, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json, 图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json, 平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/MiniCPM-V4.5视频洗稿_1961760421487251457.json、图片生成/反推提示词/Minicpm-V4.5视频反推_1966056353485721601.json、平台全量/MiniCPM-V4.5视频洗稿_1973417503571447810.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_MiniCPM_4_V_Advanced`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `KSampler`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `Primitive integer [Crystools]`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Get Image Size` —— 2/3 个有
- `GetVideoComponents` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
