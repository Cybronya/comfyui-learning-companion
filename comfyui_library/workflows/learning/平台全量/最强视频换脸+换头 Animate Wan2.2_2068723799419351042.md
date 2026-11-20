---
key: 平台全量/最强视频换脸+换头 Animate Wan2.2_2068723799419351042.json
name: 最强视频换脸+换头 Animate Wan2.2_2068723799419351042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强视频换脸+换头 Animate Wan2.2_2068723799419351042.json
hash: 933322af298d0a82
coverage: 0.547619
learned_at: 2026-11-14 02:15:11
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, GrowMask, DrawMaskOnImage, BlockifyMask, GetNode, SetNode, SetNode, GetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, WanVideoBlockSwap, WanVideoVAELoader, LayerUtility: PurgeVRAM, SetNode, SetNode, VHS_VideoInfo, PixelPerfectResolution, GetNode, Reroute, DWPreprocessor, WanVideoLoraSelectMulti, ImageResizeKJv2, JWInteger, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, SetNode, SimpleMath+, SetNode, SetNode, ImageCropByMaskAndResize, CLIPVisionLoader, GetNode, ImageResizeKJv2, SetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, WanVideoDecode, GetImageSizeAndCount, GetNode, GetNode, SimpleMath+, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, SimpleMath+, SetNode, easy cleanGpuUsed, GetNode, Int, CM_IntToFloat, GetNode, Audio Duration (mtb), ImageFromBatch+, SetNode, SimpleMath+, easy showAnything, GetImageRangeFromBatch, GetNode, GetNode, GetNode, JWInteger, JjkText, JWInteger, VHS_VideoCombine, LoadImage, VHS_LoadVideo, PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/最强视频换脸+换头 Animate Wan2.2_2068723799419351042.json

> 来源文件 `comfyui_library/workflows/平台全量/最强视频换脸+换头 Animate Wan2.2_2068723799419351042.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（84 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `JWInteger`
- `JjkText`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `PrimitiveInt`

## 知识

覆盖率 **55%**（46/84）

**有卡**：`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`easy sam3VideoSegmentation`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`VHS_VideoInfo`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`SimpleMath+`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`Int`、`CM_IntToFloat`、`Audio Duration (mtb)`、`ImageFromBatch+`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
