---
name: unknown_workflow_video_inpaint_upscale
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.904
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Float to Int, FloatConstant, Florence2Run, Florence2toCoordinates, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, ImageStitch, ImpactMinMax, InpaintPreprocessor, LoadImage, PrimitiveString, Sam2Segmentation, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json, 平台全量/Wan2.2视频换背景&换人_2027288927790436353.json, 平台全量/快速视频换背景_2064946714049601537.json, 平台全量/快速视频换背景_2066715901898084353.json, 平台全量/视频换背景&换人+视频SeedVR2高清放大_2051844889272434689.json, 平台全量/视频换背景&换人+视频高清放大 人物一致 真实自然换装_2049354105822388226.json, 平台全量/视频换背景&换人+视频高清放大 人物一致_2068975133984903169.json, 平台全量/视频换背景&换人+视频高清放大_2048561318122229762.json, 平台全量/视频换背景&换人_2026213018018779138.json, 平台全量/视频换背景&换人_2043608685833887746.json, 视频生成/图生视频/视频换背景&换人动作迁移_2045437537212174338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json、平台全量/Wan2.2视频换背景&换人_2027288927790436353.json、平台全量/快速视频换背景_2064946714049601537.json、平台全量/快速视频换背景_2066715901898084353.json、平台全量/视频换背景&换人+视频SeedVR2高清放大_2051844889272434689.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
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
- `InpaintCrop` —— 1/11 个有
- `Mask Invert` —— 1/11 个有
- `MaskBlur+` —— 1/11 个有
- `MaskToImage` —— 1/11 个有
- `SAM3PointCollector` —— 1/11 个有
- `SAM3Propagate` —— 1/11 个有
- `SAM3VideoModelLoader` —— 1/11 个有
- `SAM3VideoOutput` —— 1/11 个有
- `SAM3VideoSegmentation` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
