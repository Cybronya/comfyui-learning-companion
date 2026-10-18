---
key: 视频生成/图生视频/🈚️Wan Animate_mix模式-人物迁移_替换人物到场景-wan 2.2_1969102037159997442.json
name: 🈚️Wan Animate_mix模式-人物迁移_替换人物到场景-wan 2.2_1969102037159997442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🈚️Wan Animate_mix模式-人物迁移_替换人物到场景-wan 2.2_1969102037159997442.json
hash: 0d0426fb5894ddab
coverage: 0.55
learned_at: 2026-10-15 22:31:47
nodes: [SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, CLIPVisionLoader, GetNode, PrimitiveNode, GetNode, ImageResizeKJ, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, GetNode, SetNode, SetNode, WanVideoTextEncode, WanVideoClipVisionEncode, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoFreeInitArgs, GetNode, GetNode, WanVideoEnhanceAVideo, DWPreprocessor, easy imageRemBg, WanVideoSampler, GetNode, WanVideoDecode, SetNode, GetImageRangeFromBatch, GetNode, WanVideoSLG, GetNode, GetNode, GetNode, ImageConcanate, VHS_LoadVideo, Bjornulf_ShowInt, GetImageSizeAndCount, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, SetNode, MaskToImage, GetNode, LoadSAM3Model, ImageListToBatch+, MaskFromBatch+, ToBinaryMask, GrowMaskWithBlur, BlockifyMask, ImageListToBatch+, easy imageBatchToImageList, Reroute, GetNode, SetNode, SetNode, SAM3Segmentation, Reroute, SAM3PointCollector, VHS_VideoCombine, GetImageRangeFromBatch, ImageResizeKJv2, SeCModelLoader_Ultra-Fast, Florence2Run, ImageListToBatch+, SeCVideoSegmentation, Reroute, GetNode, DownloadAndLoadFlorence2Model, GetImageSizeAndCount, LayerUtility: CropByMask V2, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoVAELoader, SetNode, WanVideoTorchCompileSettings, GetNode, Florence2toCoordinates, Reroute, WanVideoAnimateEmbeds, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelect, GetNode, SetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️Wan Animate_mix模式-人物迁移_替换人物到场景-wan 2.2_1969102037159997442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969102037159997442.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（120 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoFreeInitArgs`
- `GetNode`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `DWPreprocessor`
- `easy imageRemBg`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `WanVideoSLG`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `VHS_LoadVideo`
- `Bjornulf_ShowInt`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `SetNode`
- `MaskToImage`
- `GetNode`
- `LoadSAM3Model`
- `ImageListToBatch+`
- `MaskFromBatch+`
- `ToBinaryMask`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `ImageListToBatch+`
- `easy imageBatchToImageList`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SAM3Segmentation`
- `Reroute`
- `SAM3PointCollector`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `SeCModelLoader_Ultra-Fast`
- `Florence2Run`
- `ImageListToBatch+`
- `SeCVideoSegmentation`
- `Reroute`
- `GetNode`
- `DownloadAndLoadFlorence2Model`
- `GetImageSizeAndCount`
- `LayerUtility: CropByMask V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `Florence2toCoordinates`
- `Reroute`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **55%**（66/120）

**有卡**：`CLIPVisionLoader`、`ImageResizeKJ`、`DrawMaskOnImage`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM V2`、`LoadWanVideoT5TextEncoder`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoFreeInitArgs`、`WanVideoEnhanceAVideo`、`DWPreprocessor`、`easy imageRemBg`、`WanVideoSampler`、`WanVideoDecode`、`GetImageRangeFromBatch`、`WanVideoSLG`、`ImageConcanate`、`VHS_LoadVideo`、`Bjornulf_ShowInt`、`GetImageSizeAndCount`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`MaskToImage`、`LoadSAM3Model`、`ImageListToBatch+`、`MaskFromBatch+`、`ToBinaryMask`、`GrowMaskWithBlur`、`BlockifyMask`、`easy imageBatchToImageList`、`SAM3Segmentation`、`SAM3PointCollector`、`VHS_VideoCombine`、`SeCModelLoader_Ultra-Fast`、`Florence2Run`、`SeCVideoSegmentation`、`DownloadAndLoadFlorence2Model`、`LayerUtility: CropByMask V2`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`Florence2toCoordinates`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LoadImage`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
