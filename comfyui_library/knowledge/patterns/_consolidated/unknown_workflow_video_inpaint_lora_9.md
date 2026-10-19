---
name: unknown_workflow_video_inpaint_lora_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6065
common_nodes: [Any Switch (rgthree), ClothesSegment, FaceSegment, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetImageSize+, GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, ImageFromBatch, ImageResize+, ImageResizeKJ, InvertMask, Label (rgthree), LoadImage, LoadWanVideoT5TextEncoder, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PreviewImage, PrimitiveStringMultiline, RMBG, ResizeMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1981001980585840642.json, 视频生成/图生视频/2007176668045123586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1981001980585840642.json、视频生成/图生视频/2007176668045123586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ClothesSegment`
- `FaceSegment`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `ImageFromBatch`
- `ImageResize+`
- `ImageResizeKJ`
- `InvertMask`
- `Label (rgthree)`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RMBG`
- `ResizeMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `BBoxesToSAM2` —— 1/2 个有
- `Bookmark (rgthree)` —— 1/2 个有
- `DownloadAndLoadQwenModel` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: DrawBBoxMaskV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerMask: ObjectDetectorMask` —— 1/2 个有
- `LayerMask: SAM2VideoUltra` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `QwenVLDetection` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
