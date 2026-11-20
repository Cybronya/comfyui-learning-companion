---
key: 平台全量/视频换装换头加服装互动 Animate Wan2.2_2039621617348780033.json
name: 视频换装换头加服装互动 Animate Wan2.2_2039621617348780033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频换装换头加服装互动 Animate Wan2.2_2039621617348780033.json
hash: 779b4e354fafeba9
coverage: 0.585714
learned_at: 2026-11-14 02:39:14
nodes: [GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, SetNode, LayerUtility: PurgeVRAM, SetNode, CLIPVisionLoader, Reroute, GetNode, SetNode, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, FaceMaskFromPoseKeypoints, DWPreprocessor, GetNode, Audio Duration (mtb), GetNode, GetImageSizeAndCount, SimpleMath+, ImageFromBatch+, Int, WanVideoModelLoader, LayerUtility: PurgeVRAM, SetNode, JWInteger, JWInteger, SimpleMath+, WanVideoBlockSwap, SetNode, Note, WanVideoSampler, GIMMVFI_interpolate, GetImageRangeFromBatch, WanVideoSetBlockSwap, GetNode, VHS_LoadVideo, SetNode, easy imageConcat, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, GetNode, WanVideoClipVisionEncode, JWInteger, SetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, WanVideoDecode, LoadImage, LoadImage, GetNode, DownloadAndLoadGIMMVFIModel, GetNode, SimpleMath+, PrimitiveInt, easy cleanGpuUsed, VHS_VideoCombine, RHHiddenNodes, JjkText]
patterns: []
missing: []
---

# 平台全量/视频换装换头加服装互动 Animate Wan2.2_2039621617348780033.json

> 来源文件 `comfyui_library/workflows/平台全量/视频换装换头加服装互动 Animate Wan2.2_2039621617348780033.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（70 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `GetNode`
- `Audio Duration (mtb)`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `ImageFromBatch+`
- `Int`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `SetNode`
- `Note`
- `WanVideoSampler` ★核心
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `WanVideoSetBlockSwap`
- `GetNode`
- `VHS_LoadVideo`
- `SetNode`
- `easy imageConcat`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoDecode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `GetNode`
- `SimpleMath+`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `JjkText`

## 知识

覆盖率 **59%**（41/70）

**有卡**：`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`LayerUtility: PurgeVRAM`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`SimpleMath+`、`ImageFromBatch+`、`Int`、`WanVideoModelLoader`、`JWInteger`、`WanVideoBlockSwap`、`WanVideoSampler`、`GIMMVFI_interpolate`、`GetImageRangeFromBatch`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`、`easy imageConcat`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoDecode`、`LoadImage`、`DownloadAndLoadGIMMVFIModel`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
