---
name: unknown_workflow_video_lora_sampler_600
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.606333
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, ComfyEverAnimate, ComfyEverAnimateTrimImages, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, INTConstant, ImageBatch, ImageConcatMulti, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelMemoryUsageFactorOverride, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, Sam2Segmentation, Seed (rgthree), SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanChunkFeedForward]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/EverAnimate for循环任意时长视频动作迁移_人体替换_2062571158205198337.json, 视频生成/图生视频/EverAnimate 无限动作迁移_2062845176858628097.json, 视频生成/图生视频/EverAnimate多参视频编辑Beta版_2062427659103199234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_600

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/EverAnimate for循环任意时长视频动作迁移_人体替换_2062571158205198337.json、视频生成/图生视频/EverAnimate 无限动作迁移_2062845176858628097.json、视频生成/图生视频/EverAnimate多参视频编辑Beta版_2062427659103199234.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyEverAnimate`
- `ComfyEverAnimateTrimImages`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageBatch`
- `ImageConcatMulti`
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
- `PreviewImage`
- `Sam2Segmentation`
- `Seed (rgthree)`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanChunkFeedForward`

**可变部分**（部分 workflow 才有）：
- `FancyTimerNode` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `TorchCompileModelWanVideo` —— 2/3 个有
- `VHS_GetImageCount` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有

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
| Steps较低可能导致细节不足 | 17/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（17/3 个样本）：Steps较低可能导致细节不足
