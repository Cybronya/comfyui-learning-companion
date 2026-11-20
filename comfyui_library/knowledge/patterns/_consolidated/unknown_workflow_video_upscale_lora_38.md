---
name: unknown_workflow_video_upscale_lora_38
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.502
common_nodes: [AILab_Preview, BiRefNetRMBG, CLIPVisionLoader, Create Grid Image from Batch, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, EmptyImage, FloatConstant, GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageBatchMulti, ImageConcanate, ImageFromBatch, ImageResizeKJv2, ImageScaleBy, ImageScaleToMaxDimension, ImpactMakeAnyList, ImpactMinMax, ImpactSelectNthItemOfAnyList, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, PreviewAny, PreviewImage, PrimitiveStringMultiline, RepeatImageBatch, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, StringConstantMultiline, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageResizeToClosest, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSVIProEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy boolean, easy compare, easy ifElse, easy int, easy lengthAnything, easy mathInt, easy promptLine, easy seed, easy whileLoopEnd, easy whileLoopStart]
problems: []
missing: []
members: [视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json, 视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2033206135498481666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json、视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2033206135498481666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_Preview`
- `BiRefNetRMBG`
- `CLIPVisionLoader`
- `Create Grid Image from Batch`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `FloatConstant`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageBatchMulti`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToMaxDimension`
- `ImpactMakeAnyList`
- `ImpactMinMax`
- `ImpactSelectNthItemOfAnyList`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RepeatImageBatch`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `StringConcatenate`
- `StringConstantMultiline`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageResizeToClosest`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSVIProEmbeds`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy boolean`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy mathInt`
- `easy promptLine`
- `easy seed`
- `easy whileLoopEnd`
- `easy whileLoopStart`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
