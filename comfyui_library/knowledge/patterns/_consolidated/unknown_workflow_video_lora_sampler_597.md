---
name: unknown_workflow_video_lora_sampler_597
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.813
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyEverAnimate, ComfyEverAnimateTrimImages, ComfyMathExpression, DrawViTPose, GetImageSizeAndCount, INTConstant, ImageBatch, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelMemoryUsageFactorOverride, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WD14Tagger|pysssss, WanChunkFeedForward, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2072998868763320320.json, 视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json, 视频生成/文生视频/EverAnimate 长视频一致性生成_2063934460369915905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_597

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2072998868763320320.json、视频生成/文生视频/EverAnimate Long Video Consistent Editing_2072998873179922432.json、视频生成/文生视频/EverAnimate 长视频一致性生成_2063934460369915905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyEverAnimate`
- `ComfyEverAnimateTrimImages`
- `ComfyMathExpression`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelMemoryUsageFactorOverride`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WD14Tagger|pysssss`
- `WanChunkFeedForward`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `SDPoseDrawKeypoints` —— 2/3 个有
- `SDPoseKeypointExtractor` —— 2/3 个有
- `YOLOModelLoader` —— 2/3 个有
- `BlockifyMask` —— 1/3 个有
- `BodyRatioMapperProportionTransfer` —— 1/3 个有
- `BodyRatioMapperSDPoseRender` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `LayerMask: SAM2VideoUltra` —— 1/3 个有
- `easy imageIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
