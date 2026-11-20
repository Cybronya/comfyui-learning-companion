---
key: 平台全量/最强视频换脸+换头+Animate+Wan2.2_2015627520716050434.json
name: 最强视频换脸+换头+Animate+Wan2.2_2015627520716050434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强视频换脸+换头+Animate+Wan2.2_2015627520716050434.json
hash: cededb5a2a609c44
coverage: 0.56962
learned_at: 2026-11-14 02:15:16
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, BlockifyMask, GrowMask, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoSampler, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoDecode, GetNode, GIMMVFI_interpolate, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, ImageFromBatch+, Int, DownloadAndLoadGIMMVFIModel, GetNode, DrawMaskOnImage, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, LayerUtility: PurgeVRAM, SetNode, JWInteger, JWInteger, JWInteger, SimpleMath+, PrimitiveInt, VHS_LoadVideo, WanVideoBlockSwap, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, JjkText, SetNode, easy cleanGpuUsed, MaskToImage, VHS_VideoCombine, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 平台全量/最强视频换脸+换头+Animate+Wan2.2_2015627520716050434.json

> 来源文件 `comfyui_library/workflows/平台全量/最强视频换脸+换头+Animate+Wan2.2_2015627520716050434.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（79 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `GrowMask`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `WanVideoDecode`
- `GetNode`
- `GIMMVFI_interpolate`
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
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy sam3ModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `easy sam3VideoSegmentation`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `JjkText`
- `SetNode`
- `easy cleanGpuUsed`
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **57%**（45/79）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoDecode`、`GIMMVFI_interpolate`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageFromBatch+`、`Int`、`DownloadAndLoadGIMMVFIModel`、`DrawMaskOnImage`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`easy sam3VideoSegmentation`、`JWInteger`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`MaskToImage`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
