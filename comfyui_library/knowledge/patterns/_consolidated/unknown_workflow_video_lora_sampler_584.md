---
name: unknown_workflow_video_lora_sampler_584
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9004
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, CropByBBoxes, ImageBatch, ImageFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveString, RTDETR_detect, SAM3_Detect, SDPoseDrawKeypoints, SDPoseKeypointExtractor, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json, 视频生成/图生视频/动作迁移（卡通形象）_wan2.2_2063784977329909762.json, 视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json, 视频生成/图生视频/图生视频  动作迁移_2062727464236965889.json, 视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_584

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/动作迁移（真人）_wan2.2_2062356303741276161.json、视频生成/图生视频/动作迁移（卡通形象）_wan2.2_2063784977329909762.json、视频生成/图生视频/动作迁移（插帧流畅版）_wan2.2_2065044173270634498.json、视频生成/图生视频/图生视频  动作迁移_2062727464236965889.json、视频生成/文生视频/动作迁移（卡通形象）_wan2.2_2061988171709239297.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CropByBBoxes`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
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
- `BodyRatioMapperProportionTransfer` —— 4/5 个有
- `BodyRatioMapperSDPoseRender` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerUtility: If ` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `CLIPLoaderGGUF` —— 3/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `BlockifyMask` —— 1/5 个有
- `DrawMaskOnImage` —— 1/5 个有
- `FrameInterpolate` —— 1/5 个有
- `FrameInterpolationModelLoader` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/5 个有
- `PixelPerfectResolution` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
