---
name: unknown_workflow_video_lora_sampler_811
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.66
common_nodes: [CLIPLoader, CLIPTextEncode, DifferentialDiffusion, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, GrowMaskWithBlur, ImageAndMaskPreview, ImageBlur, ImageCompositeMasked, ImageCrop, ImageResizeKJ, ImageScaleBy, InstructPixToPixConditioning, KSampler, LatentSyncNode, LoadAudio, LoraLoaderModelOnly, MaskBoundingBox+, MaskPreview+, MaskToSEGS, ModelSamplingSD3, SAMLoader, SegsToCombinedMask, SetNode, SkipLayerGuidanceWanVideo, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VideoLengthAdjuster, WanVideoTeaCacheKJ]
problems: []
missing: []
members: [数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json, 音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_811

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json、音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageResizeKJ`
- `ImageScaleBy`
- `InstructPixToPixConditioning`
- `KSampler`
- `LatentSyncNode`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MaskBoundingBox+`
- `MaskPreview+`
- `MaskToSEGS`
- `ModelSamplingSD3`
- `SAMLoader`
- `SegsToCombinedMask`
- `SetNode`
- `SkipLayerGuidanceWanVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoLengthAdjuster`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `Audio Cut (mtb)` —— 1/2 个有
- `DF_Int_to_Float` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 89% |
| 采样算法 | gradient_estimation | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 最常用 gradient_estimation，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
