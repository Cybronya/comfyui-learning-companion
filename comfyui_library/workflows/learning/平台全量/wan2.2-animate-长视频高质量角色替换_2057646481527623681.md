---
key: 平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json
name: wan2.2-animate-长视频高质量角色替换_2057646481527623681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json
hash: 2c5b9297311bb2aa
coverage: 0.909091
learned_at: 2026-11-14 01:19:31
nodes: [MemoryCleaner, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, PreviewImage, ImageResizeKJv2, easy sam3ModelLoader, MaskToImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy sam3GetObjectIds, PreviewAny, easy sam3Visualization, GrowMaskWithBlur, PreviewAny, WanVideoVAELoader, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, OnnxDetectionModelLoader, MemoryCleaner, easy cleanGpuUsed, BlockifyMask, DrawMaskOnImage, WanVideoSetBlockSwap, MemoryCleaner, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoAnimateEmbeds, GetNode, WanVideoTeaCache, MemoryCleaner, WanVideoSampler, CLIPVisionLoader, GetImageSizeAndCount, VHS_VideoInfo, WanVideoDecode, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, VHS_LoadVideo, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, PoseAndFaceDetection, LoadImage, LoadImage, VHS_VideoCombine, VHS_LoadVideo, GoogleTranslator, String]
patterns: []
missing: []
---

# 平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-animate-长视频高质量角色替换_2057646481527623681.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
- `MemoryCleaner`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `PreviewImage`
- `ImageResizeKJv2`
- `easy sam3ModelLoader`
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy sam3GetObjectIds`
- `PreviewAny`
- `easy sam3Visualization`
- `GrowMaskWithBlur`
- `PreviewAny`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `SetNode`
- `OnnxDetectionModelLoader`
- `MemoryCleaner`
- `easy cleanGpuUsed`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoSetBlockSwap`
- `MemoryCleaner`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoTeaCache`
- `MemoryCleaner`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `VHS_LoadVideo`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GoogleTranslator`
- `String`

## 知识

覆盖率 **91%**（50/55）

**有卡**：`MemoryCleaner`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`easy sam3ModelLoader`、`MaskToImage`、`VHS_VideoCombine`、`easy sam3GetObjectIds`、`easy sam3Visualization`、`GrowMaskWithBlur`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`OnnxDetectionModelLoader`、`easy cleanGpuUsed`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTeaCache`、`WanVideoSampler`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`VHS_VideoInfo`、`WanVideoDecode`、`easy sam3VideoModelExtraConfig`、`easy sam3VideoSegmentation`、`VHS_LoadVideo`、`DrawViTPose`、`PoseAndFaceDetection`、`LoadImage`、`GoogleTranslator`、`String`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
