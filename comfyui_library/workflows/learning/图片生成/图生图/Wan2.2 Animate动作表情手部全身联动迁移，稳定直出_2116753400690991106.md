---
key: 图片生成/图生图/Wan2.2 Animate动作表情手部全身联动迁移，稳定直出_2116753400690991106.json
name: Wan2.2 Animate动作表情手部全身联动迁移，稳定直出_2116753400690991106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作表情手部全身联动迁移，稳定直出_2116753400690991106.json
hash: bc153480e966c6cd
coverage: 0.882353
learned_at: 2026-11-02 19:13:12
nodes: [ImageFromBatch, WanVideoSampler, MemoryCleaner, WanVideoDecode, VHS_VideoCombine, GrowMask, WanVideoContextOptions, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, WanVideoModelLoader, Evaluate Integers, ClothesSegment, easy int, ImageFromBatch, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, 孤海注释, 孤海注释, SaveImage, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate动作表情手部全身联动迁移，稳定直出_2116753400690991106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作表情手部全身联动迁移，稳定直出_2116753400690991106.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
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
- `孤海注释`
- `孤海注释`
- `SaveImage`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`ImageFromBatch`、`WanVideoSampler`、`MemoryCleaner`、`WanVideoDecode`、`VHS_VideoCombine`、`GrowMask`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoModelLoader`、`Evaluate Integers`、`ClothesSegment`、`easy int`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、SaveImage
