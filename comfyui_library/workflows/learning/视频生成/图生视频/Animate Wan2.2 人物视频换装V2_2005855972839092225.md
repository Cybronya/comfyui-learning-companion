---
key: 视频生成/图生视频/Animate Wan2.2 人物视频换装V2_2005855972839092225.json
name: Animate Wan2.2 人物视频换装V2_2005855972839092225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Animate Wan2.2 人物视频换装V2_2005855972839092225.json
hash: 3e2261c4e9a097f9
coverage: 0.5625
learned_at: 2026-10-15 22:33:59
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, BlockifyMask, GrowMask, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoDecode, GetNode, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, ImageFromBatch+, Int, DownloadAndLoadGIMMVFIModel, GetNode, DrawMaskOnImage, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, JWInteger, JWInteger, JWInteger, SimpleMath+, WanVideoBlockSwap, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, Note, VHS_VideoCombine, MaskToImage, easy sam3VideoSegmentation, JjkText, VHS_VideoCombine, WanVideoSampler, GIMMVFI_interpolate, SetNode, easy cleanGpuUsed, PrimitiveInt, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Animate Wan2.2 人物视频换装V2_2005855972839092225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005855972839092225.json`

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
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
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
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy sam3ModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `MaskToImage`
- `easy sam3VideoSegmentation`
- `JjkText`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GIMMVFI_interpolate`
- `SetNode`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **56%**（45/80）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoDecode`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageFromBatch+`、`Int`、`DownloadAndLoadGIMMVFIModel`、`DrawMaskOnImage`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`JWInteger`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`VHS_VideoCombine`、`MaskToImage`、`easy sam3VideoSegmentation`、`WanVideoSampler`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
