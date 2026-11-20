---
key: 平台全量/Wan2.2 Animate功夫招式一比一复刻，动作发力衔接稳定直出_2117486747536945154.json
name: Wan2.2 Animate功夫招式一比一复刻，动作发力衔接稳定直出_2117486747536945154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate功夫招式一比一复刻，动作发力衔接稳定直出_2117486747536945154.json
hash: c28f953e8f1c8857
coverage: 0.885714
learned_at: 2026-11-14 01:05:11
nodes: [ImageFromBatch, WanVideoSampler, MemoryCleaner, WanVideoDecode, VHS_VideoCombine, GrowMask, WanVideoContextOptions, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, WanVideoModelLoader, Evaluate Integers, ClothesSegment, easy int, ImageFromBatch, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, SaveImage, SetNode, GetNode, 孤海注释, 孤海注释, ImageFromBatch]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate功夫招式一比一复刻，动作发力衔接稳定直出_2117486747536945154.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate功夫招式一比一复刻，动作发力衔接稳定直出_2117486747536945154.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
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
- `孤海注释`
- `孤海注释`
- `ImageFromBatch`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageFromBatch`、`WanVideoSampler`、`MemoryCleaner`、`WanVideoDecode`、`VHS_VideoCombine`、`GrowMask`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoModelLoader`、`Evaluate Integers`、`ClothesSegment`、`easy int`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、SaveImage
