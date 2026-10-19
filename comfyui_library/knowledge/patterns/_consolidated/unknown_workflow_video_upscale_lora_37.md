---
name: unknown_workflow_video_upscale_lora_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.531
common_nodes: [AILab_ImagePreview, BatchImagesNode, BiRefNetRMBG, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, ImageScaleToMaxDimension, ImageStitch, LoadImage, ModelAttentionBackend, PreviewAny, PreviewImage, RepeatImageBatch, SAM3_TrackPreview, SAM3_VideoTrack, SCAIL2ColoredMask, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, StringConcatenate, UNETLoader_Any, UniBlockSwap, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanChunkFeedForward, easy boolean, easy cleanGpuUsed, easy ifElse, easy int, easy loraStack, easy loraStackApply]
problems: []
missing: []
members: [视频生成/图生视频/视频编辑-Scail2-不限时长-动作迁移-主体替换-官流V2_2082550150622437378.json, 视频生成/图生视频/视频编辑-Scail2-不限时长-动作迁移-主体替换_2065300375179186177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频编辑-Scail2-不限时长-动作迁移-主体替换-官流V2_2082550150622437378.json、视频生成/图生视频/视频编辑-Scail2-不限时长-动作迁移-主体替换_2065300375179186177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImagePreview`
- `BatchImagesNode`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `ImageStitch`
- `LoadImage`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewImage`
- `RepeatImageBatch`
- `SAM3_TrackPreview`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConcatenate`
- `UNETLoader_Any`
- `UniBlockSwap`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanChunkFeedForward`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy loraStack`
- `easy loraStackApply`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `Fast Muter (rgthree)` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `InsertImagesToBatchIndexed` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `WanAnimatePlus SCAIL_2 Flow Embeds` —— 1/2 个有
- `WanAnimatePlus SCAIL_2 Flow Sampler` —— 1/2 个有
- `WanAnimatePlus VAE Decode` —— 1/2 个有
- `WanSCAILToVideo` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
