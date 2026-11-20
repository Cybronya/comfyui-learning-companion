---
key: 平台全量/Wan2.2 Animate滑板招式一比一复刻，腾空落地稳定直出_2117976480595660802.json
name: Wan2.2 Animate滑板招式一比一复刻，腾空落地稳定直出_2117976480595660802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate滑板招式一比一复刻，腾空落地稳定直出_2117976480595660802.json
hash: 51dac475fa0cd579
coverage: 0.708333
learned_at: 2026-11-14 01:05:23
nodes: [ImageFromBatch, WanVideoSampler, MemoryCleaner, WanVideoDecode, VHS_VideoCombine, GrowMask, WanVideoContextOptions, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, WanVideoModelLoader, Evaluate Integers, ClothesSegment, easy int, ImageFromBatch, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, SaveImage, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, 孤海注释, 孤海注释, ImageFromBatch, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate滑板招式一比一复刻，腾空落地稳定直出_2117976480595660802.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate滑板招式一比一复刻，腾空落地稳定直出_2117976480595660802.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `ImageFromBatch`
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GrowMask`
- `WanVideoContextOptions`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `BlockifyMask`
- `DrawMaskOnImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoModelLoader`
- `Evaluate Integers`
- `ClothesSegment`
- `easy int`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `SaveImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`
- `ImageFromBatch`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

## 知识

覆盖率 **71%**（34/48）

**有卡**：`ImageFromBatch`、`WanVideoSampler`、`MemoryCleaner`、`WanVideoDecode`、`VHS_VideoCombine`、`GrowMask`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoModelLoader`、`Evaluate Integers`、`ClothesSegment`、`easy int`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached
