---
key: 平台全量/视频换人V2+单人多人=AnimateWan2.2_2012912685184192513.json
name: 视频换人V2+单人多人=AnimateWan2.2_2012912685184192513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换人V2+单人多人=AnimateWan2.2_2012912685184192513.json
hash: 2fe20102177fa216
coverage: 0.567901
learned_at: 2026-11-14 02:38:17
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, Note, BlockifyMask, GrowMask, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, FaceMaskFromPoseKeypoints, WanVideoDecode, GetNode, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, ImageFromBatch+, Int, GetNode, DrawMaskOnImage, SetNode, SetNode, GetNode, SetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, LayerUtility: PurgeVRAM, SetNode, JWInteger, SimpleMath+, WanVideoBlockSwap, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, DownloadAndLoadGIMMVFIModel, ImageCropByMaskAndResize, VHS_VideoCombine, MaskToImage, VHS_VideoCombine, SetNode, easy cleanGpuUsed, JWInteger, JWInteger, JjkText, PrimitiveInt, VHS_LoadVideo, WanVideoSampler, WanVideoAnimateEmbeds, GIMMVFI_interpolate, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, DWPreprocessor, LoadImage]
patterns: []
missing: []
---

# 平台全量/视频换人V2+单人多人=AnimateWan2.2_2012912685184192513.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换人V2+单人多人=AnimateWan2.2_2012912685184192513.json`

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
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `Note`
- `BlockifyMask`
- `GrowMask`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `FaceMaskFromPoseKeypoints`
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
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `DownloadAndLoadGIMMVFIModel`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `MaskToImage`
- `VHS_VideoCombine`
- `SetNode`
- `easy cleanGpuUsed`
- `JWInteger`
- `JWInteger`
- `JjkText`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `GIMMVFI_interpolate`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `DWPreprocessor`
- `LoadImage`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`BlockifyMask`、`GrowMask`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`FaceMaskFromPoseKeypoints`、`WanVideoDecode`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageFromBatch+`、`Int`、`DrawMaskOnImage`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`easy sam3VideoSegmentation`、`JWInteger`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`DownloadAndLoadGIMMVFIModel`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`MaskToImage`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`GIMMVFI_interpolate`、`DWPreprocessor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
