---
key: 数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json
name: 已知最强视频换脸模型 Animate Wan2.2_2007046777135964161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json
hash: c4f6c336f9c38a31
coverage: 0.5625
learned_at: 2026-10-26 02:02:00
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, BlockifyMask, GrowMask, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoSampler, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoDecode, GetNode, GIMMVFI_interpolate, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, ImageFromBatch+, Int, DownloadAndLoadGIMMVFIModel, GetNode, DrawMaskOnImage, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, LayerUtility: PurgeVRAM, SetNode, JWInteger, JWInteger, SimpleMath+, WanVideoBlockSwap, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, JjkText, LoadImage, SetNode, easy cleanGpuUsed, MaskToImage, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, SetNode, SetNode, SetNode, JWInteger, PrimitiveInt, Note]
patterns: []
missing: []
---

# 数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
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
- `SimpleMath+`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `JjkText`
- `LoadImage`
- `SetNode`
- `easy cleanGpuUsed`
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `PrimitiveInt`
- `Note`

## 知识

覆盖率 **56%**（45/80）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoDecode`、`GIMMVFI_interpolate`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageFromBatch+`、`Int`、`DownloadAndLoadGIMMVFIModel`、`DrawMaskOnImage`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`easy sam3VideoSegmentation`、`JWInteger`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`LoadImage`、`easy cleanGpuUsed`、`MaskToImage`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
