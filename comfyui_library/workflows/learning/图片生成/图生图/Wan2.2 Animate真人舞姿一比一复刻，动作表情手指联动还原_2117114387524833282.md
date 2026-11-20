---
key: 图片生成/图生图/Wan2.2 Animate真人舞姿一比一复刻，动作表情手指联动还原_2117114387524833282.json
name: Wan2.2 Animate真人舞姿一比一复刻，动作表情手指联动还原_2117114387524833282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate真人舞姿一比一复刻，动作表情手指联动还原_2117114387524833282.json
hash: f7a5c7f93fc6eeef
coverage: 0.833333
learned_at: 2026-11-02 19:13:13
nodes: [ImageFromBatch, WanVideoSampler, MemoryCleaner, WanVideoDecode, VHS_VideoCombine, GrowMask, WanVideoContextOptions, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, WanVideoModelLoader, Evaluate Integers, ClothesSegment, easy int, ImageFromBatch, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, SetNode, GetNode, SetNode, GetNode, 孤海注释, 孤海注释, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate真人舞姿一比一复刻，动作表情手指联动还原_2117114387524833282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate真人舞姿一比一复刻，动作表情手指联动还原_2117114387524833282.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
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
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`
- `SaveImage`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`ImageFromBatch`、`WanVideoSampler`、`MemoryCleaner`、`WanVideoDecode`、`VHS_VideoCombine`、`GrowMask`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoModelLoader`、`Evaluate Integers`、`ClothesSegment`、`easy int`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、SaveImage
