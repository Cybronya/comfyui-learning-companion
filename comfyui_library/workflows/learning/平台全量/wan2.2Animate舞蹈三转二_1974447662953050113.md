---
key: 平台全量/wan2.2Animate舞蹈三转二_1974447662953050113.json
name: wan2.2Animate舞蹈三转二_1974447662953050113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2Animate舞蹈三转二_1974447662953050113.json
hash: cafdc4e13b12786a
coverage: 0.941176
learned_at: 2026-11-14 01:19:35
nodes: [CLIPVisionLoader, ImageResizeKJv2, WanVideoVAELoader, WanVideoDecode, ImageCropByMaskAndResize, WanVideoLoraSelectMulti, Note, WanVideoClipVisionEncode, FaceMaskFromPoseKeypoints, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, easy cleanGpuUsed, ImageConcatMulti, ImageConcatMulti, SimpleMath+, SimpleMath+, WanVideoSampler, WanVideoTextEncodeCached, VHS_VideoCombine, LoadImage, VHS_VideoCombine, JWInteger, JWInteger, VHS_LoadVideo, VHS_VideoInfo, PixelPerfectResolution, DWPreprocessor, WanVideoAnimateEmbeds, WanVideoModelLoader, Note, ImpactInt, ImpactInt]
patterns: []
missing: []
---

# 平台全量/wan2.2Animate舞蹈三转二_1974447662953050113.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2Animate舞蹈三转二_1974447662953050113.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `ImageCropByMaskAndResize`
- `WanVideoLoraSelectMulti`
- `Note`
- `WanVideoClipVisionEncode`
- `FaceMaskFromPoseKeypoints`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `Note`
- `ImpactInt`
- `ImpactInt`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageCropByMaskAndResize`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`FaceMaskFromPoseKeypoints`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`ImageConcatMulti`、`SimpleMath+`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`LoadImage`、`JWInteger`、`VHS_LoadVideo`、`VHS_VideoInfo`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`ImpactInt`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
