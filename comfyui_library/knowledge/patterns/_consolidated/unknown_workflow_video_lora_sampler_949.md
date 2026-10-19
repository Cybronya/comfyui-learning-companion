---
name: unknown_workflow_video_lora_sampler_949
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5125
common_nodes: [AutoCropFaces, BiRefNetRMBG, Display Int (rgthree), FloatConstant, GetNode, INTConstant, ImageListToImageBatch, ImageScaleToMaxDimension, ImpactMakeImageList, LoadImage, LoadLynxResampler, LoadWanVideoT5TextEncoder, LynxEncodeFaceIP, MaskToImage, PreviewAny, PreviewImage, SetNode, SomethingToString, StringConstantMultiline, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoImageResizeToClosest, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy lengthAnything, easy mathInt, easy promptLine, easy seed]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json, 视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_949

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json、视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `AutoCropFaces`
- `BiRefNetRMBG`
- `Display Int (rgthree)`
- `FloatConstant`
- `GetNode`
- `INTConstant`
- `ImageListToImageBatch`
- `ImageScaleToMaxDimension`
- `ImpactMakeImageList`
- `LoadImage`
- `LoadLynxResampler`
- `LoadWanVideoT5TextEncoder`
- `LynxEncodeFaceIP`
- `MaskToImage`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `SomethingToString`
- `StringConstantMultiline`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoImageResizeToClosest`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy lengthAnything`
- `easy mathInt`
- `easy promptLine`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImageCrop` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImpactMakeAnyList` —— 1/2 个有
- `ImpactSelectNthItemOfAnyList` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `easy imageCount` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
