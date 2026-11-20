---
name: unknown_workflow_video_lora_sampler_596
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.895
common_nodes: [BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, CropByBBoxes, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSampler, LayerUtility: If , LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveBoolean, PrimitiveString, RTDETR_detect, SAM3_Detect, SDPoseDrawKeypoints, SDPoseKeypointExtractor, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移（卡通形象）_wan2.2_2063784977329909762.json, 视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json, 视频生成/图生视频/图生视频  动作迁移_2062727464236965889.json, 视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_596

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/动作迁移（卡通形象）_wan2.2_2063784977329909762.json、视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json、视频生成/图生视频/图生视频  动作迁移_2062727464236965889.json、视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CropByBBoxes`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: If `
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RTDETR_detect`
- `SAM3_Detect`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 3/4 个有
- `Int` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `CLIPLoader` —— 1/4 个有
- `FrameInterpolate` —— 1/4 个有
- `FrameInterpolationModelLoader` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
