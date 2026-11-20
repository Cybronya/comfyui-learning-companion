---
key: 平台全量/wan2.2 (1)_2112493419854651394.json
name: wan2.2 (1)_2112493419854651394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 (1)_2112493419854651394.json
hash: 94828a12e987c2f7
coverage: 0.580247
learned_at: 2026-11-14 01:19:15
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoDecode, GetNode, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, ImageFromBatch+, Int, DownloadAndLoadGIMMVFIModel, GetNode, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, LayerUtility: PurgeVRAM, SetNode, WanVideoBlockSwap, SetNode, GetNode, GetNode, SetNode, GIMMVFI_interpolate, SetNode, easy cleanGpuUsed, JjkText, ImageResizeKJv2, JWInteger, JWInteger, PrimitiveInt, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, ImageCropByMaskAndResize, JWInteger, MaskComposite, CLIPVisionLoader, BlockifyMask, GrowMask, LayerUtility: PurgeVRAM, WanVideoModelLoader, DrawMaskOnImage, easy sam3VideoSegmentation, SimpleMath+, GrowMask, JWInteger, VHS_VideoInfo, DWPreprocessor, FaceMaskFromPoseKeypoints, JWFloat, WanVideoLoraSelectMulti, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 平台全量/wan2.2 (1)_2112493419854651394.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 (1)_2112493419854651394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（81 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `SetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `Audio Duration (mtb)`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `ImageFromBatch+`
- `Int`
- `DownloadAndLoadGIMMVFIModel`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy sam3ModelLoader`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GIMMVFI_interpolate`
- `SetNode`
- `easy cleanGpuUsed`
- `JjkText`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `PrimitiveInt`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `ImageCropByMaskAndResize`
- `JWInteger`
- `MaskComposite`
- `CLIPVisionLoader`
- `BlockifyMask`
- `GrowMask`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `DrawMaskOnImage`
- `easy sam3VideoSegmentation`
- `SimpleMath+`
- `GrowMask`
- `JWInteger`
- `VHS_VideoInfo`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `JWFloat`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **58%**（47/81）

**有卡**：`PixelPerfectResolution`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoDecode`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageFromBatch+`、`Int`、`DownloadAndLoadGIMMVFIModel`、`easy sam3ModelLoader`、`WanVideoBlockSwap`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`JWInteger`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`MaskComposite`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoModelLoader`、`DrawMaskOnImage`、`easy sam3VideoSegmentation`、`VHS_VideoInfo`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`JWFloat`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
