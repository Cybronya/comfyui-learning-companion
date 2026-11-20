---
name: unknown_workflow_video_inpaint_upscale_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Float to Int, FloatConstant, Florence2Run, Florence2toCoordinates, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, ImageStitch, ImpactMinMax, InpaintPreprocessor, LoadImage, PrimitiveString, Sam2Segmentation, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json, 视频生成/图生视频/视频换背景&换人动作迁移_2045437537212174338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json、视频生成/图生视频/视频换背景&换人动作迁移_2045437537212174338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Fast Groups Bypasser (rgthree)`
- `Float to Int`
- `FloatConstant`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageStitch`
- `ImpactMinMax`
- `InpaintPreprocessor`
- `LoadImage`
- `PrimitiveString`
- `Sam2Segmentation`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 1/2 个有
- `Mask Invert` —— 1/2 个有
- `MaskBlur+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SAM3PointCollector` —— 1/2 个有
- `SAM3Propagate` —— 1/2 个有
- `SAM3VideoModelLoader` —— 1/2 个有
- `SAM3VideoOutput` —— 1/2 个有
- `SAM3VideoSegmentation` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
