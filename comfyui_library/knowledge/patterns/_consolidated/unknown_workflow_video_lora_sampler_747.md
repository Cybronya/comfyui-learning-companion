---
name: unknown_workflow_video_lora_sampler_747
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.541
common_nodes: [AILab_Preview, BiRefNetRMBG, CLIPLoader, CLIPVisionLoader, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, FloatConstant, GIMMVFI_interpolate, GetNode, INTConstant, ImageBatchMulti, ImageCrop, ImageResizeKJv2, ImpactMakeAnyList, ImpactMakeImageList, ImpactSelectNthItemOfAnyList, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, MaskBatchMulti, PreviewAny, PreviewImage, SetNode, SolidMask, SomethingToString, StringConstantMultiline, TextImageEncodeQwenVL, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy forLoopEnd, easy forLoopStart, easy lengthAnything, easy promptLine, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1990305288395911170.json, 视频生成/图生视频/1990127244414734338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_747

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1990305288395911170.json、视频生成/图生视频/1990127244414734338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_Preview`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `FloatConstant`
- `GIMMVFI_interpolate`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageCrop`
- `ImageResizeKJv2`
- `ImpactMakeAnyList`
- `ImpactMakeImageList`
- `ImpactSelectNthItemOfAnyList`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskBatchMulti`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `SolidMask`
- `SomethingToString`
- `StringConstantMultiline`
- `TextImageEncodeQwenVL`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy lengthAnything`
- `easy promptLine`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `ResizeAndPadImage` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有
- `easy mathInt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
