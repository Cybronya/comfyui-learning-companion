---
name: unknown_workflow_video_lora_sampler_871
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5265
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfySwitchNode, DiffusionModelLoaderKJ, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RMBG, SAM3_VideoTrack, SCAIL2ColoredMask, SCAIL2ColoredMaskV2, SamplerCustom, SetNode, TextInput_, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanChunkFeedForward, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/SCAIL-2多图参考动作迁移v1_2067874432374366210.json, 视频生成/图生视频/SCAIL2-循环长视频v2_2065302324700073985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_871

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SCAIL-2多图参考动作迁移v1_2067874432374366210.json、视频生成/图生视频/SCAIL2-循环长视频v2_2065302324700073985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RMBG`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SCAIL2ColoredMaskV2`
- `SamplerCustom`
- `SetNode`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanChunkFeedForward`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SAM3_Detect` —— 1/2 个有
- `SAM3_TrackPreview` —— 1/2 个有
- `SAM3_TrackToMask` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_GetImageCount` —— 1/2 个有
- `WanContextWindowsManual` —— 1/2 个有
- `WanVideoMemoryEfficientSageAttentionPatch` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
