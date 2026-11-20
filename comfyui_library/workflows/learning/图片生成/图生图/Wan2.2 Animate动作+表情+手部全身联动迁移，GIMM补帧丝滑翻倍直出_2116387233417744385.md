---
key: 图片生成/图生图/Wan2.2 Animate动作+表情+手部全身联动迁移，GIMM补帧丝滑翻倍直出_2116387233417744385.json
name: Wan2.2 Animate动作+表情+手部全身联动迁移，GIMM补帧丝滑翻倍直出_2116387233417744385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作+表情+手部全身联动迁移，GIMM补帧丝滑翻倍直出_2116387233417744385.json
hash: 7753ffffee620123
coverage: 0.942857
learned_at: 2026-11-02 19:13:11
nodes: [ImageFromBatch, WanVideoSampler, MemoryCleaner, WanVideoDecode, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, GrowMask, WanVideoContextOptions, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, WanVideoModelLoader, Evaluate Integers, ClothesSegment, easy int, ImageFromBatch, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadImage, WanVideoAnimateEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, 孤海注释, 孤海注释, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate动作+表情+手部全身联动迁移，GIMM补帧丝滑翻倍直出_2116387233417744385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate动作+表情+手部全身联动迁移，GIMM补帧丝滑翻倍直出_2116387233417744385.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `ImageFromBatch`
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
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

## 知识

覆盖率 **94%**（33/35）

**有卡**：`ImageFromBatch`、`WanVideoSampler`、`MemoryCleaner`、`WanVideoDecode`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`GrowMask`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoModelLoader`、`Evaluate Integers`、`ClothesSegment`、`easy int`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、SaveImage
