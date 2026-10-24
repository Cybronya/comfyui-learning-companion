---
name: unknown_workflow_video_lora_sampler_898
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4075
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, ImageBatch, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, KSampler, LoadImage, LoadImageFromPath, LoraLoaderModelOnly, MaskPreview, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PixelPerfectResolution, PreviewImage, PrimitiveInt, SAMModelLoader (segment anything), SetNode, TorchCompileModel, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_LoadVideoPath, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/最新 Wan 2.2 Animate 无限循环 自动分割 超长视频_1971391086038040577.json, 视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_898

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最新 Wan 2.2 Animate 无限循环 自动分割 超长视频_1971391086038040577.json、视频生成/文生视频/最新 Wan 2.2 Animate + 无限循环 + 自动分割 + 原生支持 TikTok 舞蹈_1971252315321749505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageBatch`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoadImageFromPath`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PixelPerfectResolution`
- `PreviewImage`
- `PrimitiveInt`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `TorchCompileModel`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
