---
key: 平台全量/最强视频换脸+换头 Animate Wan2.2_2016787359760654338.json
name: 最强视频换脸+换头 Animate Wan2.2_2016787359760654338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强视频换脸+换头 Animate Wan2.2_2016787359760654338.json
hash: 05f15063178792a8
coverage: 0.573171
learned_at: 2026-11-14 02:15:07
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, BlockifyMask, GrowMask, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoSampler, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoDecode, GetNode, GIMMVFI_interpolate, GetNode, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, Int, DownloadAndLoadGIMMVFIModel, GetNode, DrawMaskOnImage, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, LayerUtility: PurgeVRAM, SetNode, JWInteger, SimpleMath+, WanVideoBlockSwap, ImageResizeKJv2, SetNode, JjkText, Note, SetNode, easy cleanGpuUsed, MaskToImage, VHS_VideoCombine, GetNode, SaveImage, LoadImage, SetNode, VHS_VideoCombine, DuckHideNode, GetNode, Audio Duration (mtb), SimpleMath+, ImageFromBatch+, JWInteger, VHS_LoadVideo, JWInteger, PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/最强视频换脸+换头 Animate Wan2.2_2016787359760654338.json

> 来源文件 `comfyui_library/workflows/平台全量/最强视频换脸+换头 Animate Wan2.2_2016787359760654338.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
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
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
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
- `SimpleMath+`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `SetNode`
- `JjkText`
- `Note`
- `SetNode`
- `easy cleanGpuUsed`
- `MaskToImage`
- `VHS_VideoCombine`
- `GetNode`
- `SaveImage`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `DuckHideNode`
- `GetNode`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `ImageFromBatch+`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `PrimitiveInt`

## 知识

覆盖率 **57%**（47/82）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoDecode`、`GIMMVFI_interpolate`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`Int`、`DownloadAndLoadGIMMVFIModel`、`DrawMaskOnImage`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`easy sam3VideoSegmentation`、`JWInteger`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`MaskToImage`、`VHS_VideoCombine`、`SaveImage`、`LoadImage`、`DuckHideNode`、`Audio Duration (mtb)`、`ImageFromBatch+`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
