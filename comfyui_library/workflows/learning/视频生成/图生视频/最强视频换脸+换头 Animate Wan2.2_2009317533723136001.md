---
key: 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2009317533723136001.json
name: 最强视频换脸+换头 Animate Wan2.2_2009317533723136001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2009317533723136001.json
hash: 2d98bbcf1fad62a3
coverage: 0.551724
learned_at: 2026-10-15 22:34:12
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, GrowMask, DrawMaskOnImage, BlockifyMask, GetNode, SetNode, SetNode, GetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, WanVideoBlockSwap, WanVideoVAELoader, LayerUtility: PurgeVRAM, SetNode, SetNode, VHS_VideoInfo, PixelPerfectResolution, GetNode, Reroute, DWPreprocessor, WanVideoLoraSelectMulti, ImageResizeKJv2, JWInteger, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, SetNode, SimpleMath+, SetNode, SetNode, ImageCropByMaskAndResize, CLIPVisionLoader, GetNode, ImageResizeKJv2, SetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, WanVideoDecode, GetImageSizeAndCount, GetNode, GetNode, SimpleMath+, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, SimpleMath+, SetNode, easy cleanGpuUsed, GetNode, Int, CM_IntToFloat, GetNode, Audio Duration (mtb), ImageFromBatch+, SetNode, SimpleMath+, easy showAnything, GetImageRangeFromBatch, GetNode, PrimitiveInt, JWInteger, JWInteger, MarkdownNote, GetNode, GetNode, LoadImage, VHS_LoadVideo, SaveImage, TT_img_enc, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2009317533723136001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009317533723136001.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（87 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GrowMask`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy sam3ModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `easy sam3VideoSegmentation`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `GetNode`
- `Reroute`
- `DWPreprocessor`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `SimpleMath+`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Int`
- `CM_IntToFloat`
- `GetNode`
- `Audio Duration (mtb)`
- `ImageFromBatch+`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `GetImageRangeFromBatch`
- `GetNode`
- `PrimitiveInt`
- `JWInteger`
- `JWInteger`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `SaveImage`
- `TT_img_enc`
- `JjkText`

## 知识

覆盖率 **55%**（48/87）

**有卡**：`LoadImage`、`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`easy sam3VideoSegmentation`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`VHS_VideoInfo`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`SimpleMath+`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`Int`、`CM_IntToFloat`、`Audio Duration (mtb)`、`ImageFromBatch+`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`SaveImage`、`TT_img_enc`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
