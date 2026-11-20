---
name: unknown_workflow_video_lora_sampler_662
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.643
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, ComfyEverAnimate, ComfyEverAnimateTrimImages, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, INTConstant, ImageBatch, ImageConcatMulti, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelMemoryUsageFactorOverride, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, Sam2Segmentation, Seed (rgthree), SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanChunkFeedForward]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/EverAnimate长视频人体动画动作迁移_2062510369326850050.json, 视频生成/图生视频/EverAnimate for循环任意时长视频动作迁移_人体替换_2062571158205198337.json, 视频生成/图生视频/EverAnimate 无限动作迁移_2062845176858628097.json, 视频生成/图生视频/EverAnimate多参视频编辑Beta版_2062427659103199234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_662

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/EverAnimate长视频人体动画动作迁移_2062510369326850050.json、视频生成/图生视频/EverAnimate for循环任意时长视频动作迁移_人体替换_2062571158205198337.json、视频生成/图生视频/EverAnimate 无限动作迁移_2062845176858628097.json、视频生成/图生视频/EverAnimate多参视频编辑Beta版_2062427659103199234.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
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
- `FancyTimerNode` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `TorchCompileModelWanVideo` —— 3/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `VHS_GetImageCount` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | lcm | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（30/4 个样本）：Steps较低可能导致细节不足
